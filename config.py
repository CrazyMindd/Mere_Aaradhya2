import os

API_ID = API_ID = 28773160

API_HASH = os.environ.get("API_HASH", "37bdcd1fce6d5edc6f5f8b28b44c9e8c")

BOT_TOKEN = os.environ.get("BOT_TOKEN", "7167815618:AAGQq7CCohs9vAzt-gBI0UO2suvjQxGHX7E")

PASS_DB = int(os.environ.get("PASS_DB", "721"))

OWNER = int(os.environ.get("OWNER", 6329158981))

LOG = -1002024552188

try:
    ADMINS=[]
    for x in (os.environ.get("ADMINS", "6329158981").split()):
        ADMINS.append(int(x))
except ValueError:
        raise Exception("Your Admins list does not contain valid integers.")
ADMINS.append(OWNER)


