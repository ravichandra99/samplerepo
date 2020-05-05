from django.urls import path
from webinar.views import Index, thanks

app_name = 'webinar'

urlpatterns = [
    path('', Index, name = 'index'),
    path('thanks/<just_id>', thanks, name = 'thanks'),
]