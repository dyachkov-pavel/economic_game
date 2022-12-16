from datetime import datetime, timezone
from rest_framework.views import APIView
from rest_framework.response import Response

from . import img_map


class StockByTime(APIView):
    def get(self, request, company_id, format=None):
        hour = datetime.now(timezone.utc).hour + 3

        company_dict = img_map.get(company_id)
        if company_dict is None:
            return Response(data='Wrong company id (number)', status=404)

        max_our = max(company_dict.keys())
        if hour - max_our < 2:
            hour = max_our

        link = company_dict.get(hour)
        if link is None:
            return Response(data='No stocks now', status=404)

        return Response(data=link, status=200)
