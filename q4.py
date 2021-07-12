import json


def getJSON(filepath):
    with open(filepath, 'r') as file:
        return json.load(file)


myObj = getJSON("organisms.json")


def get_organism_info(organism, class_cat):
    print(str(myObj[organism][class_cat]))


get_organism_info('Lion', 'class')
get_organism_info('Lion', 'order')
