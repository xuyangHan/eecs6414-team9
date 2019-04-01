let yorkU_data = {
    type: 'scattermapbox',
    name: 'YorkU',
    lat: ['43.7735'],
    lon: ['-79.5019'],
    mode: 'markers',
    marker: {
        color: 'rgb(255, 0, 0)',
        size: 14,
    },
    text: ['YorkU']
};

Plotly.d3.json('static/data/map.geojson', function (torontojson) {
    Plotly.d3.csv('static/data/final.CSV', function (err, rows) {
        function unpack(rows, key) {
            return rows.map(function (row) {
                return row[key];
            });
        }

        let student_data =
            {
                type: 'scattermapbox',
                mode: 'markers',
                lon: unpack(rows, 'cent_long'),
                lat: unpack(rows, 'cent_lat'),
                text: unpack(rows, 'num_students'),
                name: 'students',
                marker: {
                    size: unpack(rows, 'num_students'),
                    opacity: 0.8,
                }
            };

        let data = [yorkU_data, student_data];


        let data_layers = [];
        for (let feature_num = 0; feature_num < torontojson["features"].length; feature_num++) {
            let source = torontojson["features"][feature_num];
            let r_value = 255 - source["commute_time"] * 250 / 1500;
            let g_value = 255 - source["commute_time"] * 125 / 1500;
            let b_value = 255 - source["commute_time"] * 250 / 1500;
            let color = 'rgba(' + r_value + ', ' + g_value + ', ' + b_value + ', 0.5)';
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
            autosize: true,
            title: "Toronto",
            height: 700,
            hovermode: 'closest',
            margin: {
                r: 10,
                t: 10,
                b: 10,
                l: 10,
                pad: 0
            },
            mapbox: {
                center: {
                    lat: 43.7735,
                    lon: -79.5019
                },
                // style: 'light',
                zoom: 12,
                layers: data_layers,
            }
        };


        Plotly.plot('bubbleMap', data, layout, {
                scrollZoom: false,
                mapboxAccessToken: 'pk.eyJ1IjoiY2hyaWRkeXAiLCJhIjoiRy1GV1FoNCJ9.yUPu7qwD_Eqf_gKNzDrrCQ',
            }
        );
    });
});