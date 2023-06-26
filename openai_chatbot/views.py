from django.shortcuts import render
from django.http import HttpResponse
import openai

def index(request):
    openai.api_key = "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"
    if request.method == "POST":
        sender = request.POST.get("message-input")
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"The following is a conversation with an AI assistant:\n\n"
                   f"User: {sender}\n"
                   f"Assistant:",
            temperature=0.7,
            max_tokens=50,
            n=1,
            stop=None
        )
        result = response.choices[0].text.strip()
        context = {
            'result': result
        }
    else:
        context = {}

    return render(request, 'index.html', context)


def chat(request):
    if request.method == "POST":
        sender = request.POST.get("message-input")
        # Perform AI processing and generate the AI response
        # You can use the same OpenAI code here as in the index view
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"The following is a conversation with an AI assistant:\n\n"
                   f"User: {sender}\n"
                   f"Assistant:",
            temperature=0.7,
            max_tokens=50,
            n=1,
            stop=None
        )
        ai_response = response.choices[0].text.strip()
        return HttpResponse(ai_response)
    else:
        return HttpResponse("Invalid request")
