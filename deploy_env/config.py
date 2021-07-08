# THIS IS A SAMPLE FILE
# THIS WILL GOES TO local_settings.py
# EDIT THIS CONFIG BEFORE DEPLOY TO PRODUCTION

API_URL = "http://grader-api" # Name of the service (docker)
API_SEND_PORT = 11112
API_LISTEN_PORT = 8000

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-%!98v0b6^lp9$kr)cwb2@4s*f!oq1o+_1m_4qwo5%^sheam&29'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: don't run with allowed hosts all
ALLOWED_HOSTS = ['*']