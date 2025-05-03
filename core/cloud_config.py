import os
from dotenv import load_dotenv
load_dotenv()

class CloudConfig:
    username = os.getenv("AUTH_ID")
    password = os.getenv("AUTH_PASSWORD")
    project_name = "RTDS---Hackathon"
    domain_name = "Default"

   