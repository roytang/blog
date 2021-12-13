---
title: "Stats :: Live"
author: roy
type: page
aliases:
- /about/stats/live
date: 2021-12-13
submenu: "stats"
---

### Live Stats (Automatically updated)

<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/3.6.2/chart.min.js" integrity="sha512-tMabqarPtykgDtdtSqCL3uLVM0gS1ZkUAVhRFu1vSEFgvB73niFQWJuvviDyBGBH22Lcau4rHB5p2K2T0Xvr6Q==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>

#### Post Counts

<canvas id="chart_posts" width="400" height="200"></canvas>

#### Word Counts

<canvas id="chart_wordcount" width="400" height="200"></canvas>

---

<small>This page requires JavaScript.</small>

<script>

    let backgroundColors = {
        blog: 'rgba(99, 99, 255, 0.5)',
        notes: 'rgba(255, 99, 99, 0.5)',
        links: 'rgba(99, 255, 99, 0.5)',
    }
    function yearlyGraph(url, element_id) {
        fetch(url)
            .then(function(response) {
                return response.json();
            })
            .then(function(jsonResponse) {
                console.log(jsonResponse);

                let years = jsonResponse["years"];
                let datasets = [];
                for (let section in jsonResponse["sections"]) {
                    console.log(section);
                    let section_data = jsonResponse["sections"][section];
                    let data = [];
                    years.forEach(function (year) {
                        if (year in section_data) {
                            data.push(section_data[year]);
                        } else {
                            data.push(0);
                        }
                    });
                    datasets.push({
                        label: section,
                        data: data,
                        backgroundColor: [
                            backgroundColors[section],
                        ],
                        borderColor: [
                            backgroundColors[section],
                        ],
                        borderWidth: 1
                    });
                }

                const ctx = document.getElementById(element_id).getContext('2d');
                const myChart = new Chart(ctx, {
                    type: 'bar',
                    data: {
                        labels: years,
                        datasets: datasets
                    },
                    options: {
                        scales: {
                            y: {
                                beginAtZero: true
                            }
                        }
                    }
                });


            });
    }
    yearlyGraph("/others/stats/bysection/", "chart_posts");
    yearlyGraph("/others/stats/wordcount/", "chart_wordcount");

</script>

