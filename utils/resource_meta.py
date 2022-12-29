from pathlib import Path
import sys, frontmatter

mdfile = Path(sys.argv[1])
parent = mdfile.parent
print(parent)

resources = []
for resource in parent.glob("*.*"):
    print(resource)
    if resource.name == mdfile.name:
        continue
    resources.append({
        "src": resource.name,
        "title": ""
    })

with mdfile.open(encoding='UTF-8') as f:
    try:
        post = frontmatter.load(f)
    except Exception as e:
        print("Error parsing file: " + str(mdfile))
        print(e)

    post['resources'] = resources
    newfile = frontmatter.dumps(post)
    with mdfile.open("w", encoding='UTF-8') as w:
        w.write(newfile)
