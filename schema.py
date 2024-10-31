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

    def resolve_mission_by_id(self, info, mission_id):
       return db_session.query(MissionModel).get(mission_id)

schema = g.Schema(query=Query)