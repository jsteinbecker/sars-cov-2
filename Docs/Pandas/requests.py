import requests

site= requests.get("https://pubmed.ncbi.nlm.nih.gov/15613317/")
html = site.text

write = open("Docs/Pandas/ncbi.html","w")
write.write(html)
write.close()