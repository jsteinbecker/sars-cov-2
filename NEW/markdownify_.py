import markdownify
import requests

site = requests.get("https://www.nature.com/articles/d41586-018-05373-w").text
site

md = markdownify.markdownify(site)
savefile = open("/Users/joshsteinbecker/jts_project/NEW/MDex.md" , "w")
savefile.write(md)
savefile.close()
