---
date: 2019-08-27
syndicated:
- type: twitter
  url: https://twitter.com/roytang/statuses/1166140339972952064/
tags:
- software development
- devnotes
- python
title: 'Devnotes: Python Pathlib'
---

Ever since I started learning Python back in 2008ish, I've been using it as my primary scripting language for various tasks such as processing log files, organizing my own file system, processing stuff on this blog, and so on. A lot of it is basically moving files around. In the days of Python 2, that involved a lot of imports of different libraries like `os`, `shutil` and `glob`. It can become a bit messy with so many imports, and I often can't remember which import I need for a particular case and end up having to search for the documentation (or stackoverflow, let's not kid ourselves here).

With Python 3, a new cleaner option is available to replace all of the above libraries: [Pathlib](https://docs.python.org/3/library/pathlib.html), introduced in Python 3.4, provides an object-oriented way of doing file operations, replacing many of the most common uses I had for the libraries above. Some sample usage:

```python
from pathlib import path

# Declaring a path object is just passing the path string
p = Path("/home/roytang/stuff")

# Other paths can be derived using the / operator
subdir = p / "favorites"

# p.glob replaces stuff like os.walk and glob.glob
for mdfile in p.glob("**/*.md"):
    print(str(mdfile))

    # path objects have properties for individual path elements
    filename = mdfile.name
    stem = mdfile.stem # filename without extension

    # path.exists() replaces os.exists()
    newdir = subdir / stem 
    if not newdir.exists():
        # path.mkdir replaces os.makedirs
        newdir.mkdir(parents=True)

    newfile = newdir / newfile # path objects can be either files or dirs
    # for file copying, you still need shutil!
    import shutil
    shutil.copy(str(mdfile), str(newfile))
```

For me it's much cleaner to use than the old methods and require less imports (most of the time). I eventually hope to migrate all my older scripts to use Pathlib (the same way I migrated them away from Python 2 a while back), and moving forward I plan to use it primarily for filesystem operations.