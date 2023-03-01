import os
from dotenv import load_dotenv

basedir=os.path.abspath(os.path.dirname(__file__))

env=os.path.join(os.path.dirname(__file__),'.env')
load_dotenv(env)


class Config:
    SECRET_KEY=os.getenv('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI=os.getenv('DATABASE_URI')\
        or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    FLASK_ENV=os.getenv('FLASK_ENV')