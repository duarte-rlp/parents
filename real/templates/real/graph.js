        // Gráfica para Banano y Caña juntas
        Highcharts.chart('graph01', {
            title: {
                text: ''
            },
            xAxis: {
                categories: [2007, 2008, 2009, 2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020],
                align: 'center',
                labels: {
                    rotation: -45
                }
            },
            yAxis: [{
                title: {
                    text: 'Rendimiento',
                    style: {
                        color: 'blue'
                    }
                },
                labels: {
                    format: '{value} ton/ha',
                    style: {
                        color: 'blue'
                    }
                }
            }, {
                title: {
                    text: 'Rendimiento',
                    style: {
                        color: 'green'
                    }
                },
                labels: {
                    format: '{value} ton/ha',
                    style: {
                        color: 'green'
                    }
                },
                opposite: true
            }],
            series: [{
                animation: false,
                yAxis: 1,
                data: [9.09, 9.17, 10.09, 8.81, 10.49, 9.85, 9.8, 10.23, 9.66, 10.62, 10.63, 24.88, 24.85, 24.46],
                lineWidth: 1,
                enableMouseTracking: true,
                marker:{
                    enabled: true
                },
                color: 'blue',
                name: 'Banano',
                dashStyle: 'Solid'
            }, {
                animation: false,
                data: [114.01, 121.82, 122.3, 117.58, 122.44, 100.44, 110.73, 122.14, 119.84, 199.82, 133.15, 141.3, 12.82, 9.31],
                lineWidth: 1,
                enableMouseTracking: true,
                marker:{
                    enabled: true
                },
                color: 'green',
                name: 'Caña de Azúcar',
                dashStyle: 'Solid'
            }],
            legend: {
                enabled: true
            }
        });