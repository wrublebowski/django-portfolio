from django.urls import path
from blog_app import views
#from . import views <-- we could code that because it's the same folder

app_name = 'blog_app'

urlpatterns = [
    path ('', views.all_blogs, name="all_blogs"),
    path ('<int:blog_id>/', views.detail, name="detail"),
]
