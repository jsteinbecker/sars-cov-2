import yaml
from yaml import Loader, Dumper
doc = open("Functions/parse/employees.yml").read()
dy = yaml.load(doc,Loader=Loader)
dy['Brittanie']['trained_for']
