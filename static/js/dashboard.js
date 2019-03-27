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

let dashboard_data = [yorkU_data];


Plotly.d3.csv('static/data/example.CSV', function (err, rows) {
    function unpack(rows, key) {
        return rows.map(function (row) {
            return row[key];
        });
    }

    scl = [
        [0, 'rgb(0, 25, 255)'],
        [0.175, 'rgb(0, 152, 255)'],
        [0.375, 'rgb(44, 255, 150)'],
        [0.5, 'rgb(151, 255, 0)'],
        [0.625, 'rgb(255, 234, 0)'],
        [0.75, 'rgb(255, 111, 0)'],
        [1, 'rgb(255, 0, 0)']];

    let student_data =
        {
            type: 'scattermapbox',
            mode: 'markers',
            lon: unpack(rows, 'long'),
            lat: unpack(rows, 'lat'),
            text: unpack(rows, 'commute_time'),
            name: 'students',
            marker: {
                color: unpack(rows, 'commute_time_min'),
                colorscale: scl,
                cmin: 0,
                cmax: 30,
                reversescale: false,
                size: 8,
                opacity: 0.8,
            }
        };

    dashboard_data.push(student_data);

});


Plotly.d3.csv('static/data/fitness.CSV', function (err, rows) {
    function unpack(rows, key) {
        return rows.map(function (row) {
            return row[key];
        });
    }

    let fit_data =
        {
            type: 'scattermapbox',
            mode: 'markers',
            lon: unpack(rows, 'long'),
            lat: unpack(rows, 'lat'),
            text: unpack(rows, 'name'),
            name: 'fitness',
            marker: {
                color: unpack(rows, 'rating'),
                colorscale: 'Reds',
                cmin: 0,
                cmax: 5,
                reversescale: false,
                size: 10,
                opacity: 0.9,
            }
        };

    dashboard_data.push(fit_data);

});

Plotly.d3.csv('static/data/supermarkets.CSV', function (err, rows) {
    function unpack(rows, key) {
        return rows.map(function (row) {
            return row[key];
        });
    }

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
                colorscale: 'Blues',
                cmin: 0,
                cmax: 5,
                reversescale: false,
                size: 10,
                opacity: 0.9,
            }
        };

    dashboard_data.push(sup_data);

});


Plotly.d3.json('static/data/map.geojson', function (torontojson) {
    Plotly.d3.csv('static/data/restaurants.CSV', function (err, rows) {
        function unpack(rows, key) {
            return rows.map(function (row) {
                return row[key];
            });
        }

        let rest_data =
            {
                type: 'scattermapbox',
                mode: 'markers',
                lon: unpack(rows, 'long'),
                lat: unpack(rows, 'lat'),
                text: unpack(rows, 'name'),
                name: 'restaurants',
                marker: {
                    color: unpack(rows, 'rating'),
                    colorscale: 'Reds',
                    cmin: 0,
                    cmax: 5,
                    reversescale: false,
                    size: 10,
                    opacity: 0.9,
                }
            };

        dashboard_data.push(rest_data);

        let data_layers = [];
        for (let feature_num = 0; feature_num < torontojson["features"].length; feature_num++) {
            let source = torontojson["features"][feature_num];
            let r_value = 255;
            let g_value = 255-source["score"] * 300 ;
            let b_value = 255-source["score"] * 300 ;
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
            showlegend: true,
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


        Plotly.plot('dashboardDiv', dashboard_data, layout, {
            mapboxAccessToken: 'pk.eyJ1IjoiamF5a2Fyb255b3JrIiwiYSI6ImNqa2JjZzNkeTA5ZGkzcG55OXhmcnZxMTIifQ.XotoTIdsT-bYoQpodyW3xg'
        });

    });


});
