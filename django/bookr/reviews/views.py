from django.shortcuts import render
def index(request):
    name="world"
    book=request.GET.get("book") or "Enter the book title"
    #return render(request, "base.html", {'name': name})
    return render(request, 'search.html', {'book': book})





