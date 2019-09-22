from pathlib import Path
import re
import random
import frontmatter
from datetime import datetime, timedelta

START_OF_LINE = "AVeryLongMarkerForStartOfLine"
END_OF_LINE = "AVeryLongMarkerForEndOfLine"

class MarkovWordChain:
    def __init__(self):
      self.map = {}
    def add(self, word, nextWord):
      #print "Adding %s -> %s" % (word, nextWord)
      if not word in self.map:
        self.map[word] = { "totalCount" : 0, "nextWords" : {} }
      wordChain = self.map[word]
      wordChain["totalCount"] = wordChain["totalCount"] + 1
      nextWords = wordChain["nextWords"]
      if not nextWord in nextWords:
        nextWords[nextWord] = 0
      nextWords[nextWord] = nextWords[nextWord] + 1
      wordChain["nextWords"] = nextWords
      self.map[word] = wordChain
    def to_string(self):
      retval = ""
      for word in self.map:
        retval = retval + str(word) + " : " + str(self.map[word]["totalCount"]) + "\n"
        retval = retval + "Next words:\n"
        for nextWord in self.map[word]["nextWords"]:
          retval = retval + nextWord + "\n"
      return retval
    def sentence(self):
      retval = ""
      word = START_OF_LINE
      while word != END_OF_LINE:
        if word not in (START_OF_LINE, END_OF_LINE):
          retval = retval + word + " "
          #print "Adding %s" % word
        # get the next word
        totalCount = self.map[word]["totalCount"]
        nextWords = self.map[word]["nextWords"]
        roll = random.randint(0, totalCount-1)
        currCount = 0
        breaker = 0
        #print "Roll = %s" % roll 
        for nextWord in nextWords:
          #print "currCount = %s" % currCount 
          if currCount >= roll:
            word = nextWord
            breaker = 1
            break
          currCount = currCount + nextWords[nextWord]
        if breaker == 0:
          word = END_OF_LINE
      return retval

markov = MarkovWordChain()

cwd = Path.cwd() 
# navigate to ./content/posts
p = cwd / "content" / "post"
for mdfile in p.glob("**/*.md"):
    modtime = datetime.fromtimestamp(mdfile.stat().st_mtime)
    n = datetime.now()
    daysdelta = (n - modtime).days
    # if not all and daysdelta > 100:
    #     # dont index files older than 100 days
    #     continue
    with mdfile.open(encoding='utf-8') as f:
        post = frontmatter.load(f)
        post_text = str(post)
        for line in post_text.splitlines():
            if line.startswith("![]"):
                continue # ignore images
            prevToken = START_OF_LINE
            for token in line.split():
                markov.add(prevToken, token)
                prevToken = token
            markov.add(prevToken, END_OF_LINE)

import random

content = ["This is the demo output for a Markov chain Python script, based on posts from this site. [More info](/2019/08/python-markov-chains/)"]
for i in range(0, random.randint(10, 20)):
    content.append(markov.sentence())

fm = frontmatter.Post("\n\r".join(content))
fm['title'] = 'Markov Chain Demo'
fm['date'] = datetime.now() - timedelta(days=399) # subtract a random number of days so it doesnt appear in Onthisday and on the front page
fm['url'] = '/demos/markov'
fm['hidden'] = True

# create the year folder if it doesnt exist

newfile = frontmatter.dumps(fm)
outfile = cwd / "content" / "page" / "markov.md"
with outfile.open("w", encoding='utf-8') as w:
    w.write(newfile)        