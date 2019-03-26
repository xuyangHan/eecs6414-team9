Plotly.d3.json('static/data/map.geojson', function (torontojson) {
    Plotly.d3.csv('static/data/supermarkets.CSV', function (err, rows) {
        function unpack(rows, key) {
            return rows.map(function (row) {
                return row[key];
            });
        }

        scl = [
            [0, 'rgb(0, 25, 255)'],
            [1, 'rgb(0, 152, 255)'],
            [2, 'rgb(44, 255, 150)'],
            [2.5, 'rgb(151, 255, 0)'],
            [3, 'rgb(255, 234, 0)'],
            [4, 'rgb(255, 111, 0)'],
            [5, 'rgb(255, 0, 0)']];
        let sup_data =
            {
                type: 'scattermapbox',
                mode: 'markers',
                lon: unpack(rows, 'long'),
                lat: unpack(rows, 'lat'),
                text: unpack(rows, 'name'),
                name: 'supermarkets',
                marker: {
                    color: unpack(rows, 'rating'),
                    colorscale: scl,
                    cmin: 0,
                    cmax: 5,
                    reversescale: false,
                    size: 10,
                    opacity: 0.9,
                    colorbar: {
                        thickness: 10,
                        titleside: 'right',
                        outlinecolor: 'rgba(68,68,68,0)',
                    }
                }
            };

        let data = [sup_data];

        let data_layers = [];
        for (let feature_num = 0; feature_num < torontojson["features"].length; feature_num++) {
            let source = torontojson["features"][feature_num];
            let r_value = source["supermarkets"]*100;
            let g_value = source["supermarkets"]*50;
            let b_value = source["supermarkets"]*100;
            // let gb_value = 255 - source["supermarkets"]*40;
            // let gb_value = 15 + feature_num * 4;
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

});