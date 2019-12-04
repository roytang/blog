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

sourcefile = root / "blog.json"
sections = ["post", "comments", "notes", "photos", "reposts", "replies", "links"]
with sourcefile.open() as f:
    stats = json.loads(f.read())
    for s in sections:
        sdata = stats[s]
        years = list(sdata.keys())
        years.sort()

        g = bar.VerticalBar(years)
        options = dict(
            scale_integers=True,
            stack='side',
            width=800,
            height=400,
            graph_title=s,
            show_graph_title=False,
            show_data_labels=False,
            no_css=True,
        )
        g.__dict__.update(options)

        # don't include current year in stats
        years.remove(thisyear)
        data = []
        for year in years:
            data.append(sdata[year])
        g.add_data(dict(data=data, title=""))
        res = g.burn()

        outfile = root / ("%s.svg" % (s))
        with outfile.open('w') as w:
            w.write(res)
