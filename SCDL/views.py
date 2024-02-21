from django.shortcuts import render, redirect
from django.contrib import messages
import os
import subprocess

def main(request):
    # request object has many members such as session and user information
    # the second parameter is the template name relative to the app's template dir
    return render(request, 'scdl.html')

def download(request):
    if request.method == 'POST':
        
        # get the playlist name
        scURL = request.POST.get('scURL')
        
        # Download
        command = ["scdl", "--path", "/media/Music", "-l", scURL]
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        messages.success(request, "Download Underway...!")
        
        return redirect('SCDL')
    else:
        return render(request, 'SCDL')
