from django.shortcuts import render

def home(request):
    context = {
        "name": "Suganya S",
        "title": "Web Developer",
        "email": "suganya@gmail.com",
        "phone": "+91 9876543210",
        "image": "profile_app/images/profile.webp",
    }
    return render(request, "profile_app/home.html", context)
