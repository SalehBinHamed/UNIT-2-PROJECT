from . import views
from django.urls import path


urlpatterns =[
    path('',views.home_views , name='change_background'),
    path("about/",views.about_views,name="about_views"),
]