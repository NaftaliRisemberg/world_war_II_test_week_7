import graphene as g
from graphene_sqlalchemy import SQLAlchemyObjectType
from datetime import datetime, date
from database import db_session
from models import CityModel, TargetModel, CountryModel, TargetTypeModel,MissionModel


class City(SQLAlchemyObjectType):
    class Meta:
        model = CityModel
        interfaces = (g.relay.Node,)

class Target(SQLAlchemyObjectType):
    class Meta:
        model = TargetModel
        interfaces = (g.relay.Node,)

class Country(SQLAlchemyObjectType):
    class Meta:
        model = CountryModel
        interfaces = (g.relay.Node,)

class TargetType(SQLAlchemyObjectType):
    class Meta:
        model = TargetTypeModel
        interfaces = (g.relay.Node,)

class Mission(SQLAlchemyObjectType):
    class Meta:
        model = MissionModel
        interfaces = (g.relay.Node,)

class Query(g.ObjectType):
   # return mission by id
    mission_by_id = g.Field(Mission, mission_id=g.Int(required=True))
   # return the all mission that happened between dates
    missions_by_range_of_dates = g.List(Mission, date_start=g.Date(required=True), date_end=g.Date(required=True))

    def resolve_mission_by_id(self, info, mission_id):
       return db_session.query(MissionModel).get(mission_id)

    def resolve_missions_by_range_of_dates(self, info, date_start, date_end):
        return db_session.query(MissionModel).filter(MissionModel.mission_date.between(date_start, date_end))




schema = g.Schema(query=Query)
