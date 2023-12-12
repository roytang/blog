from pathlib import Path
import frontmatter

sourcepath = "C:\\repos\\blog\\content\\quotes\\lyrics.md"
sourcefile = Path(sourcepath)
outpath = "C:\\repos\\blog\\collections\\quotes\\lyrics"
outdir = Path(outpath)

with sourcefile.open(encoding="UTF-8") as f:
    post = frontmatter.load(f)

    parts = post.content.split("---")

    print(len(parts))

    count = 0
    for part in parts:
        count = count + 1

        fm = frontmatter.Post(part)
        fm["quotes/tags"] = ["sig", "lyrics"]
        newfile = frontmatter.dumps(fm)
        newfilename = "%s.md" % (str(count).rjust(4, '0'))
        if not outdir.exists():
            outdir.mkdir(parents=True)
        outfile = outdir / newfilename
        with outfile.open("w", encoding='utf-8') as w:
            w.write(newfile)                                


