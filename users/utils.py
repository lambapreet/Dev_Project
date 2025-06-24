
from .models import Profile, Skill
from django.db.models import Q



def searchProfiles(request):
    search_query = ''
    
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')
    
    skills = Skill.objects.filter(name__icontains=search_query)
    
    profiles = Profile.objects.distinct().filter(
        Q(name_icontains=search_query) | 
        Q(short_intro_icontains=search_query) |
        Q(skill_in=skills)
        )
    
    return profiles, search_query