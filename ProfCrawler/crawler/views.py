from django.shortcuts import render, render_to_response

from bs4 import BeautifulSoup
from django.core import serializers

import json
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


import requests

from crawler.models import Profile, Skill


def profile(request):
    return render_to_response('profile.html')


def get_profile_html_by_url(url):

    if not url.startswith( 'http' ):
        response_data = {}

        response_data['error'] = 'Please enter a valid url which starts with http'

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )

    user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36"

    headers = {'content-type': 'application/json', 'Accept-Charset': 'UTF-8', 'User-Agent' : user_agent}
    r = requests.get(url, headers=headers);

    soup = BeautifulSoup(r.content)

    profile = soup.find("div", {"class": "profile-overview-content"})
    if profile:
        # if profile.find("div", {"class":"profile-picture"}):
        #     profile_picture = profile.find("div", {"class":"profile-picture"}).find("a",href=True)['href']
        # else:
        #     profile_picture = ''

        if profile.find("p", {"class":"headline title"}):
            title = profile.find("p", {"class":"headline title"}).text
        else:
            title = ''

        if profile.find(id="name"):
            name = profile.find(id="name").text
        else:
            name = ''

        # id = profile_picture + ":" + name

        if profile.find("span",{"class":"org"}):
            current_pos = profile.find("span",{"class":"org"}).text
        else:
            current_pos = ''

        if soup.find("div", {"class":"description"}).find("p"):
            summary = soup.find("div", {"class":"description"}).find("p").text
        else:
            summary = ''

        if soup.find_all("li", {"class": "skill"}):
            count_top_skills = int(len(soup.find_all("li", {"class": "skill"})) - len(soup.find_all("li", {"class": "skill extra"})))
        else:
            count_top_skills = 0

        newProfile = Profile(url=url, name=name, title=title, current_position=current_pos, summary=summary, count_top_skills=count_top_skills)

        newProfile.save()


        skills = soup.find(id="skills").findAll("span", {"class": "wrap"})
        for skill in skills:
            newSkill = Skill(name=skill.text)
            newSkill.save()
            newProfile.skills.add(newSkill)

        serialized_profile = serializers.serialize('json', [newProfile, ])

        response_data = {}
        response_data['data'] = serialized_profile



    else:
        response_data = {}

        response_data['error'] = 'Profile does not exist'

    return HttpResponse(
        json.dumps(response_data),
        content_type="application/json"
    )



@csrf_exempt
def get_profile(request):
    url = request.POST.get("url", "")
    print(url)

    if "linkedin.com/in" not in url:
        response_data = {}

        response_data['error'] = 'Please enter a url to linkedin public profile.'

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    return get_profile_html_by_url(url)

@csrf_exempt
def get_number_of_top_skills(request):
    url = request.POST.get("url", "")
    return get_number_of_top_skills_by_url(url)

def get_number_of_top_skills_by_url(url):
    response_data = {}
    try:
        profile = Profile.objects.get(url=url)
        response_data['data'] = profile.count_top_skills
    except Profile.DoesNotExist:
        response_data['error'] = 'Something went wrong. Try again.'

    return HttpResponse(
        json.dumps(response_data),
        content_type="application/json"
    )
