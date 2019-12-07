#!/usr/bin/env python3

from jinja2 import Template, Environment, FileSystemLoader
import json

def loadPropertiesJson(path):
    with open(path) as file:
        return json.load(file)

def loadTemplate(directory, file):
    fileLoader = FileSystemLoader(directory)
    env = Environment(loader = fileLoader)
    return env.get_template(file)

def writeFile(path, obj):
    with open(path, 'w') as file: 
        file.write(obj)

data = loadPropertiesJson('properties.json')
template = loadTemplate('templates', 'template.json')

output = template.render(name = data['name'], version = data['version'])

print(output)

writeFile('files/arquivo1.json', output)