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


// Plotly.d3.json('static/data/map.geojson', function (torontojson) {

    Plotly.d3.csv('static/data/final.CSV', function (err, rows) {
        function unpack(rows, key) {
            return rows.map(function (row) {
                return row[key];
            });
        }

        scl = [
            [0, 'rgb(0, 25, 255)'],
            [0.2, 'rgb(0, 152, 255)'],
            [0.4, 'rgb(44, 255, 150)'],
            [0.5, 'rgb(151, 255, 0)'],
            [0.6, 'rgb(255, 234, 0)'],
            [0.8, 'rgb(255, 111, 0)'],
            [1, 'rgb(255, 0, 0)']];

        let data =
            {
                type: 'scattermapbox',
                mode: 'markers',
                lon: unpack(rows, 'cent_long'),
                lat: unpack(rows, 'cent_lat'),
                text: unpack(rows, 'name'),
                name: 'score',
                marker: {
                    color: unpack(rows, 'scores'),
                    colorscale: scl,
                    cmin: 0,
                    cmax: 1,
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
            }
        };

        let dashboard_data = [yorkU_data, data];
        Plotly.plot('dashboardDiv', dashboard_data, layout, {
            mapboxAccessToken: 'pk.eyJ1IjoiamF5a2Fyb255b3JrIiwiYSI6ImNqa2JjZzNkeTA5ZGkzcG55OXhmcnZxMTIifQ.XotoTIdsT-bYoQpodyW3xg'
        });
    });

// });