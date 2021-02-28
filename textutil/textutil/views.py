from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render (request,'index.html')


def new(request):
    djtext=request.GET.get('text','default')
    remove=request.GET.get('remove','off')
    analyzed=""
    punc='''!()-{}[];:.,'"\/<>?@#$%^&*~'''
    if remove=="off":
        return HttpResponse(djtext)
    else:
        for char in djtext:
            if char not in punc:
                analyzed=analyzed+char
    params={'purpose':'removed punc','analyzed_text':analyzed}
    return render(request,'remove.html',params)
