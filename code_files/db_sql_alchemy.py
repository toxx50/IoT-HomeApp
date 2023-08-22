from sqlalchemy import create_engine, ForeignKey, Column, String, Integer, CHAR
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import *
from time import *


Base = declarative_base()


class WeatherData(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    date = Column("date", String)
    time = Column("time", String)
    temperature = Column("temperature", String)
    humidity = Column("humidity", String)
    air_pressure = Column("air pressure", String)

    def __init__(self, date, time, temp, hum,ap):
        self.date = date
        self.time = time
        self.temperature = temp
        self.humidity = hum
        self.air_pressure = ap


engine = create_engine("sqlite:///db-temp/users.db", echo=False)
Base.metadata.create_all(bind=engine)

Session = sessionmaker(bind=engine)
session = Session()



#podatci iz baze u listi
users = session.query(WeatherData)






