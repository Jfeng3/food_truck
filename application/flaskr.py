
import os
from sqlite3 import dbapi2 as sqlite3
import pg
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash, json


# create our little application :)
app = Flask(__name__)


app.config.from_pyfile('map_config.py')

@app.route('/')
def index():
    return render_template('index.html')

#return trucks close to given location:
@app.route("/trucks")
def get_k_nearest_truck():
    table_name = app.config['TABLE_NAME']
    db = get_db()
    
    #get request parameters
    latitude = str(request.args.get('lat'))
    longitude = str(request.args.get('lon'))
    #query the DB for all the parkpoints
    result = db.query(' SELECT * FROM '+table_name+' ORDER BY geom <-> st_setsrid(st_makepoint(' + latitude+','+longitude+'),4326) LIMIT 1;')
#    result = db.query('SELECT gid,name,ST_X(the_geom) as lon,ST_Y(the_geom) as lat FROM '+ table_name+";")

    #Now turn the results into valid JSON
    return str(json.dumps(list(result.dictresult())))

    #bounding box (within?lat1=45.5&lon1=-82&lat2=46.5&lon2=-81)
@app.route("/trucks/within")
def within():
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

def connect_db():
    """Connects to the specific database."""
    db = pg.connect(app.config['APP_NAME'], \
         app.config['PG_DB_HOST'], \
         app.config['PG_DB_PORT'], \
         None, None, \
         app.config['PG_DB_USERNAME'], \
         app.config['PG_DB_PASSWORD'] )
    return db


def init_db():
    """Initializes the database."""
    db = get_db()
    with app.open_resource('schema.sql', mode='r') as f:
        db.cursor().executescript(f.read())
    db.commit()


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
        g.postgre_db = connect_db()
    return g.postgre_db


@app.teardown_appcontext
def close_db(error):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'postgre_db'):
        g.postgre_db.close()


@app.route('/show')
def show_entries():
    db = get_db()
    table_name = app.config['TABLE_NAME']
    
    result = db.query(' SELECT * FROM '+table_name+';')
    return render_template('index.html', entries=result)

if __name__=="__main__":
    app.run()
