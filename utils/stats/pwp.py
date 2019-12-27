# generate that stats json file for all site/blog items

from pathlib import Path
import os
import json
from datetime import datetime
from bs4 import BeautifulSoup

filename = "d:\\temp\\pwp.html"

totals = { "win": 0, "lose": 0, "draw": 0}
totals_by_format = {}
totals_by_year = {}

events = []
with Path(filename).open(encoding="UTF-8") as f:
    soup = BeautifulSoup(f.read(), "html.parser")
    rows = soup.find_all("div", { "class": "HistoryPanelRow"})
    for row in rows:
        event = {}

        achievements = row.find_all("div", { "class": "Achievement"})
        if len(achievements) > 0:
            # ignore achievement rows
            continue
        
        container = row.find_all("div", { "class": "Date"})[0]
        event["date"] = container.text 
        date = datetime.strptime(container.text, "%Y-%m-%d")
        year = date.strftime("%Y")
        container = row.find_all("div", { "class": "Description"})[0]
        event["description"] = container.text
        container = row.find_all("div", { "class": "Location"})[0]
        event["location"] = container.text
        container = row.find_all("div", { "class": "LifetimePoints"})[0]
        event["lifetimepoints"] = container.text
        container = row.find_all("div", { "class": "ProPoints"})[0]
        event["propoints"] = container.text

        container = row.find_all("div", { "class": "EventType"})[0]
        event["type"] = container.text.replace("Event Type: ", "")
        container = row.find_all("div", { "class": "EventMultiplier"})[0]
        event["multiplier"] = container.text.replace("Event Multiplier: ", "")
        container = row.find_all("div", { "class": "EventPlayers"})[0]
        event["players"] = container.text.replace("Players: ", "")
        container = row.find_all("div", { "class": "EventParticipationPoints"})[0]
        event["participationpoints"] = container.text.replace("Participation Points: ", "")
        container = row.find_all("div", { "class": "EventFormat"})[0]
        event["format"] = container.text.replace("Format: ", "")
        container = row.find_all("div", { "class": "EventLocation"})[0]
        event["location2"] = container.text.replace("Location: ", "")
        container = row.find_all("div", { "class": "EventPlace"})[0]
        event["place"] = container.text.replace("Place: ", "")
        container = row.find_all("div", { "class": "EventSanctionNumber"})[0]
        event["sanctioning_number"] = container.text.replace("Sanctioning Number: ", "")

        matches = []
        for match_row in row.find_all("tr", { "class": "MatchHistoryRow"}):
            match = {}
            match["place"] = match_row.find_all("td", { "class": "MatchPlace"})[0].text
            match["result"] = match_row.find_all("td", { "class": "MatchResult"})[0].text
            match["points"] = match_row.find_all("td", { "class": "MatchPoints"})[0].text
            match["opponent"] = match_row.find_all("td", { "class": "MatchOpponent"})[0].text.strip()
            matches.append(match)

            lresult = match["result"].lower()
            totals[lresult] = totals.get(lresult, 0) + 1

            if event["format"] not in totals_by_format:
                totals_by_format[event["format"]] = {}
            totals_by_format[event["format"]][lresult] = totals_by_format[event["format"]].get(lresult, 0) + 1

            if year not in totals_by_year:
                totals_by_year[year] = {}
            totals_by_year[year][lresult] = totals_by_year[year].get(lresult, 0) + 1

        event["matches"] = matches

        events.append(event)

stats = {}
# stats["events"] = events
stats["totals"] = totals
stats["totals_by_format"] = totals_by_format
stats["totals_by_year"] = totals_by_year

headers = """
| | Win | % | Loss | % | Draw | % | Total |
| --- | --- | --- | --- | --- | --- | --- | --- |"""
row_template = "\n| %s | %s | %.2f | %s | %.2f |%s | %.2f | %s |"\

outfile = Path.cwd() / "utils" / "stats" / "mtg.md"
with outfile.open("w", encoding="UTF-8") as w:
    def format_row(label, row):
        win = row.get("win", 0)
        loss = row.get("loss", 0)
        draw = row.get("draw", 0)
        total = win + loss + draw
        w.write(row_template % (label, win, win*100/total, loss, loss*100/total, draw, draw*100/total, total))

    row = totals

    w.write(headers)
    format_row("Total", totals)
    w.write("\n| *By Format* |")
    for key in totals_by_format:
        format_row(key, totals_by_format[key])
    w.write("\n| *By Year* |")
    for key in totals_by_year:
        format_row(key, totals_by_year[key])

# print(json.dumps(stats, indent=2))