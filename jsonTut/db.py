import json
from django.shortcuts import render
from django.http import JsonResponse


def showDB2(filename='db.json'):
    with open(filename, mode='r') as jsonFile:
        data = json.load(jsonFile)
        print(data)
        print(data['intents'])
# showDB2()


tag_add = 'my-tag5'
patterns_add = 'hi88'
responses_add = 'hello there88'

intent_add = {
    'tag': tag_add, 
    'patterns': [patterns_add],
    'responses': [responses_add]
}

def writeDB(filename='db.json'):
    with open(filename, mode='r') as jsonFile:
        data = json.load(jsonFile)
        # print(data)

    available_tags = []
    for intent in data['intents']:
        # print(intent)
        available_tags.append(intent['tag'])
    # print(available_tags)

    if tag_add in available_tags:
        index = available_tags.index(tag_add)
        # print(index)
        data['intents'][index]['patterns'].append(patterns_add)
        data['intents'][index]['responses'].append(responses_add)
    else:
        data['intents'].append(intent_add)
    
    with open(filename, mode='w') as jsonFile:
        json.dump(data, jsonFile)

# writeDB()







tag_del = 'my-tag5'
pattern_del = 'hi88888'

def deleteDB(filename='db.json'):
    with open(filename, mode='r') as jsonFile:
        data = json.load(jsonFile)

    available_tags = []
    for intent in data['intents']:
        available_tags.append(intent['tag'])

    if tag_del in available_tags:
        index = available_tags.index(tag_del)
        # print(data['intents'][index])
        del data['intents'][index]

        # print(data['intents'][index]['patterns'])
        if pattern_del in data['intents'][index]['patterns']:
            index_p = data['intents'][index]['patterns'].index(pattern_del)
            # print(index_p)
            # print(data['intents'][index]['patterns'][index_p])
            del data['intents'][index]['patterns'][index_p]

    with open(filename, mode='w') as jsonFile:
        json.dump(data, jsonFile)

# deleteDB()





tag_edt = 'ooooooooo'
pattern_edt = 'ppppppp'

def editDB(filename='db.json'):
    with open(filename, mode='r') as jsonFile:
        data = json.load(jsonFile)

    available_tags = []
    for intent in data['intents']:
        available_tags.append(intent['tag'])

    if tag_edt in available_tags:
        index = available_tags.index(tag_edt)
        # print(data['intents'][index])
        data['intents'][index]['tag'] = "ooooooooo"
        # print(data['intents'][index])

        if pattern_edt in data['intents'][index]['patterns']:
            index_p = data['intents'][index]['patterns'].index(pattern_edt)
            data['intents'][index]['patterns'][index_p] = "ppppppp1"

    with open(filename, mode='w') as jsonFile:
        json.dump(data, jsonFile)

# editDB()

