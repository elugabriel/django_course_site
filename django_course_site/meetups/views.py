from django.shortcuts import render

# Create your views here.
def index(request):

    meetups = [
        {   'title': "first meetup", 
            'location': "Nigeria",
            "slug": 'a-first-meetup'
         },

        {   'title': "second meetup", 
            'location': "Nigeria",
            "slug": 'a-second-meetup'
         }
    ]
    
    return render(request, 'meetups/index.html', 
                  {
                      'show_meetups': True,
                      'meetups':meetups
                   })

def meetup_details(request, meetup_slug):
    selected_meetups = {
        'title': 'A first meetup',
        'description': 'This is the first meetup'
    }
    return render(request, 'meetups/meetup-details.html', {
        'meetup_title': selected_meetups['title'],
        'meetup_description': selected_meetups['description']}
    )