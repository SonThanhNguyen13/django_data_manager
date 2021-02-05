$(document).ready(function() {
      document.title = "Models Visualize"
});
$(document).ready(function() {
    // draw charts
    let all_model_chart = $("#all-model-chart");
    $.ajax({
        url: all_model_chart.data("url"),
        success: function (data) {

            let ctx1 = all_model_chart[0].getContext("2d");

            new Chart(ctx1, {
                type: 'pie',
                data: {
                    labels: data.labels,
                    datasets: [{
                        label: 'Owner',
                        backgroundColor: data.color,
                        data: data.data
                    }]
                },
                options: {
                    display: true,
                    legend: {
                        position: 'left',
                        "labels": {
                            "fontSize": 30,
                            "fontColor": "black"
                        }
                    },
                    title: {
                        display: true,
                        text: 'Model by owner',
                        position:'top',
                        fontSize: 40,
                    },
                    tooltips: {
                        enabled: false
                    },
                    plugins: {
                        labels: [
                            {
                                render: 'value',
                                fontSize: 25,
                                position: 'outside',
                                fontStyle: 'bold',
                                fontColor: '#000',
                                fontFamily: '"Lucida Console", Monaco, monospace',
                            },
                            {
                                render: 'percentage',
                                fontSize: 30,
                                fontStyle: 'bold',
                                fontColor: '#FFF',
                                fontFamily: '"Lucida Console", Monaco, monospace',
                                precision: 1,
                            }
                        ]
                    }
                }
            });

        }
    });
});
$(window).on("load",function(){
    $("#loader-wrapper").fadeOut("fast");
});

