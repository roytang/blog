---
title: "Stats :: Live"
author: roy
type: page
aliases:
- /about/stats/live
date: 2021-12-13
submenu: "stats"
---

### Live Stats (Up-to-date)

#### Totals

<ul id="totals">
</ul>

<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/3.6.2/chart.min.js" integrity="sha512-tMabqarPtykgDtdtSqCL3uLVM0gS1ZkUAVhRFu1vSEFgvB73niFQWJuvviDyBGBH22Lcau4rHB5p2K2T0Xvr6Q==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>

#### Post Counts

<canvas class="chart" id="chart_posts" width="400" height="200"></canvas>

#### Word Counts

<canvas class="chart" id="chart_wordcount" width="400" height="200"></canvas>

#### By Syndication

<canvas class="chart" id="chart_syndication" width="400" height="200"></canvas>

<small>Only the major syndication sources are included in the chart.</small>

#### Most Commented Posts

<ol id="mostCommented">
</ol>

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
    let labels = {
        blog: "Blog Posts",
        links: "Shared Links",
        notes: "Notes",
        wordcount: "Word Count",
        comments: "Comments"
    }
    function yearlyGraph(jsonResponse, element_id, include_sections=false) {
        let years = jsonResponse["years"];
        let datasets = [];
        for (let section in jsonResponse["sections"]) {
            if (!Object.keys(backgroundColors).includes(section)) {
                const [r, g, b] = crypto.getRandomValues(new Uint8Array(3));
                var randomcolor = `rgba(${r}, ${g}, ${b}, 0.5)`;
                backgroundColors[section] = randomcolor;
            }
        }
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
    }

    function getAllData() {
        fetch("../../../others/stats.json")
            .then(function(response) {
                return response.json();
            })
            .then(function(jsonResponse) {
                // totals
                var listEl = document.querySelector("ul#totals");
                for (let section in jsonResponse["totals"]["sections"]) {
                    if (!Object.keys(labels).includes(section)) {
                        labels[section] = section;
                    }
                    let listItem = document.createElement("li");
                    listItem.innerText = labels[section] + ": " + jsonResponse["totals"]["sections"][section];
                    listEl.appendChild(listItem);
                }
                console.log(labels);
                var listEl = document.querySelector("ol#mostCommented");
                jsonResponse["mostcommented"].forEach(function(post) {
                    console.log(post);
                    let listItem = document.createElement("li");
                    let anchor = document.createElement("a");
                    anchor["href"] = post["permalink"]
                    anchor.innerText = post["title"] + " (" + post["count"] + " comments)"
                    listItem.appendChild(anchor);
                    listEl.appendChild(listItem);
                });
                let listRoot = document.querySelector("ol#top_commenters");
                jsonResponse["commenter"].forEach(function(item, index) {
                    let li = document.createElement("li");
                    let anchor = document.createElement("a");
                    anchor.href = item["url"];
                    anchor.innerText = item["name"];
                    li.appendChild(anchor);
                    let span = document.createElement("span");
                    span.innerText = " :: ";
                    li.appendChild(span);
                    let anchor2 = document.createElement("a");
                    anchor2.href = "/comments/bycommenter/" + item["uuid"] + "/";
                    anchor2.innerText = "(" + item["count"] + " comments)";
                    li.appendChild(anchor2);
                    listRoot.appendChild(li);
                });
                yearlyGraph(jsonResponse["section"], "chart_posts");
                yearlyGraph(jsonResponse["wordcount"], "chart_wordcount");
                yearlyGraph(jsonResponse["syndication"], "chart_syndication", include_sections={
                    "facebook": 'rgba(14, 31, 86, 0.5)',
                    "twitter": 'rgba(85, 172, 238, 0.5)',
                    "instagram": 'rgba(216, 88, 81, 0.5)',
                    "reddit": 'rgba(255, 0, 69, 0.5)',
                    "mastodon": 'rgba(126, 175, 233, 0.5)',
                });
            });
    }
    getAllData();

</script>

