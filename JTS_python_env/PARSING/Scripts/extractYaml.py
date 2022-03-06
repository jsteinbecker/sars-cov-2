import yaml
from yaml import load, dump, Loader, Dumper
import re


def Authors (text:str) :
   pattern = "(?<=```yaml\nAuthors : )[\w\W]*?(?=\n```)"
   search = re.findall(pattern,text)

   return search



def getNotes (text:str) :
   pattern = "(?<=```yaml\Notes : )[\w\W]*?(?=\n```)"
   search = re.findall (pattern,text)

   return search


fl = open("/Users/joshsteinbecker/jts_project/JTS_python_env/PARSING/Docs/# Pandemics: spend on surveillance, not .md")
data = fl.read()
Authors(data)