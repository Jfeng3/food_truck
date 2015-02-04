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
COPY truck_location FROM '/Users/jiefeng/Dropbox/Fun_Projects/uber/food_truck/application/Resource/Mobile_Food_Facility_Permit.csv' DELIMITER ',' CSV HEADER;
SELECT AddGeometryColumn('public', 'truck_location', 'geom', 4326, 'POINT', 2);
update truck_location set geom = ST_SetSRID(ST_MakePoint(Longitude, Latitude), 4326);


