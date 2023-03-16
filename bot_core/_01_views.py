from django.shortcuts import render
from django.http import JsonResponse
from ._01_sample import get_response
import json


def deskbot(request):
    return render(request, 'helpdesk.html')


def answering(request):
    text =  json.loads(request.body)
    print(text)
    text = text["message"]
    # Todo: check if text is valid
    response = get_response(text)
    #print(response)
    message = {'answer': response}
    #message = {'answer': text}
    return JsonResponse(message)
