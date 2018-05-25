
from django.urls import include, path
from . import views
urlpatterns = [
    
    path('', views.index,name="index"),
    path('compRhyme',views.rhyme,name="compGame"),
    path('multiRhyme',views.mRhyme,name="multiGame")                
]
