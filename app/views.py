from django.shortcuts import render

# Create your views here.
from app.models import *
from app.forms import *
from django.http import HttpResponse

def insert_topic(request):
    TF=TopicForm()
    d={'TF':TF}

    if request.method=='POST':
        TFD=TopicForm(request.POST)

        if TFD.is_valid():
            topic_name=TFD.cleaned_data['topic_name']
        
            TO=Topic.objects.get_or_create(topic_name=topic_name)[0]
            TO.save()
            TQS=Topic.objects.all()
            d1={'TQS':TQS}
            return render(request,'display_topic.html',d1)

    return render(request,'insert_topic.html',d)


def insert_webpage(request):
    WF=WebpageForm()
    d={'WF':WF}

    if request.method=='POST':
        WFD=WebpageForm(request.POST)

        if WFD.is_valid():
            topic_name=WFD.cleaned_data['topic_name']
            TO=Topic.objects.get_or_create(topic_name=topic_name)[0]
            TO.save()
            name=WFD.cleaned_data['name']
            url=WFD.cleaned_data['url']
            email=WFD.cleaned_data['email']
            WO=Webpage.objects.get_or_create(topic_name=TO,name=name,url=url,email=email)[0]
            WO.save()
            WQS=Webpage.objects.all()
            d1={'WQS':WQS}

            return render(request,'display_webpage.html',d1)
    return render(request,'insert_webpage.html',d)

def insert_access(request):
    AF=AccessRecordForm()
    d={'AF':AF}

    if request.method=='POST':
        AFD=AccessRecordForm(request.POST)

        if AFD.is_valid():
            name=AFD.cleaned_data['name']
            WO=Webpage.objects.get_or_create(name=name)[0]
            author=AFD.cleaned_data['author']
            date=AFD.cleaned_data['date']
            AO=AccessRecord.objects.get_or_create(name=WO,author=author,date=date)[0]
            AO.save()
            AQS=AccessRecord.objects.all()
            d1={'AQS':AQS}
            return render(request,'display_access.html',d1)

    return render(request,'insert_access.html',d)