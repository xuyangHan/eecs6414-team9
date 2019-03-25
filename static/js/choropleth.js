Plotly.d3.json('static/data/map.geojson', function (torontojson) {


    let data = [{
        type: 'scattermapbox',
        lat: [43.7735],
        lon: [-79.5019]
    },

    ];

    let data_layers = [];
    for (let feature_num = 0; feature_num <= torontojson.features.length; feature_num++) {
        data_layers.push(
            {
                sourcetype: 'geojson',
                source: torontojson.features[feature_num],
                type: 'fill',
                color: 'rgba(163,22,19,0.5)',
            }
        );
    }

    let layout = {
        title: "Toronto",
        height: 600,
        mapbox: {
            center: {
                lat: 43.7735,
                lon: -79.5019
            },
            style: 'light',
            zoom: 12,
            layers: data_layers,
        }
    };


    Plotly.newPlot("dashboardDiv", data, layout, {
        mapboxAccessToken: 'pk.eyJ1IjoiY2hyaWRkeXAiLCJhIjoiRy1GV1FoNCJ9.yUPu7qwD_Eqf_gKNzDrrCQ'
    });
});

