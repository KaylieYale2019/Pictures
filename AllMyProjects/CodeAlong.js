//My Variables!
var map;
var ourLoc;
var view;

//Intialize a Function
function init(){
  //Shaunti provided these lon/Lat values :D
  ourLoc = ol.proj.fromLonLat([-84.3869,33.7739]);

  view = new ol.View({
    center: ourLoc,

    zoom: 18 // You can change this value for the aesthetics
  });

  map = new ol.Map({
    target: 'map',
    layers: [
      new ol.layer.Tile({
        source: new ol.source.OSM()
      })
    ],
    loadTilesWhileAnimating: true,
    view: view
  });
}

function panHome(){
  view.animate({
    center: ourLoc,
    duration: 2000 //2000 milliseconds = 2 secs
  });
}
function panToLocation(){
  var countryName = document.getElementById("country-name").value;
  var lon = 0.0;
  var lat = 0.0;

  if(countryName === ""){
    alert("You didn't enter a country name!")
  }
  //Find variables from REST Countries API
  var query = "https://restcountries.eu/rest/v2/name/" + countryName;
  query = query.replace(/ /g, "%20")
  alert(query);

  var countryRequest = new XMLHttpRequest();
  countryRequest.open('GET', query, false);
  countryRequest.send();

  alert("Ready State" + countryRequest.readyState);
  alert("Status" + countryRequest.status);
  alert("Response" + countryRequest.responseText);

  var location = ol.proj.fromLonLat([lon,lat]);

  view.animate({
    center: location,
    duration: 2000
  });
}

window.onload = init;
