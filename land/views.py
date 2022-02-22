from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Land, Image, Customer_Need
import datetime


# @login_required('users/')
def post_form(request):
    return render(request, 'post_form.html')
def index(request):
    return render(request,'index.html')

class Form_make:
    def __init__(self):
        self.land_info = None
        self.images = []

    # @login_required('users/')
    def Land_form(self, request):
        if request.method == "POST":
            location = request.POST.get('location')
            type = request.POST.get('type')
            size = request.POST.get('size')
            value = request.POST.get('value')
            year = request.POST.get('year')
            mobile = request.POST.get('mobile')
            ownerName = request.POST.get('OwnerName')
            new_land = Land(location=location,
                            type=type,
                            size=size,
                            value=value,
                            year=year,
                            mobile=mobile,
                            ownerName=ownerName)
            new_land.ensure = False
            new_land.date = datetime.datetime.now()
            new_land.save()
            self.land_info = new_land
            return render(request, "imagepost.html")
        else:
            return render(request, 'post_form.html')

    # @login_required('users/')
    def image_form(self, request):
        if request.method == 'GET':
            return render(request, "imagepost.html")
        else:
            if request.FILES.get('file') is not None:
                image = request.FILES.get('file')
                image_name = image.name
                image_field = image
                belong = self.land_info
                new_image = Image(name=image_name, image=image_field, belong=belong)
                new_image.save()
                self.images.append(new_image.image.url)
                return render(request, "imagepost.html")
            else:
                return redirect('/')

    def required_post(self, request):
        if request.method == 'GET':
            return render(request, 'required.html')
        else:
            if request.method == 'POST':
                name = request.POST.get('name')
                mobile = request.POST.get('mobile')
                method = request.POST.get('method')
                type = request.POST.get('type')
                province = request.POST.get('province')
                city = request.POST.get('city')
                countrySide = request.POST.get('countryside')
                dis = request.POST.get('dis')
                value_min = request.POST.get('value_min')
                value_max = request.POST.get('value_max')
                year_min = request.POST.get('year_min')
                year_max = request.POST.get('year_max')
                size_min = request.POST.get('size_min')
                size_max = request.POST.get('size_max')
                require = Customer_Need(name=name, mobile=mobile, type=type,method=method,
                                        province=province, city=city,
                                        countrySide=countrySide, dis=dis, value_min=value_min,
                                        value_max=value_max, year_min=year_min, year_max=year_max, size_min=size_min,
                                        size_max=size_max)
                require.save()
                return redirect('/')
