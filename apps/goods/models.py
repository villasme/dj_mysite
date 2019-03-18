from datetime import datetime

from django.db import models

# Create your models here.


class GoodBrand(models.Model):
    """
    品牌
    """
    name = models.CharField(default='', max_length=100, verbose_name="品牌名称")
    desc = models.TextField(default='', max_length=200, verbose_name='品牌描述')
    image = models.ImageField(max_length=200, upload_to='brand/', null=True, blank=True, verbose_name="品牌LOGO")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "品牌"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Good(models.Model):
    """
    商品类
    """
    goodsName = models.CharField(max_length=50, verbose_name="商品名称", help_text="商品名称")
    goodsNum = models.IntegerField(default=0, verbose_name="商品库存", help_text="商品库存")
    goodsPrice = models.IntegerField(default=0, verbose_name="商品价格", help_text="商品价格")
    goodsSpecId = models.CharField(max_length=200, verbose_name="商品规格", help_text="商品规格")
    goodsImg = models.ImageField(max_length=200, upload_to='goods/', null=True, blank=True, verbose_name="商品图", help_text="商品图")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间", help_text="添加时间")
    brands = models.ForeignKey(GoodBrand, related_name='goods', null=True, blank=True, verbose_name="品牌",
                               on_delete=models.CASCADE, help_text="品牌")

    class Meta:
        verbose_name = '商品'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.goodsName


class GoodInfo(models.Model):
    """
    创建商品
    """
    name = '商品'
    goods = models.ForeignKey(Good, related_name='create_good', null=True, blank=True, verbose_name="商品名称",
                              on_delete=models.CASCADE)
    brands = models.ForeignKey(GoodBrand, related_name='create_good', null=True, blank=True, verbose_name='品牌',
                               on_delete=models.CASCADE)
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = '上架'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name
