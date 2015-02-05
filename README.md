Food Truck by Jie Feng
I am new to web development. My background is mainly on algorithm/data science
This is my first web application

How to run
1. Need install postgresql with postgis extension
2. Adjust information in map_config.py(PG_DB_USERNAME, PG_DB_PASSWORD) and create database food_truck 
2. Clone this repo and cd application
3. Run food_truck_map.py. should see a map with pins indicating food truck locations. 
4. The server will now be listening on localhost:5000

Server: Use flask, food_truck_map.py
I use postgresql database with postgis to extract k nearest neighbor locations
Response to the follwing request:

    1. "/trucks/?lat=a&lon=b": 
    Return the closest food truck infomation near the location (latitude=a, longitude=b)
    
    2. "/trucks/?lat1=a1&lon1=b1&lat2=a2&lon2=b2":
    Return at most 25 truck locations inside rectangle formed by (lat1,lon1,lat2,lon2)
    
    3. "/"
    Return at most 25 food truck locations within current map bound
    

 

