from django.shortcuts import render

# Create your views here.
def create_post(request):
    return render(request,"create_post.html", {})

def edit_post(request):
    return render(request,"edit_post.html", {})

def read_post(request):
    return render(request,"read_post.html", {})

def post_list(request):
    return render(request,"post_list.html", {})

def search(request):
    return render(request,"search.html", {})


