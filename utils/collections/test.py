from pathlib import Path
import frontmatter

sourcepath = "C:\\repos\\blog\\content\\quotes\\sig2.md"
sourcefile = Path(sourcepath)
outpath = "C:\\repos\\blog\\collections\\quotes"
outdir = Path(outpath)

with sourcefile.open(encoding="UTF-8") as f:
    post = frontmatter.load(f)

    parts = post.content.split("---")

    print(len(parts))

    count = 0
    for part in parts:
        count = count + 1

        fm = frontmatter.Post(part)
        fm["quotes/tags"] = ["sig"]
        newfile = frontmatter.dumps(fm)
        newfilename = "%s.md" % (str(count).rjust(4, '0'))
        outfile = outdir / newfilename
        with outfile.open("w", encoding='utf-8') as w:
            w.write(newfile)                                


