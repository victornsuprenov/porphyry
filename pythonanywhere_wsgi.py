import sys
import os

# Укажите путь к вашей папке с проектом
project_home = os.path.expanduser('~/МЕДНЫЕ')
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

from app import app as application
