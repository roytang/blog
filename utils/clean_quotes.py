# Reference: https://elbauldelprogramador.com/en/how-to-parse-frontmatter-with-python/
from pathlib import Path
import html

inpath = Path("D:\\backups\\sorted\\projects\\quotes\\quotes_source_old.txt")
outfile = Path("out.txt").open("w", encoding="UTF-8")

get_next_line = False
lines = []
with inpath.open(encoding="UTF-8") as f:
    for line in f.readlines():
        if line.startswith("#"):
            get_next_line = True
        else:
            if get_next_line:
                get_next_line = False
                if line not in lines:
                    lines.append(line)
                else:
                    outfile.write(line + "\n")

