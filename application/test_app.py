"""
    map Tests
    ~~~~~~~~~~~~
    Tests the map application.
    :copyright: (c) 2015 by Jie Feng
    :license: BSD, see LICENSE for more details.
"""
import pytest
import os
import map
import json
@pytest.fixture
def client(request):
    map.app.config['TESTING'] = True
    map.app.config['TABLE_NAME'] = "test_food_truck"
    client = map.app.test_client()
    with map.app.app_context():
        map.init_db()
    def teardown():
        pass
    request.addfinalizer(teardown)
    return client
    
def test_get_trucks(client):
    """test get nearest truck location"""
    rv = client.get('/trucks?lat=37.790149087496&lon=-122.39865818459')
    truck_info = json.loads(rv.data)
    assert truck_info[0]['longitude'] == -122.390016333636
    
def test_trucks_within(client):
    """test trucks within a rectangle"""
    rv = client.get('/trucks/within?lat1=37.78658909826544&lon1=-122.40637421607971&lat2=37.793795881958815&lon2=-122.39244818687439')
    truck_info = json.loads(rv.data)
    assert len(truck_info) == 25
    assert truck_info[0]['longitude'] == -122.394593199235