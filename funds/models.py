from django.core.files import File
from django.db import models

# funds schema
class funds(models.Model):
    name = models.CharField(max_length=255) # 基金名稱
    slug = models.SlugField() # 基金的網頁 slug
    price = models.DecimalField(max_digits=20,decimal_places=2) # 基金每單位當前價格 $NTD 
    subscription = models.DecimalField(max_digits=50,decimal_places=2) # 基金申購量 
    redemption = models.DecimalField(max_digits=50,decimal_places=2) # 基金贖回量 
    description = models.TextField(blank=True, null=True) # 基金敘述 
    time = models.DateTimeField() # 時間(以日為單位) 

    # 照價格排序
    class Meta:
        ordering = ('price',)

    # slug 改為網址後墜
    def get_absolute_url(self):
        return f'/{self.slug}/'