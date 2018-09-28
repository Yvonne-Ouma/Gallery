from django.shortcuts import render, redirect
from django.http import HttpResponse,Http404
import datetime as dt
from .models import Image

# Create your views here.
def welcome(request):
    return render(request, 'gallery.html')

def posts_today(request):
    date = dt.date.today()
    posts = Image.todays_posts()
    
    return render(request, 'all-pics/today-posts.html', {"date": date,"posts": posts})
def convert_dates(dates):
    
    # Function that gets the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    # Returning the actual day of the week
    day = days[day_number]
    return day 

# view function for present posts from past days
def past_days_posts(request,past_date):
    try:
    
        # Converts data from the string Url
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()
      
    except ValueError:
        # Raise 404 error when ValueError is thrown    
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(posts_today)

    posts = Image.days_posts(date)    
    return render(request, 'all-pics/past-posts.html', {"date": date, "posts": posts})

def search_results(request):

    if 'image' in request.GET and request.GET["image"]:
        search_term = request.GET.get("image")
        searched_images = Image.search_by_category(search_term)
        message = f"{search_term}"

        return render(request, 'all-pics/search.html', {"message": message, "images": searched_images}) 

    else:
        message = "You haven't searched for any image"
        return render(request, 'all-pics/search.html', {"message": message})    

