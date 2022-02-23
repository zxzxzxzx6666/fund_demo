# 序列化套件
from rest_framework import serializers

from .models import funds

class fundsSerializer(serializers.ModelSerializer):
    class Meta:
        model = funds 
        # 前端要轉換的欄位
        fields = ( 
            "id",
            "name",
            "description",
            "price",
            "subscription",
            "redemption",
            "time",
            "get_absolute_url",
        )
