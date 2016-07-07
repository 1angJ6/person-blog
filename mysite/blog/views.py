from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
import os
import urllib.request
import urllib
import json
from bs4 import *

from tools.forms import instForm


def index(request):
    return render(request, 'index.html')


def instagram(request, starID):

    # url = 'https://www.instagram.com/' + starID
    # myRequest = urllib.request.Request(url)
    # response = urllib.request.urlopen(myRequest, timeout=2)
    # html = response.read().decode('utf-8')
    # html = BeautifulSoup(html, 'html.parser')
    #
    # body = html.find_all('body')
    # scripts = body[0].find_all('script')
    # jsonInfo = scripts[2].string
    #
    # jsonInfo = json.loads(jsonInfo[21: len(jsonInfo) - 1])
    #
    # images = jsonInfo['entry_data']['ProfilePage'][0]['user']['media']['nodes']
    #
    # path = []
    # for i in range(0, len(images)):
    #     path.append('/static/img/' + starID + str(i) + '.jpg')
    #     urllib.request.urlretrieve(images[i]['display_src'], path[i])
    #
    # return render(request, 'instagram.html', {'id': starID, 'path': path})
    return HttpResponse(os.listdir(os.getcwd()))


def starsIns(request):
    if request.method == 'POST':
        form = instForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/instagram/'+form.cleaned_data['id']+'/')
    else:
        form = instForm()
    return render(request, 'starsIns.html', {'form': form})


# HTTP Error 400
def error(request):
    return render(request, '404.html', status=404)
