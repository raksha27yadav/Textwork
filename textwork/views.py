# I have created this file-"raksha"
from django.http import HttpResponse
from django.shortcuts import render
def index(request):
    return render(request,'index.html')
    #return HttpResponse("<h1>Wlcome Home")
def navigator(request):
    s='''<h2>My Navigation Bar<br></h2>
    <a href="https://www.facebook.com/">Facebook here</a><br>
    <a href="https://www.linkedin.com/mynetwork/">My linkedin Profile </a><br>
    <a href="https://www.youtube.com/watch?v=lcpqpxVowU0&list=PLu0W_9lII9ah7DDtYtflgwMwpT3xmjXY9&index=12">Visit this youtube channel</a>'''
    return HttpResponse(s)
    
def analyze(request):
    djtext=request.POST.get('text','default')
    remove = request.POST.get('remove', 'off')
    fullcaps = request.POST.get('fullcaps', 'off')
    removelines=request.POST.get('removelines','off')
    extraspaceremover = request.POST.get('extraspaceremover', 'off')
    charcount = request.POST.get('charcount', 'off')
    if remove=="on":
        punctuations="""!()-[]{};:'"\,<>./?@#$%*_~"""
        analyzed=""
        for char in djtext:
            if char not in punctuations:
                analyzed=analyzed+char
        params={'purpose':'REMOVED','analyzed_text':analyzed}
        djtext=analyzed
    if(fullcaps=="on"):
        analyzed=""
        for i in djtext:
            analyzed=analyzed+i.upper()
        params = {'purpose': 'HERE SHOWING YOU THE UPPER CASE TEXTS', 'analyzed_text': analyzed}
        djtext=analyzed
    if removelines=="on":
        analyzed=""
        for i in djtext:
            if i !="\n" and i!="\r":
                 analyzed=analyzed+i
        params = {'purpose': 'It is to remove the new lines', 'analyzed_text': analyzed}
        djtext = analyzed
    if extraspaceremover=="on":
        analyzed=""
        for i in range(len(djtext)):
            if (djtext[i]==" ") and (djtext[i+1]==" "):
                pass
            else:
                analyzed=analyzed+djtext[i]
        params = {'purpose': 'It is to remove extra spaces', 'analyzed_text': analyzed}
        djtext = analyzed
    if charcount=="on":
        analyzed=0
        for i in djtext:
            if i.isalpha():
                analyzed+=1
        params = {'purpose': 'It is to count the character', 'analyzed_text': analyzed}
        djtext = analyzed



    if charcount=="off" and remove=="off" and extraspaceremover=="off" and fullcaps=="off" and removelines=="off" :
        return HttpResponse(djtext)
    else:
        return render(request, 'analyze.html', params)


