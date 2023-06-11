# Don't Edit

import os

from dotenv import load_dotenv
load_dotenv()


# Mandatory variables for the bot to start
API_ID = int(os.getenv("API_ID", "9738903"))
API_HASH = os.environ.get("API_HASH", "d05599b2b23fd03e208ca54a2ff93445")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "5757877293:AAE6MSBoRxhWDLS22CjKInvRVqodqLXc3-g")
ADMINS = [int(i.strip()) for i in os.environ.get("ADMINS").split("1030188110")] if os.environ.get("ADMINS") else []
ADMIN = ADMINS
DATABASE_NAME = os.environ.get("DATABASE_NAME", "Tajlinkshortner")
DATABASE_URL = os.getenv("DATABASE_URL", "mongodb+srv://technical:technical@cluster0.qqyb9zi.mongodb.net/?retryWrites=true&w=majority") 
OWNER_ID =  int(os.environ.get("OWNER_ID", "1030188110")) 
ADMINS.append(OWNER_ID) if OWNER_ID not in ADMINS else []
ADMINS.append(Id Owned Id)
#  Optionnal variables
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001944388469")) 
UPDATE_CHANNEL = os.environ.get("UPDATE_CHANNEL", "tajlinkofficial") # For Force Subscription
BROADCAST_AS_COPY = os.environ.get('BROADCAST_AS_COPY', "True") # true if forward should be avoided
WELCOME_IMAGE = os.environ.get("WELCOME_IMAGE", '') # image when someone hit /start # image when someone hit /start
LINK_BYPASS = "False"
