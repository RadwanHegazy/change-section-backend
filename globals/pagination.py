from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from dataclasses import dataclass

@dataclass
class PaginationMainClass :
    queryset:str
    serializer_class:object
    request:object
    page_size:int=10

    def start (self) :
        self.page = self.request.query_params.get("page")
        self.default_page_size = self.page_size
        
        paginator = Paginator(self.queryset, self.default_page_size)

        page = self.page

        if page == None or not page:
            page = 1
        page = int(page)

        try:
            model = paginator.page(page)
        except PageNotAnInteger:
            model = paginator.page(1)
        except EmptyPage:
            model = paginator.page(paginator.num_pages)

        has_previous = model.has_previous()
        has_next = model.has_next()
        pages = paginator.num_pages


        serializer = self.serializer_class(model, many=True)
        data = {
            "data": serializer.data,
            "page": page,
            "pages": pages,
            "has_previous": has_previous,
            "has_next": has_next,
        }

        return data
