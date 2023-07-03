from sqlalchemy import create_engine
from sqlalchemy.engine import URL
from sqlalchemy.orm import sessionmaker

from dotenv import dotenv_values

config = dotenv_values('.env')

url = URL.create(
    drivername="postgresql",
    username=config.get('DB_USERNAME'),
    password=config.get('DB_PASSWORD'),
    host=config.get('DB_HOST'),
    database=config.get('DB_NAME'),
    port=config.get('DB_PORT')
)

engine = create_engine(url)
Session = sessionmaker(bind=engine)
session = Session()