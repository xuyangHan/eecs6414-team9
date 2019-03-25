Plotly.d3.json('static/data/map.geojson', function (torontojson) {


    let data = [{
        type: 'scattermapbox',
        lat: [43.7735],
        lon: [-79.5019]
    },

    ];

    let data_layers = [];
    for (let feature_num = 0; feature_num <= torontojson["features"].length; feature_num++) {
        let source = torontojson["features"][feature_num];
        // let gb_value = 255 - source["students"];
        let gb_value = 15 + feature_num * 4;
        let color = 'rgba(163, ' + gb_value + ', ' + gb_value +', 0.5)';
        data_layers.push(
            {
                sourcetype: 'geojson',
                source: source,
                type: 'fill',
                color: color,
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

