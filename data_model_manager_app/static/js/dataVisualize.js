$(document).ready(function() {
    // draw charts
    let all_data_chart = $("#all-data-chart");
    $.ajax({
        url: all_data_chart.data("url"),
        success: function (data) {

            let ctx1 = all_data_chart[0].getContext("2d");

            new Chart(ctx1, {
                type: 'pie',
                data: {
                    labels: data.labels,
                    datasets: [{
                        label: 'Datasets',
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
                        text: 'Datasets by category',
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
    let analyzed_data_chart = $("#analyzed-data-chart");
    $.ajax({
        url: analyzed_data_chart.data("url"),
        success: function (data) {

            let ctx2 = analyzed_data_chart[0].getContext("2d");

            new Chart(ctx2, {
                type: 'doughnut',
                data: {
                    labels: data.labels,
                    datasets: [{
                        label: 'Datasets',
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
                        text: 'Datasets Analyzed',
                        position:'top',
                        fontSize: 40,
                    },
                    tooltips: {
                        enabled: false
                    },
                    plugins: {
                        labels: {
                            render: 'percentage',
                            fontSize: 25,
                            fontStyle: 'bold',
                            fontColor: '#FFF',
                            fontFamily: '"Lucida Console", Monaco, monospace',
                            precision: 1,
                        }
                    }
                }
            });

        }
    });
});
