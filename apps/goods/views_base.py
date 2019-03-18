from django.views.generic.base import View

from .models import Good


class GoodsView(View):
    def get(self, request):
        goods = Good.objects.all()

        from django.core import serializers
        json_data = serializers.serialize('json', goods)
        import json
        json_data = json.loads(json_data)
        from django.http import JsonResponse

        return JsonResponse(json_data, safe=False)
