---
title: "Stats :: Food"
submenu: "stats"
---

### Total overall fast food spend and meal counts (2017-onwards)

<table id="overallstats">
<tr>
<th>Franchise</th>
<th>Spend (PHP)</th>
<th>Count</th>
</tr>
</table>

### Spend by year

<canvas class="chart" id="chart_costs" width="400" height="200"></canvas>

### Count by year

<canvas class="chart" id="chart_counts" width="400" height="200"></canvas>

<script src="https://cdnjs.cloudflare.com/ajax/libs/Chart.js/3.6.2/chart.min.js" integrity="sha512-tMabqarPtykgDtdtSqCL3uLVM0gS1ZkUAVhRFu1vSEFgvB73niFQWJuvviDyBGBH22Lcau4rHB5p2K2T0Xvr6Q==" crossorigin="anonymous" referrerpolicy="no-referrer"></script>

### Notes

- This page requires JavaScript.
- "counts" here are separate meals that included food from the specific franchise. This includes meals that I did not pay for, so spend and count may not necessarily be related. Also, some purchases may have lasted over multiple meals, and some purchases may have been for other people.
- The data on the page is static instead of queried directly from my database, since I only need to update it once a year.
- [About this page and more notes](/2023/08/fast-food-consumption/)