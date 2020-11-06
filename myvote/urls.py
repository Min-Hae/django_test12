'''
Created on 2020. 11. 6.

@author: KITCOOP
'''
from django.urls.conf import path
from myvote import views
urlpatterns = [
    path('', views.DispFunc, name="disp"), # /gogo/
    path('<int:question_id>/', views.DetailFunc, name="detail"), # /gogo/1
    path('<int:question_id>/vote/', views.VoteFunc, name="vote"), # /gogo/1/vote
    path('<int:question_id>/results/', views.ResultsFunc, name="results"), # /gogo/1/vote
    
]