from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response



class CustomArticlePagination(PageNumberPagination):
    page_size = 8
    page_size_query_param = "page_size"
    max_page_size = 30

    def get_paginated_response(self, data):
        return Response({
            "page_info": {
                "current_page": self.page.number,
                "total_pages": self.page.paginator.num_pages,
                "total_items": self.page.paginator.count,
            },
            "items_info": {
                "per_page": self.get_page_size(self.request),
                "count_on_page": len(data),
            },
            "results": data
        })

    def get_page_size(self, request):
        try:
            return super().get_page_size(request)
        except Exception:
            raise ValueError("Invalid page_size parameter. Must be an integer.")