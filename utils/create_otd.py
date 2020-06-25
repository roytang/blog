from pathlib import Path
from importers.utils import loadurlmap, contentdir
from datetime import datetime, timedelta, date

template = '---\ntitle: "On This Day for %s"\ndate: %s\n---'


# def create_archives():
#     urlmap = loadurlmap()
#     for u in urlmap:
#         info = urlmap[u]
#         if info.get("source_path", "page\\").startswith("page\\"):
#             continue
#         if 'date' in info:
#             d = datetime.strptime(info["date"], "%Y-%m-%d")
#             year = d.strftime("%Y")
#             target_file = contentdir / "archy" / (year + ".md")
#             if not target_file.exists():
#                 with target_file.open("w") as f:
#                     yearcontent = year_template % (year, year)
#                     f.write(yearcontent)
#             month = d.strftime("%m")
#             target_file = contentdir / "archm" / (year + "-" + month + ".md")
#             if not target_file.exists():
#                 with target_file.open("w") as f:
#                     monthcontent = month_template % (month + ' ' + year, year, month)
#                     f.write(monthcontent)

# create_archives()

start_date = date(1980, 1, 1)
end_date = date(1981, 1, 1)

for n in range(int((end_date - start_date).days)):
    d = start_date + timedelta(n)
    # print(d.strftime("%Y-%m-%d"))
    day = d.strftime("%m-%d")
    # print(content)
    target_file = contentdir / "otd" / (day + ".md")
    if not target_file.exists():
        with target_file.open("w") as f:
            content = template % (day, d.strftime("%Y-%m-%d"))
            f.write(content)
