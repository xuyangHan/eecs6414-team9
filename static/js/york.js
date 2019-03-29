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
Plotly.d3.json('static/data/map.geojson', function (torontojson) {
    Plotly.d3.json('static/data/york.geojson', function (yorkjson) {

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
                layers: [
                    {
                        sourcetype: 'geojson',
                        source: yorkjson,
                        type: 'fill',
                        color: 'rgba(163,22,19,0.8)'
                    },
                    {
                        sourcetype: 'geojson',
                        source: torontojson,
                        type: 'fill',
                        color: 'rgba(255,255,255,0.3)'
                    },
                ]
            }
        };


        Plotly.plot('dashboardDiv', dashboard_data, layout, {
            mapboxAccessToken: 'pk.eyJ1IjoiamF5a2Fyb255b3JrIiwiYSI6ImNqa2JjZzNkeTA5ZGkzcG55OXhmcnZxMTIifQ.XotoTIdsT-bYoQpodyW3xg'
        });
    });
});