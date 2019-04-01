$.getJSON("static/data/gtafsadistribution.geojson", function(data){

    var mymap = L.map('mapid').setView([43.7735, -79.5019], 13);

    L.tileLayer('https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token=pk.eyJ1IjoibWFwYm94IiwiYSI6ImNpejY4NXVycTA2emYycXBndHRqcmZ3N3gifQ.rJcFIG214AriISLbB6B5aw', {
        maxZoom: 18,
        attribution: 'Map data &copy; <a href="https://www.openstreetmap.org/">OpenStreetMap</a> contributors, ' +
            '<a href="https://creativecommons.org/licenses/by-sa/2.0/">CC-BY-SA</a>, ' +
            'Imagery © <a href="https://www.mapbox.com/">Mapbox</a>',
        id: 'mapbox.streets'
    }).addTo(mymap);

    var marker = L.marker([43.7735, -79.5019]).addTo(mymap).openPopup();

    // add GeoJSON layer to the map once the file is loaded
    var datalayer = L.geoJson(data ,{
        onEachFeature: function(feature, featureLayer) {
            featureLayer.bindPopup(feature.properties.CFSAUID);
        }
    }).addTo(mymap);

    mymap.fitBounds(datalayer.getBounds());
});