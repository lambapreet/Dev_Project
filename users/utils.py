
from .models import Profile, Skill
from django.db.models import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage



def paginateProfiles(request, profiles, results):
    page = request.GET.get('page')
    
    # Use the 'results' value passed to the function
    paginator = Paginator(profiles.order_by('id'), results)

    try:
        profiles = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        profiles = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        profiles = paginator.page(page)    

    page = int(page)

    leftIndex = max(page - 1, 1)
    rightIndex = min(page + 2, paginator.num_pages + 1)

    custom_range = range(leftIndex, rightIndex)

    return custom_range, profiles


# def paginateProfiles(request, profiles, results):
    
#     page = request.GET.get('page')
#     paginator = Paginator(page, results)
    
#     paginator = Paginator(profiles.order_by('id'), 5)

    
#     try:
#         profiles = paginator.page(page)
#     except PageNotAnInteger:
#         page = 1
#         profiles = paginator.page(page)
#     except EmptyPage:
#         page = paginator.num_pages
#         profiles = paginator.page(page)    
        
#     leftIndex = (int(page) - 1)
    
#     if leftIndex < 1:
#         leftIndex = 1
    
#     rightIndex = (int(page) + 2)
    
#     if rightIndex > paginator.num_pages:
#         rightIndex = paginator.num_pages + 1
        
#     custom_range = range(leftIndex, rightIndex)
    
#     return custom_range, profiles


def searchProfiles(request):
    search_query = request.GET.get('search_query', '')

    skills = Skill.objects.filter(name__icontains=search_query)

    profiles = Profile.objects.distinct().filter(
        Q(name__icontains=search_query) | 
        Q(short_intro__icontains=search_query) |
        Q(skill__in=skills)
    )

    return profiles, search_query

# def searchProfiles(request):
#     search_query = ''
    
#     if request.GET.get('search_query'):
#         search_query = request.GET.get('search_query')
    
#     skills = Skill.objects.filter(name__icontains=search_query)
    
#     profiles = Profile.objects.distinct().filter(
#         Q(name__icontains=search_query) | 
#         Q(short_intro__icontains=search_query) |
#         Q(skill__in=skills)
#         )
    
#     return profiles, search_query