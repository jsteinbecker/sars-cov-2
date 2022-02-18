import yaml
from yaml import Loader, Dumper
doc = open("Functions/parse/pl.yml").read()

y = yaml.load(doc,Loader=Loader)
y['']
y['product'][1]