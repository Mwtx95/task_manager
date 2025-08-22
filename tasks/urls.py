from django import views
from django.urls import path, include
from rest_framework import routers

from .views import *


router = routers.DefaultRouter()
router.register(r'tasks', TaskViewSet)
router.register(r'tasklist', TaskListViewSet)
router.register(r'subtask', SubTaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
]