from django.urls import path
from collection.views import IndexView

urlpatterns = [
    path('', IndexView.as_view())
]
