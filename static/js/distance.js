
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
                colorbar: {
                    thickness: 10,
                    titleside: 'right',
                    outlinecolor: 'rgba(68,68,68,0)',
                    ticksuffix: ' min',
                }
            }
        };

    let data = [yorkU_data, student_data];

    let layout = {
        autosize: true,
        height:700,
        hovermode: 'closest',
        margin: {
            r: 0,
            t: 0,
            b: 0,
            l: 0,
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

    Plotly.plot('distanceMap', data, layout);
});