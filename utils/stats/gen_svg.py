# Generate svg graphs using the json stats
from pathlib import Path
from svg.charts.plot import Plot
from svg.charts import bar
from svg.charts import time_series
from svg.charts import pie
from svg.charts import schedule
from svg.charts import line
from datetime import datetime
import json

thisyear = datetime.now().strftime("%Y")
print(thisyear)
root = Path(__file__).parent.absolute()

def gen_chart(xaxis, yaxis, filename):
    g = bar.VerticalBar(xaxis)
    options = dict(
        scale_integers=True,
        stack='side',
        width=800,
        height=400,
        graph_title=filename,
        show_graph_title=False,
        show_data_labels=False,
        no_css=True,
    )
    g.__dict__.update(options)

    g.add_data(dict(data=yaxis, title=""))
    res = g.burn()

    # let's do this manually for now:
    res = res.replace('width="800" height="400" viewBox', 'viewBox')

    outfile = root / ("%s.svg" % (filename))
    with outfile.open('w') as w:
        w.write(res)


def gen_svg_blog():
    sourcefile = root / "blog.json"
    sections = ["post", "comments", "notes", "photos", "reposts", "replies", "links"]
    with sourcefile.open() as f:
        stats = json.loads(f.read())
        for s in sections:
            sdata = stats[s]
            years = list(sdata.keys())
            years.sort()

            # don't include current year in stats
            years.remove(thisyear)
            data = []
            for year in years:
                data.append(sdata[year])
            gen_chart(years, data, s)

import csv
def gen_svg_music(infile):
    with Path(infile).open(encoding='UTF-8') as f:
        read = csv.reader(f)
        counts_by_year = {}
        artists_by_year = { "ALL": {} }
        tracks_by_year = { "ALL": {} }
        years = []
        for row in read:
            date = datetime.strptime(row[3], '%d %b %Y %H:%M')
            year = date.strftime("%Y")
            counts_by_year[year] = counts_by_year.get(year, 0) + 1
            if year not in years:
                years.append(year)
            artist = row[0]
            artists_by_year[year] = artists_by_year.get(year, {})
            artists_by_year[year][artist] = artists_by_year[year].get(artist, 0) + 1
            artists_by_year["ALL"][artist] = artists_by_year["ALL"].get(artist, 0) + 1
            track = row[2]
            tracks_by_year[year] = tracks_by_year.get(year, {})
            tracks_by_year[year][track] = tracks_by_year[year].get(track, 0) + 1
            tracks_by_year["ALL"][track] = tracks_by_year["ALL"].get(track, 0) + 1
        years.sort()
        data = [counts_by_year[year] for year in years]
        gen_chart(years, data, "lastfm")

        def print_top(year, label, items_by_year):

            print("\n##### %s\n" % (label))
            items = []
            for item in items_by_year[year]:
                items.append({"name": item, "count": items_by_year[year][item]})
            items.sort(key=lambda obj: obj["count"], reverse=True)
            idx = 0
            for item in items:
                print("- %s (%s)" % (item["name"], item["count"]))
                idx = idx + 1
                if idx >= 5:
                    break

        years.insert(0, "ALL")
        for year in years:
            print("{{< grid3 >}}")
            print("\n##### " + year)
            print("{{< grid_item >}}")
            print_top(year, "Artists", artists_by_year)
            print("{{</ grid_item >}}")
            print("{{< grid_item >}}")
            print_top(year, "Tracks", tracks_by_year)
            print("{{</ grid_item >}}")
            print("{{</ grid3 >}}")

        print(len(artists_by_year["ALL"]))
      

# export file is from https://benjaminbenben.com/lastfm-to-csv/
# infile = "C:\\Users\\USER\\Dropbox\\backups\\lastfm-roytang-20191206.csv"
# gen_svg_music(infile)
gen_svg_blog()