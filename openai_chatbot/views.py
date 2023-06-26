from django.shortcuts import render
from django.http import HttpResponse
import openai

def index(request):
    openai.api_key = "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"
    if request.method == "POST":
        sender = request.POST.get("message-input")
        # sender = "which is the largest ocean"
        messages = []
        messages.append({"role": "user", "content": sender})
        # sender = "Who is elon musk"
        while sender != "":
            user_msg = sender
            messages.append({"role": "user", "content": user_msg})
            completion  = openai.ChatCompletion.create(model='gpt-3.5-turbo',  messages=messages)
            print(completion.choices[0].message.content)
            messages.append({"role": "system", "content": completion.choices[0].message.content})
            sender = completion.choices[0].message.content
        # context = {
        #     "messages": messages
        # }


    return render(request, 'index.html')



# def index(request):
#     if request.method == "POST":
#         # sender = request.POST.get("message-input")

#         # Generate AI response using OpenAI GPT-3.5-turbo API
#         openai.api_key = "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"
#         response = openai.Completion.create(
#             model="gpt-3.5-turbo",
#             messages=[
#                 # {"role": "system", "content": "You are a helpful assistant."},
#                 {"role": "user", "content": "Hello"}
#             ],
#             max_tokens=50,
#             temperature=0.7,
#             n=1,
#             stop=None
#         )
#         ai_response = response.choices[0].message.content.strip()

#         return render(request, 'index.html', {'ai_response': ai_response})
#     else:
#         return render(request, 'index.html')


