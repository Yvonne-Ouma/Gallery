from django.shortcuts import render
from django.http import HttpResponse,Http404
import datetime as dt

# Create your views here.
def welcome(request):
    return render(request, 'gallery.html')

def posts_of_day(request):
    date = dt.date.today()
    
    return render(request, 'all-pics/today-posts.html', {"date": date,})
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


        day = convert_dates(date)
        html = f'''
        <html>
            <body>
                <h1>Posts for {day} {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
            '''
        return HttpResponse(html)
