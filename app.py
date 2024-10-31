from flask import Flask
from flask_graphql import GraphQLView
from sqlalchemy.orm import sessionmaker
from database import db_session, db_url, init_db, engine
from schema import schema


app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = db_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

#session_maker = sessionmaker(bind=engine)
with app.app_context():
    init_db()

app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        schema=schema,
        graphiql=True
    )
)

if __name__ == "__main__":
    app.run(debug = True)
