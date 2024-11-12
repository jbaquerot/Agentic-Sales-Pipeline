# src/email_engagement.py
import logging
from pydantic import BaseModel, Field
from typing import List, Dict
from errors import KickoffError, ValidationError
from crewai import Agent, Task, Crew
from crewai_tools import SerperDevTool, ScrapeWebsiteTool
import yaml

# Define file paths for YAML configurations
files = {
    'email_agents': 'config/email_engagement_agents.yaml',
    'email_tasks': 'config/email_engagement_tasks.yaml',
}

# Load configurations from YAML files
configs = {}
for config_type, file_path in files.items():
    with open(file_path, 'r') as file:
        configs[config_type] = yaml.safe_load(file)

email_agents_config = configs['email_agents']
email_tasks_config = configs['email_tasks']


email_content_specialist = Agent(
    config=email_agents_config['email_content_specialist']
)

engagement_strategist = Agent(
    config=email_agents_config['engagement_strategist']
)

# Tasks
email_drafting = Task(
    config=email_tasks_config['email_drafting'],
    agent=email_content_specialist
)

engagement_optimization = Task(
    config=email_tasks_config['engagement_optimization'],
    agent=engagement_strategist
)

# Crew
email_writing_crew = Crew(
    agents=[
        email_content_specialist,
        engagement_strategist
    ],
    tasks=[
        email_drafting,
        engagement_optimization
    ],
    verbose=True
)

# Logging
logger = logging.getLogger(__name__)
