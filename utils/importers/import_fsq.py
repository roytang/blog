import json
from pathlib import Path
import datetime

out_items = []
with Path("d:\\temp\\foursquare.json").open(encoding="UTF-8") as f:
    data = json.loads(f.read())
    for item in data[0]["response"]["checkins"]["items"]:
        epoch_time = item["createdAt"]
        d = datetime.datetime.fromtimestamp(epoch_time).strftime('%Y-%m-%d %H:%M:%S')
        print(d)
        out_items.append({
            "lat": item["venue"]["location"]["lat"],
            "lng": item["venue"]["location"]["lng"],
            "label": item["venue"]["name"] + " " + item["venue"]["location"].get("address", ""),
            "date": d,
            "shout": item.get("shout", ""),
            "source": "foursquare"
        })

# print(json.dumps(out_items, indent=2))

# count repeats I guess?

label_map = {}
for item in out_items:
    label = item["label"]
    if label not in label_map:
        label_map[label] = [item]
    else:
        label_map[label].append(item)

keys = []
for key in label_map:
    print(key, len(label_map[key]))
    keys.append(key)

keys.sort(key=lambda x: len(label_map[x]))

for key in keys:
    print(key, len(label_map[key]))


# with Path("out.json").open("w", encoding="UTF-8") as f:
#     f.write(json.dumps(label_map, indent=2))

