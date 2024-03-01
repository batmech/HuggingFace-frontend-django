from django.shortcuts import render
from transformers import pipeline

# Create your views here.
def home(request):
    if request.method == 'POST':
        input_text = request.POST.get('input_text')
        print(input_text)
    return render(request, 'index.html')