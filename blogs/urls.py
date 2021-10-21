from django.urls import path
from .views import ManageBlog, getBlog, getTagList

urlpatterns = [
    path('create-blog', ManageBlog.as_view()),
    path('edit-blog/<id>', ManageBlog.as_view()),
    path('blog/<id>', getBlog.as_view()),
    path('list-blog/<tag>', getTagList.as_view()),
    path('list-blog', ManageBlog.as_view()),
]
