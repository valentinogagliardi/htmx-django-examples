from django_filters import FilterSet, DateFromToRangeFilter
from django_filters.views import FilterView
from django_filters.widgets import RangeWidget

from date_range.models import Book


class BookFilterSet(FilterSet):
    publication_date = DateFromToRangeFilter(widget=RangeWidget(attrs={"type": "date"}))

    class Meta:
        model = Book
        fields = ["publication_date"]


class BookFilter(FilterView):
    filterset_class = BookFilterSet
    template_name = "date_range/book_list.html"

    def get(self, request, *args, **kwargs):
        if request.htmx:
            self.template_name = "date_range/book_list_partial.html"
        return super().get(request, *args, **kwargs)
