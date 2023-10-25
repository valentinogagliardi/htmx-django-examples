from django.views.generic import ListView, DeleteView
from django.urls import reverse_lazy
from django.http import HttpResponse

from modal_delete.models import Book


class BookList(ListView):
    model = Book


class BookDelete(DeleteView):
    model = Book

    def delete(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.delete()
        res = HttpResponse(status=204)
        res["HX-Redirect"] = reverse_lazy("modal_delete:list")
        return res
