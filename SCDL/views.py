from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import SCDownload

def main(request):
    # request object has many members such as session and user information
    # the second parameter is the template name relative to the app's template dir
    return render(request, 'scdl.html')

def download(request):
    if request.method == 'POST':
        
        form = SCDownload(request.POST)
        
        # get the playlist name
        playlistName = request.POST.get('scURL')
        
        print(playlistName)
        
        
        messages.success(request, "Download successful!")
        
        return redirect('SCDL')
    else:
        return render(request, 'SCDL')
