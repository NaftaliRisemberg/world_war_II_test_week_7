from flask import Flask
from flask_graphql import GraphQLView
from database import db_session, db_url
#from schema import schema


app = Flask(__name__)
app.debug = True

app.config["SQLALCHEMY_DATABASE_URI"] = db_url
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False


app.add_url_rule(
    '/graphql',
    view_func=GraphQLView.as_view(
        'graphql',
        #schema=schema,
        graphiql=True
    )
)

if __name__ == "__main__":
    app.run(host='0.0.0.0',
            port=5001)
