from pathlib import Path
from importers.utils import loadurlmap, contentdir
from datetime import datetime

year_template = '---\ntitle: "Yearly Archives for %s"\ndate: %s-01-01 00:00:00\n---'
month_template = '---\ntitle: "Monthly Archives for %s"\ndate: %s-%s-01 00:00:00\n---'

def create_archives():
    urlmap = loadurlmap()
    for u in urlmap:
        info = urlmap[u]
        if info.get("source_path", "page\\").startswith("page\\"):
            continue
        if 'date' in info:
            d = datetime.strptime(info["date"], "%Y-%m-%d")
            year = d.strftime("%Y")
            target_file = contentdir / "archy" / (year + ".md")
            if not target_file.exists():
                with target_file.open("w") as f:
                    yearcontent = year_template % (year, year)
                    f.write(yearcontent)
            month = d.strftime("%m")
            target_file = contentdir / "archm" / (year + "-" + month + ".md")
            if not target_file.exists():
                with target_file.open("w") as f:
                    monthcontent = month_template % (month + ' ' + year, year, month)
                    f.write(monthcontent)

create_archives()