// console.log(data);

function createCell(contents, clazz) {
    let newCell = document.createElement("td");
    if (clazz)
        newCell.className = clazz;
    newCell.innerText = contents;
    return newCell;
}

// https://public.tableau.com/app/profile/chris.gerrard/viz/TableauColors/ColorPaletteswithRGBValues
let backgroundColors = [
    'rgba(31, 119, 180, 0.9)',
    'rgba(152, 223, 138, 0.9)',
    'rgba(140, 86, 75, 0.9)',
    'rgba(199, 199, 199, 0.9)',
    'rgba(174, 199, 232, 0.9)',
    'rgba(214, 39, 40, 0.9)',
    'rgba(196, 156, 148, 0.9)',
    'rgba(188, 189, 34, 0.9)',
    'rgba(255, 127, 14, 0.9)',
    'rgba(255, 152, 150, 0.9)',
    'rgba(227, 119, 194, 0.9)',
    'rgba(219, 219, 141, 0.9)',
    'rgba(255, 187, 120, 0.9)',
    'rgba(148, 103, 189, 0.9)',
    'rgba(247, 182, 210, 0.9)',
    'rgba(23, 190, 207, 0.9)',
    'rgba(44, 160, 44, 0.9)',
    'rgba(197, 176, 213, 0.9)',
    'rgba(127, 127, 127, 0.9)',
    'rgba(158, 218, 229, 0.9)',
]

let years = [];
let costdatasets = [];
let countdatasets = [];
let totalcosts = 0.0;
let totalcounts = 0.0;
let container = document.querySelector("table#overallstats");
for (let i = 0; i < data.length; i++) {
    let row = data[i];
    let newRow = document.createElement("tr");
    newRow.appendChild(createCell(row["label"]));
    newRow.appendChild(createCell(row["totalcoststr"], "numeric"));
    newRow.appendChild(createCell(row["totalcount"], "numeric"));
    container.appendChild(newRow);
    totalcosts = totalcosts + row["totalcost"];
    totalcounts = totalcounts + row["totalcount"];
}
let newRow = document.createElement("tr");
newRow.appendChild(createCell("Total"));
newRow.appendChild(createCell(totalcosts.toFixed(2), "numeric"));
newRow.appendChild(createCell(totalcounts, "numeric"));
container.appendChild(newRow);
years.sort();
// console.log(years);
// need a second pass after we have all the years
// to create the chart data
for (let i = 0; i < data.length; i++) {
    let row = data[i];
    for (let year in row["years"]) {
        if (!years.includes(year)) {
            years.push(year);
        }
    }
    let bgcolor = backgroundColors.pop();
    let thisrowData = row["years"];
    let yearlyCosts = [];
    let yearlyCounts = [];
    years.forEach(function (year) {
        if (year in thisrowData) {
            yearlyCosts.push(thisrowData[year]["cost"]);
            yearlyCounts.push(thisrowData[year]["count"]);
        } else {
            yearlyCosts.push(0.0);
            yearlyCounts.push(0.0);
        }
    });
    
    costdatasets.push({
        label: row["label"],
        data: yearlyCosts,
        backgroundColor: [
            bgcolor,
        ],
        borderColor: [
            bgcolor,
        ],
        borderWidth: 1
    });
    countdatasets.push({
        label: row["label"],
        data: yearlyCounts,
        backgroundColor: [
            bgcolor,
        ],
        borderColor: [
            bgcolor,
        ],
        borderWidth: 1
    });
}

function createChart(elementid, datasets) {
    // console.log("Creating chart!")
    const ctx = document.getElementById(elementid).getContext('2d');
    const myChart = new Chart(ctx, {
        type: 'line',
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

createChart("chart_costs", costdatasets);
createChart("chart_counts", countdatasets);