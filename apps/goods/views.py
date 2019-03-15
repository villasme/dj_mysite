from rest_framework import viewsets


from .models import GoodInfo
from .serializers import GoodInfoSerializer


class GoodInfoView(viewsets.ModelViewSet):
    queryset = GoodInfo.objects.all()
    serializer_class = GoodInfoSerializer
