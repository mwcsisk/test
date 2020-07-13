from django.shortcuts import render, redirect

from . import util


def index(request):
    return render(request, "encyclopedia/index.html", {
        "entries": util.list_entries()
    })

def entry(request, title):
    entry = util.get_entry(title)
    if entry:
        return render(request, "encyclopedia/entry.html", {
            "title": title,
            "entry": util.get_entry(title)
        })
    else:
        return render(request, "encyclopedia/error.html", {
            "title": title
        })

def search(request):
    query = request.GET.get('q', '')

    results = []
    for entry in util.list_entries():
        if query.casefold() == entry.casefold():
            return redirect('entry', title=entry)
        elif query.casefold() in entry.casefold():
            results.append(entry)
    return render(request, "encyclopedia/search.html", {
        "query": query,
        "results": results
    })