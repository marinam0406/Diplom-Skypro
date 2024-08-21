from rest_framework.generics import ListAPIView, RetrieveAPIView, DestroyAPIView, CreateAPIView, UpdateAPIView
from rest_framework.permissions import IsAuthenticated, AllowAny

from educational_modules.models import EduModel
from educational_modules.pagination import MyPagination
from educational_modules.permissions import IsAdmin
from educational_modules.serializers import EduSerializer


class EduModelAPIView(ListAPIView):
    """
    List all EduModel instances.
    """
    queryset = EduModel.objects.all()
    serializer_class = EduSerializer
    permission_classes = [AllowAny]
    pagination_class = MyPagination


class EduModelDetailAPIView(RetrieveAPIView):
    """
    Retrieve a single EduModel instance.
    """
    queryset = EduModel.objects.all()
    serializer_class = EduSerializer
    permission_classes = [AllowAny]


class EduModelCreateAPIView(CreateAPIView):
    """
    Create a new EduModel instance.
    """
    serializer_class = EduSerializer
    permission_classes = [AllowAny]


class EduModelUpdateAPIView(UpdateAPIView):
    '''
    Update an existing EduModel instance.
    '''
    queryset = EduModel.objects.all()
    serializer_class = EduSerializer
    permission_classes = [IsAuthenticated]


class EduModelDestroyAPIView(DestroyAPIView):
    '''
    Delete an existing EduModel instance.
    '''
    queryset = EduModel.objects.all()
    permission_classes = [IsAdmin]
