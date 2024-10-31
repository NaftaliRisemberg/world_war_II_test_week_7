from sqlalchemy import Column, Integer, String, Float, Date, Table, ForeignKey, Index
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class CityModel(Base):
    _tablename_ = 'cities'
    city_id = Column(Integer, primary_key=True)
    city_name = Column(String)
    country_id = Column(Integer, ForeignKey('countries.country_id')) # מפתח זר של המדינה עיר יכולה להיות במדינה אחת לכל מדינה יש כמה ערים
    latitude = Column(Float)
    longitude = Column(Float)
    city = relationship("CityModel", back_populates="countries")

class CountryModel(Base):
    _tablename_ = 'countries'
    country_id = Column(Integer, primary_key=True)
    country_name = Column(String)
    cities = relationship("CityModel", back_populates="countries")

class TargetTypeModel(Base):
    _tablename_ = 'targettypes'
    target_type_id = Column(Integer, primary_key=True)
    target_type_name = Column(String)

class TargetModel(Base):
    _tablename_ = 'targets'
    target_id = Column(Integer, primary_key=True)
    mission_id = Column(Integer, ForeignKey('mission.mission_id'))
    target_industry = Column(String)
    city_id = Column(Integer, ForeignKey('cities.city_id'))
    target_type_id = Column(Integer, ForeignKey('targettypes.target_type_id'))
    target_priority = Column(Integer)

class MissionModel(Base):
    _tablename_ = 'missions'
    mission_id = Column(Integer, primary_key=True)
    mission_date = Column(Date)
    airborne_aircraft = Column(Integer)
    attacking_aircraft = Column(Integer)
    bombing_aircraft = Column(Integer)
    aircraft_returned = Column(Integer)
    aircraft_failed = Column(Integer)
    aircraft_damaged = Column(Integer)