from typing import Text
from sqlalchemy.orm import sessionmaker
from enum import Enum
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.schema import Column
from sqlalchemy.types import String, Integer, Text
from dotenv import load_dotenv
import os

load_dotenv()

engine = create_engine(os.environ.get("DATABASE_URI"))
Base = declarative_base() 

class Model(Base):
    __tablename__ = "model"
    id = Column(Integer, primary_key=True)
    share_id = Column(String(32))
    twitter_id = Column(String(32))
    model_json = Column(Text)
    
    def __init__(self, unique_id, model_json_string, twitter_id=""):
        self.share_id = unique_id
        self.model_json = model_json_string
        self.twitter_id = twitter_id

    def load_model():
        pass        

    def save_model(model):
        pass

Base.metadata.create_all(engine)

def clean_DB():
    SessionClass = sessionmaker(engine)
    session = SessionClass()
    session.query(Model).delete()
    all_models = session.query(Model).all()
    print("Nothing should be below")
    for i in all_models: print(i)
    session.close()

import random, string

def get_random_id(length):
    randlst = [random.choice(string.ascii_letters + string.digits) for i in range(length)]
    return ''.join(randlst)


if __name__ == "__main__":
    # Model.__table__.drop(engine)
    pass
    # clean_DB()