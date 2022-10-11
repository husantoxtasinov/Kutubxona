from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import StudentForm


def sinashga(request):
    return HttpResponse("Hello world!")

def bosh_sahifa(request):
    return render(request,'html.html')
def mashq(request):
    return render(request,'Temir.html')

# def books(request):
#     if request.method=="POST":
#         forma=KitobForm(request.POST)
#         if forma.is_valid():
#             forma.save()
#         return redirect('/books/')
#     data={
#         'books': Kitob.objects.all(),
#         'forma': KitobForm
#     }
#     return render(request, 'mashq/books.html', data)

#1-topshiriq
def Mualliflar(request):
    if request.user.is_authenticated:
        data={
            'barcha_m':Muallif.objects.all()
        }
        return render(request,'html.html',data)
    else:
        return redirect('/')
#2-topshiriq
def Muallif(request, son):
    data = {
        'muallif': Muallif.objects.get(id=son)
    }
    return render(request, 'html_2.html',data)
#3-topshiriq
def Kitoblar(request):
    if request.user.is_authenticated:
        data={
            'kitoblar':Kitob.objects.all()
        }
        return render(request,'html_3.html',data)
    else:
        return redirect('/')
#4-topshiriq
def bitta_kitob(request, son):
    data={
        'kitob':Kitob.objects.get(id=son)
    }
    return render(request,'html_4.html',data)
#5-topshiriq
def recordlar(request):
    data = {
        'recordlar': Record.objects.all()
    }
    return render(request, 'html_5.html', data)
#6-topshiriq
def T_mualliflar(request):
    data = {
        'muallifla': Muallif.objects.filter(tirik=True)
    }
    return render(request, 'html_6.html', data)
#7-topshiriq
def Katta_kitob(request):
    data={
        'katta':Kitob.objects.order_by('sahifa')[:3]
    }
    return render(request,'html_7.html',data)
#8-topshiriq
def kitobi_kop_muallif(request):
    data = {
        'kop_kitobli': Muallif.objects.order_by('-kitob_soni')[:3]
    }
    return  render(request, 'html_8.html', data)
#9-topshiriq
def oxirgi_recordlar(request):
    data = {
        'recordla': Record.objects.order_by('-olingan_sana')[:3]
    }
    return render(request, 'record_9.html', data)
#10-topshiriq
def tirik_muallif_k(request):
    data = {
        'Kitobla': Kitob.objects.filter(muallif__tirik=True)
    }
    return render(request, 'K_muallif_10.html', data)
#11-topshiriq
def badiiy_kitoblar(request):
    data = {
        'kitoblarr': Kitob.objects.filter(janr="Badiiy")
    }
    return render(request, 'kitob11.html',data)
#12-top
def a_student(request):
    data = {
        'studentlarr': Student.objects.filter(ism__contains="a")
    }
    return render(request, 'A_student12.html',data)
#13-top
def yoshi_k_mualliflar(request):
    data = {
        'mualliflarr': Muallif.objects.order_by('tugilgan_yil')[:3]
    }
    return render(request, 'K_muallf13.html', data)
#14-top
def kop_kitobli_mualliflar(request):
    data = {
        'kkitoblar': Kitob.objects.filter(muallif__kitob_soni__lt=10)
    }
    return render(request, 'Kkmuallif14.html', data)
#15-top
def Erkak_studentlar(request):
    data = {
        'estudentlar': Student.objects.filter(jins="Erkak")
    }
    return render(request, 'Estudent15.html', data)
#16-top
def batafsil_record(request,son):
    data = {
        'record': Record.objects.get(id=son),
        'bool': Record.objects.get(id=son).qaytardi
    }
    return render(request, 'brecord16.html', data)
#17-top
def bitiruvchi_studentlar_recordlari(request):
    data = {
        'brecordlar':  Record.objects.filter(student__bitiruvchi=True)
    }
    return render(request, 'bstudent17.html', data)
#7-dars
#1-top
def barcha_recordlar(request):
    ism = request.GET.get('ism')
    if ism is None:
        m = Record.objects.all()
    else:
        m = Record.objects.filter(student__ism__contains=ism)
    data = {
        'qrecordlar': m
    }
    return render(request, '7darsrecord1.html/', data)
#2-top
def muallif_ochir(request,son):
    Muallif.objects.get(id=son).delete()
    return redirect('/mualliflar2/')
#3-top
def hamma_recordlar3(request):
    data = {
        'recordlar': Record.objects.all()
    }
    return render(request, '7Dars/record3.html', data)


def record_ochir3(request,son):
    Record.objects.get(id=son).delete()
    return redirect('/recordlar3/')
#4-top
def hamma_mualliflar4(request):
    ism = request.GET.get('soz')
    if ism is None:
        s = Muallif.objects.all()
    else:
        s = Muallif.objects.filter(ism__contains=ism)
    data = {
        'mualliflar': s
    }
    return render(request, '7Darsmuallif4.html', data)



def hamma_studentlar(request):
    if request.method=='POST':
        f=StudentForm(request.POST)
        if f.is_valid():
            Student.objects.create(
                ism=f.cleaned_data.get('i'),
                jins=f.cleaned_data.get('j'),
                kitob_soni=f.cleaned_data.get('kitoblari_soni'),
                bitiruvchi=f.cleaned_data.get('bitiruvchi')
            )
        return redirect('/studentlar/')
    soz = request.GET.get('q_sozi')
    if soz is None:
        s = Student.objects.all()
    else:
        s=Student.objects.filter(ism__contains=soz)
    data={
        'studentlar':s,
        'forma':StudentForm

    }
    return render(request, 'Student.html',data)
def Bitiruvchilar(request):

    data={
        'bitiruvchi':Student.objects.filter()
    }
    return render(request,'mashq/Bitiruvchi.html',data)

def talaba_ochir(request,son):
    Student.objects.get(id=son).delete()
    return redirect('/studentlar/')

def talaba_tasdiqlash(request, son):
    data={
        'talaba':Student.objects.get(id=son)
    }
    return render(request, 'talaba_ochir.html', data)


def kitob_ochir(request,son):
    Kitoblar.objects.get(id=son).delete()
    return redirect('/kitoblar/')


def talaba(request, son):
    data={
        'student' : Student.objects.get(id=son)
    }
    return render(request, 'mashq/Student.html', data)

def student_tahrirlash(request,son):
    if request.method=='POST':
        if request.POST.get('bt')=='on':
            natija=True
        else:
            natija=False
        Student.objects.filter(id=son).update(
            ism=request.POST.get('ismi'),
            kitob_soni=request.POST.get('k_soni'),
            bitiruvchi=natija
            )
        return redirect('/studentlar/')


    data={
        'student':Student.objects.get(id=son)
    }
    return render(request, 'student-edit.html',data)

def Hamma_mualliflar(request):
    data={
        'hammasi':Muallif.objects.all()
    }
    return render(request,'Hamma_muallif8.html',data)


def loginview(request):
    if request.method=='POST':
        user=authenticate(username=request.POST.get('l'),
                          pasword=request.POST.get('p'))
        if user is None:
            return redirect('')
        login(request,user)
        return redirect('/studentlar/')
    return (request,'login.html')

def logoutview(request):
    logout(request)
    return redirect('/')

def register(request):
    if request.method=='POST':
        u=User.objects.create_user(username=request.POST.get('login'),
                                   password=request.POST.get('parol')
                                   )
        Student.objects.create(
            ism=request.POST.get('i'),
            bitiruvchi=request.POST.get('b'),
            kitob_soni=request.POST.get('k_s'),
            user=u
        )
        return redirect('/')
    return render(request,'register.html')