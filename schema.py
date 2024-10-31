import graphene as g
from graphene_sqlalchemy import SQLAlchemyObjectType
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
        model= MissionModel
        name='Mission'
        interfaces = (g.relay.Node,)

class Query(g.ObjectType):
   # return mission by id
    mission_by_id = g.Field(Mission, mission_id=g.Int(required=True))
   # return the all mission that happened between dates
    missions_by_range_of_dates = g.List(Mission, date_start=g.Date(required=True), date_end=g.Date(required=True))
   # return tha all mission by country they took part in
    missions_by_country = g.List(Mission, country=g.String(required=True))

    def resolve_mission_by_id(self, info, mission_id):
       return db_session.query(MissionModel).get(mission_id)

    def resolve_missions_by_range_of_dates(self, info, date_start, date_end):
        return db_session.query(MissionModel).filter(MissionModel.mission_date.between(date_start, date_end))

 #   def resolve_mission_by_country(self, info, country):
  #      return db_session.query(MissionModel).join(MissionModel.target).join()

# Mutations

class AddMission(g.Mutation):
    class Arguments:
        mission_id = g.Int(required=True)
        mission_date = g.Date(required=True)
        airborne_aircraft = g.String(required=True)
        attacking_aircraft = g.Int(required=True)
        bombing_aircraft = g.Int(required=True)
        aircraft_returned = g.Int(required=True)
        aircraft_failed = g.Int(required=True)
        aircraft_damaged = g.Int(required=True)

    mission = g.Field(lambda: MissionModel)

    def mutate(self, info, mission_date, airborne_aircraft, attacking_aircraft,bombing_aircraft,
               aircraft_returned, aircraft_failed, aircraft_damaged):
        new_mission = MissionModel(mission_date=mission_date, airborne_aircraft=airborne_aircraft, attacking_aircraft=attacking_aircraft,
                                   bombing_aircraft=bombing_aircraft, aircraft_returned=aircraft_returned, aircraft_failed=aircraft_failed,
                                   aircraft_damaged=aircraft_damaged)

        db_session.add(new_mission)
        db_session.commit()
        db_session.refresh(new_mission)
        return AddMission(missioin=new_mission)

class Mutation(g.ObjectType):
    add_mission = AddMission.Field()


schema = g.Schema(query=Query, mutation=Mutation)