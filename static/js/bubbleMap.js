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

Plotly.d3.csv('static/data/distribution.CSV', function (err, rows) {
    function unpack(rows, key) {
        return rows.map(function (row) {
            return row[key];
        });
    }

    let student_data =
        {
            type: 'scattermapbox',
            mode: 'markers',
            lon: unpack(rows, 'long'),
            lat: unpack(rows, 'lat'),
            text: unpack(rows, 'num'),
            name: 'students',
            marker: {
                size: unpack(rows, 'size'),
                opacity: 0.8,
            }
        };

    let data = [yorkU_data, student_data];

    let layout = {
        autosize: true,
        hovermode: 'closest',
        margin: {
            r: 10,
            t: 10,
            b: 10,
            l: 10,
            pad: 0
        },
        showlegend: false,
        mapbox: {
            bearing: 0,
            center: {
                lat: 43.7735,
                lon: -79.5019
            },
            pitch: 0,
            zoom: 12
        },
    };

    Plotly.setPlotConfig({
        mapboxAccessToken: 'pk.eyJ1IjoiamF5a2Fyb255b3JrIiwiYSI6ImNqa2JjZzNkeTA5ZGkzcG55OXhmcnZxMTIifQ.XotoTIdsT-bYoQpodyW3xg'
    });

    Plotly.plot('bubbleMap', data, layout);
});