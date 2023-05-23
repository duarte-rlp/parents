$(function () {

    Highcharts.chart('xy_scores', {

        chart: {
            height: 510,
            width: 450
        },

        exporting: {
            scale: 10,
            filename: "xy_scores"
        },

        title: {
            text: '(x,y)-Scores'
        },

        xAxis: {
            title: {
                text: 'x-Score',
                y: 10
            },
            height: 300,
            width: 300,
            gridLineWidth: 1,
            tickInterval: 0.5,
            tickLength: 0,
            labels: {
                step: 2
            },
            max: scale,
            min: - scale,
            plotLines: [{
                color: 'black',
                dashStyle: 'dash',
                width: 1,
                value: 0,
                zIndex: 3
            }]
        },

        yAxis: {
            title: {
                text: 'y-Score',
                x: -10
            },
            height: 300,
            width: 300,
            gridLineWidth: 1,
            tickInterval: 0.5,
            labels: {
                step: 2
            },
            max: scale,
            min: - scale,
            plotLines: [{
                color: 'black',
                dashStyle: 'dash',
                width: 1,
                value: 0,
                zIndex: 3
            }]
        },

        plotOptions: {
            bubble: {
                minSize: 5,
                maxSize: 15
            }
        },


        tooltip: {
            headerFormat: '',
            pointFormat: '<b>({point.x}, {point.y})</b><br/># Obs.: {point.z}'
        },

        series: [{
            type:'area',
            name: 'inequality-averse',
            threshold: 0.75,
            lineWidth: 0,
            color:'rgb(188,212,212)',
            fillOpacity: 0.6,
            data:[[-scale,0.75],[-scale,scale],[-0.75,scale],[-0.75,0.75]],
            enableMouseTracking: false
        },{
            type:'area',
            name: 'maximin',
            threshold: 0.75,
            lineWidth: 0,
            color:'rgb(188,212,200)',
            fillOpacity: 0.6,
            data:[[-0.75,0.75],[-0.75,scale],[0.75,scale],[0.75,0.75]],
            enableMouseTracking: false
        },{
            type:'area',
            name: 'altruistic',
            threshold: 0.75,
            lineWidth: 0,
            color:'rgb(188,212,188)',
            fillOpacity: 0.6,
            data:[[0.75,0.75],[0.75,scale],[scale,scale],[scale,0.75]],
            enableMouseTracking: false
        },{
            type:'area',
            name: 'envious',
            threshold: -0.75,
            lineWidth: 0,
            color:'rgb(188,200,212)',
            fillOpacity: 0.6,
            data:[[-scale,-0.75],[-scale,0.75],[-0.75,0.75],[-0.75,-0.75]],
            enableMouseTracking: false
        },{
            type:'area',
            name: 'selfish',
            threshold: -0.75,
            lineWidth: 0,
            color:'rgb(188,200,200)',
            fillOpacity: 0.6,
            data:[[-0.75,-0.75],[-0.75,0.75],[0.75,0.75],[0.75,-0.75]],
            enableMouseTracking: false
        },{
            type:'area',
            name: 'kiss-up',
            threshold: -0.75,
            lineWidth: 0,
            color:'rgb(188,200,188)',
            fillOpacity: 0.6,
            data:[[0.75,-0.75],[0.75,0.75],[scale,0.75],[scale,-0.75]],
            enableMouseTracking: false
        },{
            type:'area',
            name: 'spiteful',
            threshold: -scale,
            lineWidth: 0,
            color:'rgb(188,188,212)',
            fillOpacity: 0.6,
            data:[[-scale,-scale],[-scale,-0.75],[-0.75,-0.75],[-0.75,-scale]],
            enableMouseTracking: false
        },{
            type:'area',
            name: 'kick-down',
            threshold: -scale,
            lineWidth: 0,
            color:'rgb(188,188,200)',
            fillOpacity: 0.6,
            data:[[-0.75,-scale],[-0.75,-0.75],[0.75,-0.75],[0.75,-scale]],
            enableMouseTracking: false
        },{
            type:'area',
            name: 'equality-averse',
            threshold: -scale,
            lineWidth: 0,
            color:'rgb(188,188,188)',
            fillOpacity: 0.6,
            data:[[0.75,-scale],[0.75,-0.75],[scale,-0.75],[scale,-scale]],
            enableMouseTracking: false
        },{
            type: 'bubble',
            data: xy_scores,
            name: '(x,y)-Scores',
            color: 'rgb(66,66,66)',
            fillOpacity: 0.6,
            showInLegend: false
        }],

        legend: {
            width: 400,
            floating: true,
            verticalAlign: 'bottom',
            itemWidth: 130,
            borderWidth: 0,
            itemDistance: 15,
            itemStyle: {
                color: 'rgb(66,66,66)',
                fontWeight: 'normal'
            }
        },

        credits: {
            enabled: false
        }

    }, function (chart) {

        chart.renderer.rect(88,65,24,24,3)
            .attr({
                zIndex: 8
            })
            .css({
                fill: 'rgb(240,240,240)',
                stroke: 'rgb(140,140,140)',
                'stroke-width': 1
            })
            .add();

        chart.renderer.text(bm_freq[0], 100, 82)
            .attr({
                rotation: 0,
                align: 'center',
                zIndex: 10
            })
            .css({
                color: 'rgb(60,60,60)',
                fontSize: '12px'

            })
            .add();

        chart.renderer.rect(340,65,24,24,3)
            .attr({
                zIndex: 8
            })
            .css({
                fill: 'rgb(240,240,240)',
                stroke: 'rgb(140,140,140)',
                'stroke-width': 1
            })
            .add();

        chart.renderer.text(bm_freq[1], 352, 82)
            .attr({
                rotation: 0,
                align: 'center',
                zIndex: 10
            })
            .css({
                color: 'rgb(60,60,60)',
                fontSize: '12px'

            })
            .add();

        chart.renderer.rect(340,317,24,24,3)
            .attr({
                zIndex: 8
            })
            .css({
                fill: 'rgb(240,240,240)',
                stroke: 'rgb(140,140,140)',
                'stroke-width': 1
            })
            .add();

        chart.renderer.text(bm_freq[2], 352, 334)
            .attr({
                rotation: 0,
                align: 'center',
                zIndex: 10
            })
            .css({
                color: 'rgb(60,60,60)',
                fontSize: '12px'

            })
            .add();

        chart.renderer.rect(88,317,24,24,3)
            .attr({
                zIndex: 8
            })
            .css({
                fill: 'rgb(240,240,240)',
                stroke: 'rgb(140,140,140)',
                'stroke-width': 1
            })
            .add();

        chart.renderer.text(bm_freq[3], 100, 334)
            .attr({
                rotation: 0,
                align: 'center',
                zIndex: 10
            })
            .css({
                color: 'rgb(60,60,60)',
                fontSize: '12px'

            })
            .add();
    });

});