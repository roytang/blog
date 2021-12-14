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

<canvas class="chart" id="chart_posts" width="400" height="200"></canvas>

#### Word Counts

<canvas class="chart" id="chart_wordcount" width="400" height="200"></canvas>

#### By Syndication

<canvas class="chart" id="chart_syndication" width="400" height="200"></canvas>

<small>Only the major syndication sources are included in the chart.</small>

#### Top Commenters

<ol id="top_commenters"></ol>

---

<small>This page requires JavaScript.</small>

<script>

    let backgroundColors = {
        blog: 'rgba(99, 99, 255, 0.5)',
        notes: 'rgba(255, 99, 99, 0.5)',
        links: 'rgba(99, 255, 99, 0.5)',
        comments: 'rgba(180, 180, 99, 0.5)',
    }
    function yearlyGraph(url, element_id, include_sections=false) {
        fetch(url)
            .then(function(response) {
                return response.json();
            })
            .then(function(jsonResponse) {

                let years = jsonResponse["years"];
                let datasets = [];
                for (let section in jsonResponse["sections"]) {
                    var backgroundColor = backgroundColors[section];
                    if (include_sections) {
                        if (section in include_sections) {
                            backgroundColor = include_sections[section];
                        } else {
                            continue;
                        }
                    }
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
                            backgroundColor,
                        ],
                        borderColor: [
                            backgroundColor,
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
    yearlyGraph("/others/stats/syndication/", "chart_syndication", include_sections={
        "facebook": 'rgba(14, 31, 86, 0.5)',
        "twitter": 'rgba(85, 172, 238, 0.5)',
        "instagram": 'rgba(216, 88, 81, 0.5)',
        "reddit": 'rgba(255, 0, 69, 0.5)',
        "mastodon": 'rgba(126, 175, 233, 0.5)',
    });
        fetch("/others/stats/commenter/")
            .then(function(response) {
                return response.json();
            })
            .then(function(jsonResponse) {
                let listRoot = document.querySelector("ol#top_commenters");
                jsonResponse.forEach(function(item, index) {
                    let li = document.createElement("li");
                    anchor = document.createElement("a");
                    anchor.href = "/comments/bycommenter/" + item["uuid"] + "/";
                    anchor.innerText = item["name"];
                    li.appendChild(anchor);
                    let span = document.createElement("span");
                    span.innerText = " (" + item["count"] + ")"
                    li.appendChild(span);
                    listRoot.appendChild(li);
                });
            });


</script>

