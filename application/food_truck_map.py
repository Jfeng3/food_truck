"""
    food_truck_map
    ~~~~~~~~~~~~
    The food truck map application.
    :copyright: (c) 2015 by Jie Feng
    :license: BSD, see LICENSE for more details.
"""
import os
import pg
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash, json
# create our little application :)
app = Flask(__name__)

# load config file
app.config.from_pyfile('map_config.py')

@app.route('/')
def index():
    return render_template('index.html')

#return trucks close to given location:
@app.route("/trucks")
def get_nearest_truck():
    table_name = app.config['TABLE_NAME']
    db = get_db()
    
    #get request parameters
    latitude = str(request.args.get('lat'))
    longitude = str(request.args.get('lon'))
    #query the DB for all the truck points
    result = db.query(' SELECT * FROM '+table_name+' ORDER BY geom <-> st_setsrid(st_makepoint(' + latitude+','+longitude+'),4326) LIMIT 1;')

    #Now turn the results into valid JSON
    return str(json.dumps(list(result.dictresult())))

#return trucks in bounding box 
@app.route("/trucks/within")
def trucks_within():
    table_name = app.config['TABLE_NAME']
    db = get_db()
    #get the request parameters
    lat1 = str(request.args.get('lat1'))
    lon1 = str(request.args.get('lon1'))
    lat2 = str(request.args.get('lat2'))
    lon2 = str(request.args.get('lon2'))
    limit = 25

    #use the request parameters in the query
    result = db.query("SELECT * FROM "+table_name+" t WHERE ST_Intersects( \
        ST_MakeEnvelope("+lon1+", "+lat1+", "+lon2+", "+lat2+", 4326), t.geom) LIMIT "+str(limit)+";")

    #turn the results into valid JSON
    return str(json.dumps(list(result.dictresult())))

def init_db():
    """Initializes the database."""
    db = get_db()
    #db.query("CREATE EXTENSION postgis;")
    with app.open_resource('schema.sql', mode='r') as f:
        query_text = f.read()
        query_text = query_text.replace("truck_location",app.config['TABLE_NAME'])
        db.query(query_text)


@app.cli.command('initdb')
def initdb_command():
    """Creates the database tables."""
    init_db()
    print('Initialized the database.')


def get_db():
    """Opens a new database connection if there is none yet for the
    current application context.
    """
    if not hasattr(g, 'postgre_db'):
        g.postgre_db = pg.connect(app.config['DATABASE_NAME'], \
                 app.config['PG_DB_HOST'], \
                 app.config['PG_DB_PORT'], \
                 None, None, \
                 app.config['PG_DB_USERNAME'], \
                 app.config['PG_DB_PASSWORD'] )
    return g.postgre_db


@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'postgre_db'):
        g.postgre_db.close()


@app.route("/test")
def test():
    "small test"
    return "Hello World!"

if __name__=="__main__":
    app.run()
