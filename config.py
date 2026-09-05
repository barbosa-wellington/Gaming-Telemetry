import os
from dotenv import load_dotenv


# loading the environment variable from the .end file
load_dotenv()

# Create an object for accessing each variable of the file .env
class Config:

    API_STEAM = os.environ.get("API_STEAM")
    ID_STEAM = os.environ.get("ID_STEAM")

if not Config.API_STEAM:
    raise ValueError("Critical Error: API_Steam")