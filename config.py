import os

# Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7009285082:AAEtuj2aLvlaebPQ3G0zKbU3CLWhgS3F2X8")

# Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "22844653"))

# Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "9a656406da0a7a661348cd56a824f076")

# Your Owner / Admin Id For Broadcast 
ADMINS = int(os.environ.get("ADMINS", "8048617293"))

# Your Mongodb Database Url
# Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_URI = os.environ.get("DB_URI", "mongodb+srv://ajflixhubsssssssss:ajaytrams@cluster0.oes23.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0") # Warning - Give Db uri in deploy server environment variable, don't give in repo.
DB_NAME = os.environ.get("DB_NAME", "ajflixhubsssssssss")

# If You Want Error Message In Your Personal Message Then Turn It True Else If You Don't Want Then Flase
ERROR_MESSAGE = bool(os.environ.get('ERROR_MESSAGE', True))
