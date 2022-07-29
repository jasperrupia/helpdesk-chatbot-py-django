
from django.shortcuts import redirect, render
from django.http import JsonResponse
from .chat import get_response
import json
from adminPanel.models import UserVisit
from datetime import date
from django.contrib.auth.decorators import login_required
import os


def helpdesk(request):
    today = date.today().isoformat()
    try:
        query = UserVisit.objects.get(date_visitad=today) 
        query.count_users = query.count_users + 1
        query.save() 
    except: 
        query = UserVisit(count_users = 1)
        query.save()
        pass
    return render(request, 'helpdesk/helpdesk.html')



def predict(request):
    text =  json.loads(request.body)
    text = text["message"]
    # print(type(text))
    response = get_response(text)
    # print(type(response)) 
    message = {'answer': response}
    # print(type(message))
    return JsonResponse(message)



@login_required(login_url='') 
def feed_data(request, filename='helpdesk/intents.json'):
    with open(filename, mode='r') as jsonFile:
        data = json.load(jsonFile)
    context = {
        'data': data['intents']
    }
    return render(request, 'advanced/page_feed_data.html', context)



@login_required(login_url='') 
def crud(request, filename='helpdesk/intents.json'):
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
        # pattern_del = 'hi88888'
        available_tags = []
        for intent in data['intents']:
            available_tags.append(intent['tag'])

        if tag_del in available_tags:
            index = available_tags.index(tag_del) 
            del data['intents'][index]

            # if pattern_del in data['intents'][index]['patterns']:
            #     index_p = data['intents'][index]['patterns'].index(pattern_del)
            #     del data['intents'][index]['patterns'][index_p]

    # if 'edt_intent' in request.POST:
    #     tag_edt = 'ooooooooo'
    #     pattern_edt = 'ppppppp'

    #     available_tags = []
    #     for intent in data['intents']:
    #         available_tags.append(intent['tag'])

    #     if tag_edt in available_tags:
    #         index = available_tags.index(tag_edt)
    #         data['intents'][index]['tag'] = "ooooooooo"

    #         if pattern_edt in data['intents'][index]['patterns']:
    #             index_p = data['intents'][index]['patterns'].index(pattern_edt)
    #             data['intents'][index]['patterns'][index_p] = "ppppppp1"

    with open(filename, mode='w') as jsonFile:
        json.dump(data, jsonFile) 
    # print(data['intents']) 
    
    return redirect('feed_data')
    


def train(request):
    os.system('python helpdesk/train.py')
    return redirect('feed_data')

