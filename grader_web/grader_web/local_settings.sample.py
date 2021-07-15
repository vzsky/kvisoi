# THIS IS A SAMPLE FILE
# EDIT THIS CONFIG BEFORE DEPLOY TO PRODUCTION

API_URL = "http://grader-api" # Name of the service (docker)
API_SEND_PORT = 11112
API_LISTEN_PORT = 8000

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'anysecretkey'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: don't run with allowed hosts all
ALLOWED_HOSTS = ['*']