from django.urls import path

from .views import SnackList, SnackDetail

urlpatterns = [
    path('<int:pk>/', SnackDetail.as_view()),
    path('', SnackList.as_view()),
]
