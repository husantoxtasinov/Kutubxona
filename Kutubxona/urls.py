"""Kutubxona URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from asosiy.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('sinashga/', sinashga),
    path('bitiruvchi/',Bitiruvchilar),
    path('talaba_ochir/<int:son>/',talaba_ochir),
    path('studentlar/',hamma_studentlar),
    path('kitob_ochir/<int:son>/',kitob_ochir),
    path('mualliflar',Hamma_mualliflar),
    path('talaba_edit/<int:son>/',student_tahrirlash),
    path('student/<int:son>/',talaba),
    path('talaba_tas/<int:son>/',talaba_tasdiqlash),
    # path('books/',books),
    path('barcha_m',Mualliflar),
    path('muallif/<int:son>/', Muallif),
    path('kitoblar/',Kitoblar),
    path('kitob/<int:son>/',bitta_kitob),
    path('recordlar/',recordlar),
    path('muallifla/',T_mualliflar),
    path('katta/',Katta_kitob),
    path('kop_kitobli/',kitobi_kop_muallif),
    path('recordla/', oxirgi_recordlar),
    path('Kitobla/', tirik_muallif_k),
    path('kitoblarr/', badiiy_kitoblar),
    path('studentlarr/', a_student),
    path('mualliflarr/', yoshi_k_mualliflar),
    path('kkitoblar/', kop_kitobli_mualliflar),
    path('estudentlar/', Erkak_studentlar),
    path('record16/<int:son>/',batafsil_record),
    path('brecordlar', bitiruvchi_studentlar_recordlari),
    path('qrecordlar/', barcha_recordlar),
    path('muallif_ochir/<int:son>/', muallif_ochir),
    path('muallif4/', hamma_mualliflar4),
    path('hammasi',Hamma_mualliflar),
    path('',loginview),
    path('logout/',logoutview),
    path('register/',register),


]
