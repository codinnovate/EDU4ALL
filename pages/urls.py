from django.urls import path
from .views import HomePageView,deafyPageView,blindPageView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('deafy/',deafyPageView.as_view(),name='deafy'),
    path('blind/',blindPageView.as_view(),name='blind')
]
