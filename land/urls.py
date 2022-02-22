from django.urls import path
from . import views

form = views.Form_make()
urlpatterns = [
    path('add/',views.post_form),
    path('infoadd/',form.Land_form),
    path('imageadd/',form.image_form),
    path('need/',form.required_post),
    path('',views.index)
]