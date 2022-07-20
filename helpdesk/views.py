from django.shortcuts import render
from django.http import JsonResponse
from .chat import get_response
import json
from adminPanel.models import UserVisit
from datetime import date


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
    print(text)
    # Todo: check if text is valid
    response = get_response(text)
    message = {'answer': response}
    return JsonResponse(message)
 