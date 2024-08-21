from rest_framework.pagination import PageNumberPagination


class MyPagination(PageNumberPagination):
    '''
    Custom pagination for paginating EduModel instances.
    '''
    page_size = 5
    page_query_param = "page_size"
    max_page_size = 100
