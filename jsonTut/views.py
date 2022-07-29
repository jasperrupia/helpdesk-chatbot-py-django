from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from adminPanel.models import User


def jsonView(request):
    jsonDict = {
                "intents": [
                    {
                        "tag": "greeting",
                        "patterns": [
                            "Hi",
                            "Hey",
                            "How are you",
                            "Is anyone there?",
                            "Hello",
                            "Good day"
                        ],
                        "responses": [
                            "Hello, thanks for visiting",
                            "Hi there, what can I do for you?",
                            "Hi there, how can I help?"
                        ]
                    },
                    {
                        "tag": "travel",
                        "patterns": [
                            "How long does traveling to Mzumbe take?"
                        ],
                        "responses": [
                            "It depends, <a href='https://maps.google.com' target='_blank'> google map </a> will help you",
                            "If I were you, I would ask <a href='https://maps.google.com' target='_blank'> google map </a> for that."
                        ]
                    }
                ]
            }
    return JsonResponse(jsonDict, safe=False) 


def jsonView2(request):
    jsonDict = list(User.objects.values()) # include keys
    # jsonDict = list(User.objects.values_list()) # ignore keys
    return JsonResponse(jsonDict, safe=False) 
    
