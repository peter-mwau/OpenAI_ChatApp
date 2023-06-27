from django.shortcuts import render
from django.http import HttpResponse
import openai
from gradio_client import Client

def index(request):
    openai.api_key = "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"
    if request.method == "POST":
        # sender = request.POST.get("message-input")

        sender = "what is the fifa 23 in 5 words"
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



# def index(request):
#     if request.method == "POST":
#         client = Client("https://a488d0b594b5d1d300.gradio.live/")
#         result = client.predict(
#             "what is javascript",
#             api_name="/predict"
#         )
#         print(result)  # Check the value of result

#         if result is not None:
#             return render(request, 'index.html', {'ai_response': result})
#         else:
#             error_message = "An error occurred during prediction."
#             return render(request, 'index.html', {'error_message': error_message})

#     return render(request, 'index.html')



