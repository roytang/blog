from pathlib import Path

year_template = '{"date": "%s-01-01 00:00:00"}'
month_template = '{"date": "%s-%s-01 00:00:00"}'

def create_archives():
    # assumes cwd is the blog root
    cwd = Path.cwd() 
    # navigate to ./content/post
    p = cwd / "content" / "post"
    if p.name != "post":
        print("Could not find post folder")
        return
    # immediately under the posts are the year folders
    for year in p.iterdir():
        # outer loop generates the year templates
        if year.is_dir():
            yearcontent = year_template % (year.name)
            target_file = cwd / "content" / "archy" / (year.name + ".md")
            if not target_file.exists():
                with target_file.open("w") as f:
                    f.write(yearcontent)
            for month in year.iterdir():
                # inner loop generates the month templates
                if month.is_dir():
                    monthcontent = month_template % (year.name, month.name)
                    target_file = cwd / "content" / "archm" / (year.name + "-" + month.name + ".md")
                    if not target_file.exists():
                        with target_file.open("w") as f:
                            f.write(monthcontent)


create_archives()