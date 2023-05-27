from django.urls import path
from . import views

urlpatterns = [
    path('', views.PostList.as_view()), # CSV 방식
    path("/<int:pk>/", views.single_post_page),
    # path('', views.index) # FSV 방식
]