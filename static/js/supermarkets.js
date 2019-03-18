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

    let layout = {
        autosize: true,
        height:700,
        hovermode: 'closest',
        margin: {
            r: 20,
            t: 40,
            b: 20,
            l: 20,
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

    Plotly.plot('supermarketDiv', data, layout);
});