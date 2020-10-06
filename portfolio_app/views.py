from django.shortcuts import render, HttpResponse
from wsgiref.util import FileWrapper
import os
import mimetypes
from .forms import GetFeedback
from django.core.mail import send_mail
# Create your views here.


def download_pdf(request):
    file_path = 'media/Resume.pdf'
    filename = 'Parimal_Mahindrakar_Resume.pdf'
    file = open(file_path, 'rb')
    mime_types, _ = mimetypes.guess_type(file_path)
    response = HttpResponse(file, content_type=mime_types)
    response['Content-Disposition'] = "attachment; filename=%s" % filename
    return response
    
def index(request):
    if request.method == "POST":
        form = GetFeedback(request.POST)
        
        if form.is_valid():
            # print(form.cleaned_data)
            email = form.cleaned_data['email']
            view = form.cleaned_data['view']
            message = f"This is {email}. And he wants to say : \n\n {view}."
            send_mail('From django database of my personal portfolio site.',message, 'parimal', ['parimalm4653@gmail.com'], fail_silently=False)
            form.save()
            form = GetFeedback()
    else:
        form = GetFeedback()
    return render(request,"base.html",{'form':form})