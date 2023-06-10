# I have creted file
from django.http import HttpResponse
from django.shortcuts import render


# def index(request):
#     print(request.GET.get('text','default'))
#     return HttpResponse("index.html")

def index(request):
    return render(request,"index.html")


def analyze(request):
    dtext= request.POST.get('text','default')
    removepunc= request.POST.get('removepunc','off')
    UpperCase= request.POST.get('UpperCase','off')
    print(removepunc)
    print(dtext)
    if removepunc=="on":
        punctuation='''!()-[]{};:'"\,<>./?@#$%^&*_~'''
        analyzed=""
        for char in dtext:
            if char not in punctuation:
                 analyzed=analyzed+char
            
        params={'purpose':'remove','analyze_text':analyzed}
        return render(request,'analyze.html',params)   
    elif(UpperCase=="on"):
        analyzed=""
        for char in dtext: 
            analyzed=analyzed + char.upper()
        params={'purpose':'change Uppercase ','analyze_text':analyzed}
        return render(request,'analyze.html',params)   
    else:
        return HttpResponse("error")

# def about(request):
#     return HttpResponse("capitalfirst")






