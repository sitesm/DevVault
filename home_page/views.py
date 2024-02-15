from django.shortcuts import render

# Create your views here.
def home(request):
    # request object has many members such as session and user information
    # the second parameter is the template name relative to the app's template dir
    return render(request, 'home.html')
