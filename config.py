import os

from instance.config import DATABASE_URL 

class Config:
  '''
  General configuration parent class
  '''
  SECRET_KEY = 'k9YIw3u'
  SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://wachira:Lydiah007@localhost/pitches'
  UPLOADED_PHOTOS_DEST ='app/static/photos'
  SQLALCHEMY_TRACK_MODIFICATIONS=True

  #  email configurations
  MAIL_SERVER = 'smtp.googlemail.com'
  MAIL_PORT = 587
  MAIL_USE_TLS = True
  MAIL_USERNAME='oneminutepitches@gmail.com'
  MAIL_PASSWORD='wakadinali'



  @staticmethod
  def init_app(app):
        pass

class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL').replace("://", "ql://", 1)

DEBUG = True

class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://wachira:Lydiah007@localhost/pitches'
    
DEBUG = True

config_options = {
    'development':DevConfig,
    'production': ProdConfig
}