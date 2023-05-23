$(function() {

    Highcharts.chart('archetypes', {

        chart: {
            type: 'column',
            height: 470,
            width: 450
        },

        exporting: {
            scale: 10,
            filename: "archetypes"
        },

        title: {
            text: 'Distribution of Archetypes'
        },

        xAxis: {
            categories: archetypes,
            labels: {
                rotation: -90
            }
        },

        yAxis: {
            min: 0,
            title: {
                text: '# Obs.'
            },
            height: 300
        },

        tooltip: {
            pointFormat: '# Obs.: ' + '{point.y}',
            shared: true,
            useHTML: true
        },

        plotOptions: {
            column: {
                pointPadding: 0.05,
                borderWidth: 0,
                colorByPoint: true,
                colors: [
                    'rgba(190,212,212,0.6)',
                    'rgba(190,212,200,0.6)',
                    'rgba(190,212,188,0.6)',
                    'rgba(190,200,212,0.6)',
                    'rgba(190,200,200,0.6)',
                    'rgba(190,200,188,0.6)',
                    'rgba(190,188,212,0.6)',
                    'rgba(190,188,200,0.6)',
                    'rgba(190,188,188,0.6)'
                ]
            }
        },

        series: [{
            name: 'Archetypes',
            data: type_freq
        }],

        legend: {
            enabled: false
        },

        credits: {
            enabled: false
        }

    });

});