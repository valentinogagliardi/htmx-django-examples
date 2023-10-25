from django.urls import path
from date_range.views import BookFilter

app_name = "daterange"

urlpatterns = [
    path("", BookFilter.as_view(), name="filter"),
]
