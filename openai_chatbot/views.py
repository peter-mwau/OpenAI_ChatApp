from django.shortcuts import render
from django.http import HttpResponse
import openai

def index(request):
    openai.api_key = "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"
    if request.method == "POST":
        sender = request.POST.get("message-input")
        if sender:
            completion = openai.ChatCompletion.create(
                model='gpt-3.5-turbo',
                messages=[{"role": "user", "content": sender}]
            )
            result = completion['choices'][0]['message']['content']
            print(result)
            context = {
                'result': result
            }
        else:
            context = {}
    else:
        context = {}

    return render(request, 'index.html', context)


