// map.js
var map = L.map('map').setView([47.3667, 8.5500], 12); // Koordinaten für Zürich, Zoom-Level 10
let position;

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

// Marker für ausgewählten Standort
var marker = L.marker([47.3667, 8.5500], { draggable: true }).addTo(map);
position= marker.getLatLng();

// Event-Handler für das Verschieben des Markers
marker.on('dragend', function(event){
    position = marker.getLatLng(); // Aktuelle Position des Markers
    console.log('Neue Position:', position.lat, position.lng); // Ausgabe der Koordinaten in der Konsole
});


// Optional: Marker für Zürich hinzufügen
/* L.marker([47.3667, 8.5500]).addTo(map)
    .bindPopup('Zürich Canton')
    .openPopup(); */

/*
var map = L.map('map').setView([47.3667, 8.5500], 10); // Koordinaten für Zürich, Zoom-Level 10

L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
    attribution: '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> contributors'
}).addTo(map);

// Laden und Anzeigen der GeoJSON-Grenzdaten des Kantons Zürich
fetch('/static/map.geojson')
    .then(function(response) {
        return response.json();
    })
    .then(function(data) {
        L.geoJSON(data, {
            style: function(feature) {
                return {
                    color: 'blue', // Farbe der Grenzlinie
                    weight: 2, // Dicke der Linie
                    opacity: 1 // Deckkraft der Linie
                };
            }
        }).addTo(map);
    });
*/

document.getElementById('submitBtn').addEventListener('click', function() {
    if (position) {
      $.ajax({
        url: '/submit',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({
          lat: position.lat,
          lng: position.lng
        }),
        success: function(response) {
          console.log(response);
  
          // Update the DOM with response data
          const nearestNeighborElement = document.getElementById('nearestNeighbor');
          const coefficientElement = document.getElementById('coefficient');
          const nodes = document.getElementById('nodes');

  
          if (nearestNeighborElement) {
            nearestNeighborElement.textContent = "Anzahl nodes innerhalb von 1km: "+response.amount_nearest_neighbor;
          }

         /*  if (nodes) {
            nearestNeighborElement.textContent = "Nodes: "+response.nodes;
          } */
  
          if (coefficientElement) {
            coefficientElement.textContent = "Koeffizient: "+response.coefficient;
          } else {
            alert("An error occurred. Missing element for coefficient");
          }
        },
        error: function(xhr) {
          console.log("Error:", xhr);
        }
      });
    } else {
      alert("Please select a location on the map first.");
    }
  });
  