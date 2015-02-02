createdb -U postgres <DATABASENAME>
psql -U postgres -d <DATABASENAME> -c 'CREATE EXTENSION postgis'

CREATE EXTENSION postgis;
CREATE EXTENSION postgis_topology;
CREATE EXTENSION fuzzystrmatch;
CREATE EXTENSION postgis_tiger_geocoder;


DROP TABLE IF EXISTS truck_location;
CREATE TABLE truck_location(
locationid int,
Applicant varchar,
FacilityType varchar,
cnn int,
LocationDescription varchar,
Address varchar,
blocklot varchar,
block varchar,
lot varchar,
permit varchar,
Status varchar,
FoodItems varchar,
X double precision,
Y double precision,
Latitude double precision,
Longitude double precision,
Schedule varchar,
NOISent varchar,
Approved TIMESTAMP,
Received TIMESTAMP,
PriorPermit int,
ExpirationDate TIMESTAMP,
Location varchar
);
COPY truck_location FROM '/Users/jiefeng/Dropbox/Fun_Projects/uber/food_truck/app/Mobile_Food_Facility_Permit.csv' DELIMITER ',' CSV;

SELECT AddGeometryColumn('public', 'truck_location', 'geom', 900913, 'POINT', 2);
update truck_location set geom = ST_SetSRID(ST_MakePoint(Longitude, Latitude), 900913);
CREATE INDEX idx_points ON truck_location USING GIST (geom);

SELECT *
FROM truck_location
ORDER BY geom <-> st_setsrid(st_makepoint(-90,40),4326)
LIMIT 10;
