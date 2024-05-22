from django.urls import path
from blogs import views
from blogs.views import blogsViewSet
from .views import RegisterViewSet,LoginViewSet
urlpatterns = [
    path("blogs/", blogsViewSet.as_view()),
    path("blogs/<int:id>/", blogsViewSet.as_view()),
    path("register/", RegisterViewSet.as_view()),
    path("login/", LoginViewSet.as_view()),
]