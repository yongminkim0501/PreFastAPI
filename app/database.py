import json
import os
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SECRET_FILE = os.path.join(BASE_DIR, 'secret.json')
secrets = json.load(open(SECRET_FILE).read())
db = secrets["db"]

SQLALCHEMY_DATABASE_URL = f"mysql+pymysql://{db.get('user')}:{db.get('password')}@{db.get('host')}:{db.get('port')}/{db.get('database')}?charset=utf8"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()