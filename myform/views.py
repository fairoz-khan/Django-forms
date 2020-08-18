from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Base(request):
    return render(request, 'Base.html')

def form(request):
    if request.method == 'POST':
        email = request.POST.get('mail')
        password = request.POST.get('pswrd')
        fname = request.POST.get('fname')
        lname = request.POST.get('lname')
        gender = request.POST.get('gender')
        return HttpResponse(f"<h3>email:{email}<br>password:{password}<br>first-name:{fname}<br>Last-name:{lname}<br>Gender:{gender}<br></h3>")
    return render(request, 'myform/form.html')

def multiselect(request):
    if request.method == "POST":
        languages = request.POST.getlist('language')
        Framework = request.POST.getlist('framework') 
        return HttpResponse(f"<h2>{languages}<br>{Framework}</h2>")
    return render(request, 'myform/multiselect.html')

# Uploading and displaying the uploaded image
from django.core.files.storage import FileSystemStorage
# import subprocess
# subprocess.call("/Users/apple/Documents/Jspider/django/projects/form/media")
def mediaUpload(request):
    file_url = ''
    if request.method == 'POST' and request.FILES:
        image = request.FILES['img']
        fs = FileSystemStorage()
        file = fs.save(image.name, image)
        file_url = fs.url(file)
        print(file_url)
    return render(request, 'myform/mediaup.html', {'file_url': file_url})


from .forms import SampleForm

def djangoform(request):
    form = SampleForm()
    return render(request, 'myform/dforms.html', {'form': form})