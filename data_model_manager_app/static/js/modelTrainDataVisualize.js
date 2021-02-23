$(document).ready(function() {
      document.title = "Model Data Result Visualize"
});
$(document).ready(function() {
    // draw charts
    let all_model_chart = $("#all-records-chart");
    $.ajax({
        url: all_model_chart.data("url"),
        success: function (data) {

            let ctx1 = all_model_chart[0].getContext("2d");

            new Chart(ctx1, {
                type: 'bar',
                data: {
                    labels: data.labels,
                    datasets: [{
                        label: 'Precision',
                        backgroundColor: data.color,
                        data: data.data
                    }]
                },
                options: {
                    display: true,
                    legend: {
                        display: false,
                        position: 'left',
                        "labels": {
                            "fontSize": 30,
                            "fontColor": "black"
                        }
                    },
                    scales: {
                        xAxes: [{
                            ticks: {
                                fontSize: 20,
                            }
                        }],
                        yAxes: [{
                            ticks: {
                                fontSize: 20,
                                beginAtZero: true,
                                fontColor: 'black',
                            }
                        }]
                    },
                    title: {
                        display: true,
                        text: 'Model trains on data result',
                        position:'top',
                        padding: 25,
                        fontSize: 40,
                    },
                    tooltips: {
                        enabled: true
                    },
                    plugins: {
                        labels: [
                            {
                                render: 'value',
                                fontSize: 25,
                                fontStyle: 'bold',
                                fontColor: '#000',
                                fontFamily: '"Lucida Console", Monaco, monospace',
                            },
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

