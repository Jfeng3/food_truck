DROP TABLE IF EXISTS Food_Location;
CREATE TABLE Food_Location(
locationid INTEGER,
Applicant TEXT,
FacilityType TEXT,
cnn INTEGER,
LocationDescription TEXT,
Address TEXT,
blocklot TEXT,
block TEXT,
lot TEXT,
permit TEXT,
Status TEXT,
FoodItems TEXT,
X REAL,
Y REAL,
Latitude REAL,
Longitude REAL,
Schedule TEXT,
NOISent TEXT,
Approved DATETIME,
Received DATETIME,
PriorPermit INTEGER,
ExpirationDate DATETIME,
Location TEXT
);
.mode csv
.import Mobile_Food_Facility_Permit.csv Food_Location