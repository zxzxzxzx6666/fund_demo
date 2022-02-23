# rest
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

# model
from .models import funds
from .serializers import fundsSerializer

from rest_framework import status, authentication, permissions

# 基金總覽
class fundsList(APIView):
    # 驗證
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request, format=None):
        fund_data = funds.objects.all()
        serializer = fundsSerializer(fund_data, many=True) # 大於一個用 more
        return Response(serializer.data)

# 價格篩選
@api_view(['POST'])
def priceFilter(request):
    # 取得 post request data
    price = float(request.POST.get('price'))
    filter = request.POST.get('filter')
    if filter=="bigger":
        funds_list=funds.objects.filter(price__gte=price)    
    if filter=="smaller":
        funds_list=funds.objects.filter(price__lte=price)
    serializer = fundsSerializer(funds_list, many=True)
    return Response(serializer.data)

#  use linux test command
#  curl -d 'price=2000&filter=bigger' 'http://192.168.56.159:8000/api/v1/price-filter/'

