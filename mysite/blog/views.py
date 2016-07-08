from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.conf import settings
import os
import urllib.request
import urllib
import json
from bs4 import *

from tools.forms import instForm


def index(request):
    return render(request, 'index.html')


def instagram(request, starID):
    url = 'https://www.instagram.com/' + starID
    myRequest = urllib.request.Request(url)
    response = urllib.request.urlopen(myRequest, timeout=2)
    html = response.read().decode('utf-8')
    html = BeautifulSoup(html, 'html.parser')

    body = html.find_all('body')
    scripts = body[0].find_all('script')
    jsonInfo = scripts[2].string

    jsonInfo = json.loads(jsonInfo[21: len(jsonInfo) - 1])

    images = jsonInfo['entry_data']['ProfilePage'][0]['user']['media']['nodes']

    path = []
    file = []
    for i in range(0, len(images)):
        path.append('../../python_web/person-blog/mysite/blog/static/img/' + starID + str(i) + '.jpg')
        urllib.request.urlretrieve(images[i]['display_src'], path[i])
        file.append('/static/img/' + starID + str(i) + '.jpg')

    return render(request, 'instagram.html', {'id': starID, 'path': file})

    # return HttpResponse(settings.STATIC_URL)


def starsIns(request):
    if request.method == 'POST':
        form = instForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('/instagram/' + form.cleaned_data['id'] + '/')
    else:
        form = instForm()
    return render(request, 'starsIns.html', {'form': form})


def get_name(s):
    s = s.split(': ', 1)[1]
    family_name = s.split(', ', 1)[0]
    given_name = s.split(', ', 1)[1]
    return family_name + ' ' + given_name


def parse_course(table_info, start_time, duration):
    code = table_info.find_all('table')[0].find_all('font')[0].string
    course_name = table_info.find_all('table')[1].find_all('font')[0].string
    location = table_info.find_all('table')[2].find_all('font')[0].string
    stime = 8 + float(start_time / 2)
    end_time = stime + duration / 2
    time = str(stime) + '-' + str(end_time)
    return {'code': code, 'name': course_name, 'location': location, 'start_time': str(stime),
            'end_time': str(end_time)}


def timetable(request, studentId, weekBegin, weekEnd):

    data = {}

    try:

        for week in range(int(weekBegin), int(weekEnd)):
            url = 'http://timetablingunnc.nottingham.ac.uk:8005/reporting/Individual;Students;id;' + studentId + '?template=SWSCUST+Student+Individual&weeks=' + str(
                week) + '&days=1-5&periods=1-26&Width=0&Height=0'

            request = urllib.request.Request(url)
            response = urllib.request.urlopen(request)
            html = response.read().decode('utf-8')

            html = BeautifulSoup(html, 'html.parser')
            tables = html.find_all('table')
            name = get_name(tables[5].b.string)

            course_info = tables[6]
            m_day = 1
            single_week = {}
            for day in course_info.find_all('tr', recursive=False)[1:6]:
                number_of_td = len(day.find_all('td', recursive=False))
                index = 0
                course = []
                for i in range(1, number_of_td):
                    try:
                        start_time = index
                        duration = int(day.find_all('td', recursive=False)[i]['colspan'])
                        course.append(parse_course(day.find_all('td', recursive=False)[i], index, duration))
                        index += duration
                    except:
                        index += 1
                        continue
                single_week[m_day] = course
                m_day += 1
            print(week)
            data[week] = single_week
    except:
        print('Error student id...Please check again!')

    # print(json.dumps(data, indent=4))
    return HttpResponse(str(json.dumps(data, indent=4)))


# HTTP Error 400
def error(request):
    return render(request, '404.html', status=404)
