import csv
from pathlib import Path

SRCFILE = Path("/mnt/doom/files/Dropbox/games.csv")
TEMPLATE = """- description: 'Placeholder review'
  media: games
  platforms:
  - %s
  title: '%s (%s)'
  date: %s"""

with SRCFILE.open() as f:
    read = csv.reader(f)
    for row in read:
        out = TEMPLATE % (row[2], row[0], row[2], row[1])
        print(out)