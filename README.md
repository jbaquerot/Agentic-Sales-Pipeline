# L_3_Agentic Sales Pipeline

Este proyecto implementa un pipeline de ventas utilizando agentes y tareas configurados en archivos YAML. La aplicación está construida con FastAPI y utiliza la biblioteca `crewai` para la gestión de agentes y tareas.

## Estructura del Proyecto
```t
L_3_Agentic_Sales_Pipeline/ 
├── config/ 
│ ├── lead_qualification_agents.yaml 
│ ├── lead_qualification_tasks.yaml 
│ ├── email_engagement_agents.yaml 
│ ├── email_engagement_tasks.yaml 
├── src/ 
│ ├── __init__.py 
│ ├── agents.py 
│ ├── tasks.py 
│ ├── crews.py 
│ ├── models.py 
│ ├── flow.py 
│ ├── main.py 
│ ├── routes.py 
│ ├── errors.py 
│ ├── logging_config.py 
│ └── services.py
├── test/ 
│ ├── __init__.py 
│ ├── test_routes.py 
│ └── test_services.py
├── .env 
├── app.py 
├── pytest.ini
├── requirements.txt 
└── README.md
```

## Configuración

1. Clona el repositorio:
```sh
git clone https://github.com/tu_usuario/L_3_Agentic_Sales_Pipeline.git
cd L_3_Agentic_Sales_Pipeline
```
2. Instala las dependencias:
```sh
pip install -r requirements.txt
```
3. Configura las variables de entorno necesarias en un archivo .env o directamente en el código.

## Ejecución
1. Para ejecutar el pipeline de ventas:
```sh
python src/main.py
```
2. Para iniciar el servidor FastAPI:
```sh
uvicorn app:app --reload
```

## Endpoints

* POST /start_pipeline/: Inicia el pipeline de ventas con los leads proporcionados.
## Ejemplo de Solicitud
```t
[
    {
        "name": "João Moura",
        "job_title": "Director of Engineering",
        "company": "Clearbit",
        "email": "joao@clearbit.com",
        "use_case": "Using AI Agent to do better data enrichment."
    }
]
```
## Ejemplo de Respuesta


```t
{
    "emails": [
        {
            "subject": "Interesado en nuestros servicios",
            "body": "Hola João, estamos interesados en conocer más sobre su uso de AI Agent para la mejora del enriquecimiento de datos."
        }
    ]
}
```




