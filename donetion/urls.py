from django.urls import path
from donetion.views import get_donetion

urlpatterns = [

    path('donetion/',get_donetion, name="get_donetion")
    

]