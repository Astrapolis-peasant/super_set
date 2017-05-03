import os
import sys
from superset import config
from copy_replace_files import copytree

# BASE_DIR = os.path.abspath(os.path.dirname(__file__))
#---------------------------------------------------------
# Superset specific config
#---------------------------------------------------------
# ROW_LIMIT = 5000
SUPERSET_WORKERS = 1 # for it to work in heroku basic/hobby dynos increase as you like

# SUPERSET_WEBSERVER_PORT = 8088
#---------------------------------------------------------

# export PYTHONPATH=$WHEREYOURCONFIGIS:$PYTHONPATH

#---------------------------------------------------------
# Flask App Builder configuration
#---------------------------------------------------------
# Your App secret key
SECRET_KEY = '\2\1thisismyscretkey\1\2\e\y\y\h'  # noqa

# The SQLAlchemy connection string to your database backend
# This connection defines the path to the database that stores your
# Superset metadata (slices, connections, tables, dashboards, ...).
# Note that the connection information to connect to the datasources
# you want to explore are managed directly in the web UI
SQLALCHEMY_DATABASE_URI = 'postgresql://bonan:ybn1992615@tudiio.ceo7x9fchbd7.us-east-1.rds.amazonaws.com:5432/superset_db'
# SQLALCHEMY_DATABASE_URI = 'postgresql://admin:admin@localhost:5432/superset'
MAPBOX_API_KEY = 'pk.eyJ1IjoiYm9uYW55IiwiYSI6ImNqMTczeW9zNzA0OWEzOG9kOTc4MDR5NGwifQ.1KjCtkIS4swYYL9ht5qDww'
# Flask-WTF flag for CSRF
CSRF_ENABLED = False
APP_NAME = "tudi.io"


CSRF_ENABLED = False

LANGUAGES = {
    'en': {'flag': 'us', 'name': 'English'},
    # 'fr': {'flag': 'fr', 'name': 'French'},
    'zh': {'flag': 'cn', 'name': 'Chinese'},
}

#config the cache
CACHE_CONFIG = {'CACHE_TYPE': 'redis'}


# config.APP_ICON = "/static_files/tudi.png"
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
superset_path = config.BASE_DIR
relative_path = os.path.relpath(superset_path,BASE_DIR)

print ("path", relative_path)
copytree('superset', relative_path)
print ("files copied")

APP_ICON = "/static/assets/images/data_top.png"
AUTH_ROLE_PUBLIC = 'Public'





