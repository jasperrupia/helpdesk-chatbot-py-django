from django.shortcuts import render
from django.http import JsonResponse
from .chat import get_response
import json


def helpdesk(request):
    return render(request, 'helpdesk/helpdesk.html')


def predict(request):
    text =  json.loads(request.body)
    text = text["message"]
    print(text)
    # Todo: check if text is valid
    response = get_response(text)
    message = {'answer': response}
    return JsonResponse(message)
