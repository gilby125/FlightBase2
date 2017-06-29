import os

# WTF_CSRF_ENABLED = True
# SECRET_KEY = 'you-will-never-guess'

class BaseConfig(object):
	DEBUG = False
	SQLALCHEMY_DATABASE_URI = os.environ["DATABASE_URL"]


class DevConfig(BaseConfig):
	DEBUG = True


class ProdConfig(BaseConfig):
	DEBUG = False