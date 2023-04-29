from django.shortcuts import render

# Create your views here.
def index(request):

    meetups = [
        {'title': "first meetup", 
         'location': "Nigeria",
         "slug": 'A-first-meetup'
         },

        {'title': "second meetup", 
         'location': "Nigeria",
         "slug": 'A-first-meetup'
         }
    ]
    
    return render(request, 'meetups/index.html', {'meetups':meetups})