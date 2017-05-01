import os
import sys
from superset import config
import shutil
import stat

def copytree(src, dst, symlinks = False, ignore = None):
  if not os.path.exists(dst):
    os.makedirs(dst)
    shutil.copystat(src, dst)
  lst = os.listdir(src)
  if ignore:
    excl = ignore(src, lst)
    lst = [x for x in lst if x not in excl]
  for item in lst:
    s = os.path.join(src, item)
    d = os.path.join(dst, item)
    if symlinks and os.path.islink(s):
      if os.path.lexists(d):
        os.remove(d)
      os.symlink(os.readlink(s), d)
      try:
        st = os.lstat(s)
        mode = stat.S_IMODE(st.st_mode)
        os.lchmod(d, mode)
      except:
        pass # lchmod not available
    elif os.path.isdir(s):
      copytree(s, d, symlinks, ignore)
    else:
      shutil.copy2(s, d)



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
SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://admin:admin@localhost:5432/superset'
# MAPBOX_API_KEY = 'pk.eyJ1IjoiYm9uYW55IiwiYSI6ImNqMTczeW9zNzA0OWEzOG9kOTc4MDR5NGwifQ.1KjCtkIS4swYYL9ht5qDww	'
# Flask-WTF flag for CSRF
CSRF_ENABLED = False
APP_NAME = "tudi.io"


CSRF_ENABLED = False

LANGUAGES = {
    'en': {'flag': 'us', 'name': 'English'},
    # 'fr': {'flag': 'fr', 'name': 'French'},
    'zh': {'flag': 'cn', 'name': 'Chinese'},
}

# config.APP_ICON = "/static_files/tudi.png"
BASE_DIR = os.path.abspath(os.path.dirname(__file__))
superset_path = config.BASE_DIR
relative_path = os.path.relpath(superset_path,BASE_DIR)

print ("path", relative_path)
copytree('superset', relative_path)
print ("files copied")

APP_ICON = "/static/assets/images/data_top.png"






