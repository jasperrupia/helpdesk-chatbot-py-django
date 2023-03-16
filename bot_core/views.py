
from django.shortcuts import redirect, render
from django.http import JsonResponse
from .chat import get_response
import json
import os


def index(request):
    return render(request, 'helpdesk.html')



def predict(request):
    text =  json.loads(request.body)
    text = text["message"]
    # print(type(text))
    response = get_response(text)
    # print(type(response)) 
    message = {'answer': response}
    # print(type(message))
    return JsonResponse(message)



def feed_data(request, filename='bot_core/intents.json'):
    with open(filename, mode='r') as jsonFile:
        data = json.load(jsonFile)
    context = {
        'data': data['intents']
    }
    return render(request, 'page_feed_data.html', context)



def crud(request, filename='bot_core/intents.json'):
    with open(filename, mode='r') as jsonFile:
        data = json.load(jsonFile)

    if 'add_intent' in request.POST:
        tag_add = request.POST['tag']
        patterns_add = request.POST['pattern']
        responses_add = request.POST['response']
        intent_add = {
            'tag': tag_add, 
            'patterns': [patterns_add],
            'responses': [responses_add]
        }

        available_tags = []
        for intent in data['intents']:
            available_tags.append(intent['tag'])

        if tag_add in available_tags:
            index = available_tags.index(tag_add)
            data['intents'][index]['patterns'].append(patterns_add)
            data['intents'][index]['responses'].append(responses_add)
        else:
            data['intents'].append(intent_add)

    if 'del_intent' in request.POST:
        tag_del = request.POST['tag']
        available_tags = []
        for intent in data['intents']:
            available_tags.append(intent['tag'])

        if tag_del in available_tags:
            index = available_tags.index(tag_del) 
            del data['intents'][index]

    with open(filename, mode='w') as jsonFile:
        json.dump(data, jsonFile) 
    
    return redirect('feed_data')
    


def train(request):
    os.system('python bot_core/train.py')
    return redirect('feed_data')

