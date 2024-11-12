# src/lead_qualification.py
import logging
from pydantic import BaseModel, Field
from typing import List, Dict
from errors import KickoffError, ValidationError
from models import LeadScoringResult
from crewai.flow.flow import listen, start
from crewai import Flow, Agent, Task, Crew
from crewai_tools import SerperDevTool, ScrapeWebsiteTool
from email_engagement import email_writing_crew 
import yaml

from src import email_engagement

# Logging
logger = logging.getLogger(__name__)


# Models
class Lead(BaseModel):
    lead_data: Dict
    our_data: Dict

class LeadsRequest(BaseModel):
    leads: List[Lead]

# Flow
class SalesPipeline(Flow):
    def __init__(self, leads):
        super().__init__()
        self.leads = leads

    @start()
    def score_leads(self):
        scores = lead_scoring_crew.kickoff_for_each(self.leads)
        self.state["score_crews_results"] = scores
        return scores
    
    @listen(score_leads)
    def store_leads_score(self, scores):
        # Here we would store the scores in the database
        return scores

    @listen(score_leads)
    def filter_leads(self, scores):
        return [score for score in scores if score['lead_score'].score > 70]

    @listen(filter_leads)
    def write_email(self, leads):
        scored_leads = [lead.to_dict() for lead in leads]
        emails = email_writing_crew.kickoff_for_each(scored_leads)
        return emails

    @listen(write_email)
    def send_email(self, emails):
        # Here we would send the emails to the leads
        return emails

# Load configurations from YAML files
# Define file paths for YAML configurations
files = {
    'lead_agents': 'config/lead_qualification_agents.yaml',
    'lead_tasks': 'config/lead_qualification_tasks.yaml'
}

# Load configurations from YAML files
configs = {}
for config_type, file_path in files.items():
    with open(file_path, 'r') as file:
        configs[config_type] = yaml.safe_load(file)

lead_agents_config = configs['lead_agents']
lead_tasks_config = configs['lead_tasks']


# Creating Agents
lead_data_agent = Agent(
    config=lead_agents_config['lead_data_agent'],
    tools=[SerperDevTool(), ScrapeWebsiteTool()]
)

cultural_fit_agent = Agent(
    config=lead_agents_config['cultural_fit_agent'],
    tools=[SerperDevTool(), ScrapeWebsiteTool()]
)

scoring_validation_agent = Agent(
    config=lead_agents_config['scoring_validation_agent'],
    tools=[SerperDevTool(), ScrapeWebsiteTool()]
)


# Creating Tasks
lead_data_task = Task(
    config=lead_tasks_config['lead_data_collection'],
    agent=lead_data_agent
)

cultural_fit_task = Task(
    config=lead_tasks_config['cultural_fit_analysis'],
    agent=cultural_fit_agent
)

scoring_validation_task = Task(
    config=lead_tasks_config['lead_scoring_and_validation'],
    agent=scoring_validation_agent,
    context=[lead_data_task, cultural_fit_task],
    output_pydantic = LeadScoringResult
)

# Creating Crews
lead_scoring_crew = Crew(
    agents=[
        lead_data_agent,
        cultural_fit_agent,
        scoring_validation_agent
    ],
    tasks=[
        lead_data_task,
        cultural_fit_task,
        scoring_validation_task
    ],
    verbose=True
)

