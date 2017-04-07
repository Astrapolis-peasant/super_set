import os
#---------------------------------------------------------
# Superset specific config
#---------------------------------------------------------
# ROW_LIMIT = 5000
SUPERSET_WORKERS = 1 # for it to work in heroku basic/hobby dynos increase as you like

# SUPERSET_WEBSERVER_PORT = 8088
#---------------------------------------------------------

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
SQLALCHEMY_DATABASE_URI = 'postgresql://bonan:ybn1992615@tudiio.ceo7x9fchbd7.us-east-1.rds.amazonaws.com:5432/tupai_list'
MAPBOX_API_KEY = 'pk.eyJ1IjoiYm9uYW55IiwiYSI6ImNqMTczeW9zNzA0OWEzOG9kOTc4MDR5NGwifQ.1KjCtkIS4swYYL9ht5qDww	'
# Flask-WTF flag for CSRF
CSRF_ENABLED = True
