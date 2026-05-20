
# Create your views here.
from django.shortcuts import render
from django.conf import settings

def index(request):
    return render(request, 'index.html')

def about(request):
    # Collect all files in the certificates folder and pass to the template
    cert_dir = settings.BASE_DIR / 'certificates'
    certificates = []
    try:
        if cert_dir.exists():
            certificates = sorted([f.name for f in cert_dir.iterdir() if f.is_file()])
    except Exception:
        certificates = []

    return render(request, 'about.html', {'certificates': certificates})

def projects(request):
    return render(request, 'projects.html')

def blog(request):
    return render(request, 'blog.html')

def contact(request):
    return render(request, 'contact.html')