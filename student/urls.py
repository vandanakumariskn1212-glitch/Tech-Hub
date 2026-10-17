from django.urls import path 
from . import views

urlpatterns=[
    path("dashboard/",views.dashboard),
    path("category/",views.mycategory),
    path("lectures/",views.lectures),
    path("lecturecat/",views.lecturecat),
    path("notes/",views.enotes),
    path("profile/",views.profile),
    path("softwarekit/",views.software),
    path("signout/",views.signout),
    path("task/",views.task),
    path("tsubmitted/",views.tsubmitted),
    
]