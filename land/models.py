from django.db import models


# Register your models here.
class Land(models.Model):
    ownerName = models.TextField('用户姓名', max_length=32)
    location = models.TextField('地区', max_length=32)
    type = models.TextField('类型与用途', max_length=32)
    size = models.TextField('面积', max_length=10)
    mobile = models.TextField('联系方式', max_length=11)
    ensure = models.BooleanField('是否电话核实')
    value = models.TextField('价格', max_length=30)
    year = models.TextField('流转年限', max_length=5)
    date = models.DateTimeField('发布日期')


class Image(models.Model):
    name = models.CharField('图片名', max_length=32)
    image = models.ImageField('图片')
    belong = models.ForeignKey(Land, on_delete=models.CASCADE)


class Customer_Need(models.Model):
    name = models.CharField('姓名',max_length=20)
    mobile = models.CharField('联系方式',max_length=32)
    method = models.CharField('预期流转方式',max_length=32)
    type = models.CharField("预期土地类型",max_length=32)
    province = models.CharField("省份",max_length=32)
    city = models.CharField("市",max_length=32)
    countrySide = models.CharField("县/区",max_length=32)
    value_min = models.CharField('预期价格下界',max_length=32)
    value_max = models.CharField('预期价格上界',max_length=32)
    year_min = models.CharField("年限下界",max_length=32)
    year_max = models.CharField('年限上界',max_length=32)
    size_min = models.CharField("预期土地范围下界",max_length=32)
    size_max = models.CharField('预期土地范围上界',max_length=32)
    dis = models.TextField('预期描述')


