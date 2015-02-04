var map = L.map('map').setView([37.790149087496, -122.39865818459], 16);
var markerLayerGroup = L.layerGroup().addTo(map);
L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
  maxZoom: 18,
  attribution: 'Map data &copy; <a href="https://openstreetmap.org">OpenStreetMap</a> contributors, <a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>'
}).addTo(map);

function getPins(e){
  bounds = map.getBounds();
  url = "trucks/within?lat1=" + bounds.getSouthWest().lat + "&lon1=" + bounds.getSouthWest().lng + "&lat2=" + bounds.getNorthEast().lat + "&lon2=" + bounds.getNorthEast().lng;
  $.get(url, pinTheMap, "json")
}

function pinTheMap(data){
  //clear the current pins
  map.removeLayer(markerLayerGroup);

  //add the new pins
  console.log("Hello");
  var markerArray = new Array(data.length)
  console.log(data.length);
  for (var i = 0; i < data.length; i++){
    truck = data[i];
    
    markerArray[i] = L.marker([truck.latitude, truck.longitude]).bindPopup(truck.fooditems);
  }

  markerLayerGroup = L.layerGroup(markerArray).addTo(map);
}

map.on('dragend', getPins);
map.on('zoomend', getPins);
map.whenReady(getPins)

