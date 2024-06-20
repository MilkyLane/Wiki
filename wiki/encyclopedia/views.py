import random

from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse
from markdown2 import Markdown
from django.core.files import File
from . import util
from random import choice

def convertMd(title):
    content =  util.get_entry(title)
    markdower = Markdown()
    if content == None:
        return None
    else:
     return markdower.convert(content)
def index(request):
     return render(request, "encyclopedia/index.html",{
         "entries" : util.list_entries()
  })

'''
def get_page(request,title):
    page = util.get_entry(title)

    if page is None:
        return render(request,"encyclopedia/error.html",{
            "form":form
        })
    return render(request, "encyclopedia/titlepage.html", {
        'title': title,
        'content': page,
        "form": form,

    })
'''

def entry(request,title):
    htmlContent =convertMd(title)
    if htmlContent == None:
        return render(request, "encyclopedia/error.html",{
            "message": "Error 404, Page not found"
        })

    else:
            return render(request, "encyclopedia/entry.html",{
                "title": title,
                "content": htmlContent
            })
def search(request):
    if request.method == "POST":
        eSearch = request.POST['q']
        htmlC = convertMd(eSearch)
        if htmlC is not None:
            return render(request, "encyclopedia/entry.html", {
                "title": eSearch,
                "content": htmlC
            })
        else:
            allEntries = util.list_entries()
            recommend= []
            for entry in allEntries:
                if eSearch.lower() in entry.lower():
                    recommend.append(entry)
            return render(request, "encyclopedia/search.html",{
                "recommend":recommend
            })

def newPage(request):
    if request.method== "GET":
        return render(request,"encyclopedia/new.html")
    else:
        title = request.POST['title']
        content = request.POST['mdC']
        tExist = util.get_entry(title)
        if tExist is not None:
            return render(request, "encyclopedia/error.html",{
                "message": "Error: Page already exists"
            })
        else:
            util.save_entry(title,content)
            htmlC = convertMd(title)
            return render(request, "encyclopedia/new.html",{
                "title": title,
                "content": htmlC
            })
def rand(request):
    aEntries = util.list_entries()
    r = random.choice(aEntries)
    htmlC = convertMd(r)
    return render(request, "encyclopedia/entry.html",{
        "title": r,
        "content": htmlC
    })

def edit(request):
    if request.method== "POST":
        title = request.POST['eTitle']
        content = util.get_entry(title)
        return render(request, "encyclopedia/edit.html", {
            "title": title,
            "content": content
        })
def saveEdit(request):
    if request.method== "POST":
        title=request.POST['title']
        content= request.POST['mdC']
        util.save_entry(title, content)
        htmlC = convertMd(title)
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "content": htmlC
        })