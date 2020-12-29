---
title: "Stats :: Gaming"
author: roy
type: page
date: 2020-12-29
aliases:
- /about/stats/gaming
submenu: "stats"
---

### Steam stats

<div id="app">
    <h4>Playtime by Year</h4>
    <table class="data">
        <tr v-for="item in items.playtime_by_years">
            <td>[[ item.year ]]</td>
            <td>[[ item.playtime.toFixed(2) ]] hour(s)</td>
        </tr>
    </table>
    <h4>Most Played Games</h4>
    <table class="data">
        <tr><th colspan="2">Lifetime</th></tr>
        <tr v-for="item in items.top_games">
            <td><a href="[[ item.url ]]">[[ item.name ]]</a></td>
            <td>[[ item.playtime.toFixed(2) ]] hour(s)</td>
        </tr>
        <template v-for="(data, year) in items.top_games_by_year">
            <tr><th colspan="2">[[ year ]]</th></tr>
            <tr v-for="item in data">
                <td><a href="[[ item.url ]]">[[ item.name ]]</a></td>
                <td>[[ item.playtime.toFixed(2) ]] hour(s)</td>
            </tr>
        </template>
    </table>
</div>
<script src="https://cdn.jsdelivr.net/npm/vue@2.6.10/dist/vue.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/vue-resource@1.3.4"></script>
<script type="text/javascript">
    let timeline = new Vue({
        delimiters: ['[[', ']]'],
        el: '#app',
        data: {
            title: "test",
            items: [],
        },
        http: {
            root: '/',
        },
        mounted: function() {
            this.loadEntries();
        },
        methods: {
            loadEntries: function() {
                this.$http.get("/apps/steamhist/report/", {params: {"json": "true"}})
                    .then(response => {
                        this.items = response.data;
                        console.log(this.items);
                    });
            },
        }
    });
</script>

* updated daily; loading the data on this page requires JavaScript
* I don't really play DOTA 2, that's my brothers playing on my account