from django.urls import path
from modal_delete.views import BookList, BookDelete

app_name = "modal_delete"

urlpatterns = [
    path("", BookList.as_view(), name="list"),
    path("delete/<int:pk>/", BookDelete.as_view(), name="delete"),
]
