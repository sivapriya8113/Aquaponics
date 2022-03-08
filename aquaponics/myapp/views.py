from django.shortcuts import render
from django.db import connection
from django.contrib.auth.models import User
from django.contrib.auth import login as log, logout, authenticate
from .models import *
from django.db.models import Q

from .models import registration, product, category


def index(request):
    return render(request, 'index.html', {})


def adminindex(request):
    return render(request, 'admin/index.html', {})


def adminaddcat(request):
    if request.method == "POST":
        h = category()
        h.cat_name = request.POST.get('catname')
        h.cat_img = request.FILES['image']
        h.save()
        return render(request, 'admin/addcategory.html', {'r': 'Inserted'})
    else:
        return render(request, 'admin/addcategory.html', {})


def deletecategory(request, value):
    s = category.objects.get(cat_id=int(value))
    s.delete()
    s = category.objects.all()
    return render(request, 'admin/viewcategory.html', {'s': s})


def adminviewusers(request):
    ids = User.objects.filter(last_name='User').values_list('id', flat=True)
    s = registration.objects.filter(user_id_id__in=ids).values('user_name', 'user_address', 'user_phone', 'user_email',
                                                               'user_id_id')
    return render(request, 'admin/viewusers.html', {'s': s})


def adminviewfarmers(request):
    ids = User.objects.filter(last_name='Farmer').values_list('id', flat=True)
    s = registration.objects.filter(user_id_id__in=ids).values('user_name', 'user_address',
                                                               'user_phone', 'user_email',
                                                               'user_id_id')
    return render(request, 'admin/viewfarmers.html', {'s': s})


def farmerapprove(request, value):
    s = User.objects.get(id=int(value))
    print(s)
    print(s.is_active)
    s.is_active = True
    s.save()
    print(s.is_active)
    ids = User.objects.filter(last_name='Farmer').values_list('id', flat=True)
    s = registration.objects.filter(user_id_id__in=ids).values('user_name', 'user_address', 'user_phone', 'user_email',
                                                               'user_id_id')
    return render(request, 'admin/viewfarmers.html', {'s': s})


def farmerreject(request, value):
    s = User.objects.get(id=int(value))
    print(s)
    s.is_active = 0
    s.save()
    ids = User.objects.filter(last_name='Farmer').values_list('id', flat=True)
    s = registration.objects.filter(user_id_id__in=ids).values('user_name', 'user_address', 'user_phone', 'user_email',
                                                               'user_id_id')
    return render(request, 'admin/viewfarmers.html', {'s': s})


def adminviewsuppliers(request):
    ids = User.objects.filter(last_name='Farmer').values_list('id', flat=True)
    s = registration.objects.filter(user_id_id__in=ids).values('user_name', 'user_address', 'user_phone', 'user_email',
                                                               'user_id_id')
    return render(request, 'admin/viewfarmers.html', {'s': s})


def supplierapprove(request, value):
    s = User.objects.get(id=int(value))
    print(s)
    print(s.is_active)
    s.is_active = True
    s.save()
    print(s.is_active)
    ids = User.objects.filter(last_name='Farmer').values_list('id', flat=True)
    s = registration.objects.filter(user_id_id__in=ids).values('user_name', 'user_address', 'user_phone', 'user_email',
                                                               'user_id_id')
    return render(request, 'admin/viewfarmers.html', {'s': s})


def supplierreject(request, value):
    s = User.objects.get(id=int(value))
    print(s)
    s.is_active = 0
    s.save()
    ids = User.objects.filter(last_name='Farmer').values_list('id', flat=True)
    s = registration.objects.filter(user_id_id__in=ids).values('user_name', 'user_address', 'user_phone', 'user_email',
                                                               'user_id_id')
    return render(request, 'admin/viewfarmers.html', {'s': s})


def adminviewcategory(request):
    s = category.objects.all()
    return render(request, 'admin/viewcategory.html', {'s': s})


def editcategory(request, value):
    s = category.objects.get(cat_id=int(value))
    return render(request, 'admin/editcategory.html', {'s': s})


def adminupdatecategory(request):
    if request.method == "POST":
        id = request.POST.get('catid')
        h = category.objects.get(cat_id=id)
        h.cat_name = request.POST.get('catname')
        h.cat_img = request.FILES['image']
        h.save()
        s = category.objects.all()
        return render(request, 'admin/viewcategory.html', {'s': s})


def adminaddguideline(request):
    if request.method == "POST":
        h = guideline()
        h.g_name = request.POST.get('gname')
        h.g_desc = request.POST.get('gdesc')
        h.g_img = request.FILES['image']
        print(h.g_name)
        h.save()
        return render(request, 'admin/addguideline.html', {'r': 'Inserted'})
    else:
        return render(request, 'admin/addguideline.html', {})


def adminviewguideline(request):
    s = category.objects.all()
    return render(request, 'admin/viewcategory.html', {'s': s})


def editguideline(request, value):
    s = category.objects.get(cat_id=int(value))
    return render(request, 'admin/editcategory.html', {'s': s})


def deleteguideline(request, value):
    s = category.objects.get(cat_id=int(value))
    s.delete()
    s = category.objects.all()
    return render(request, 'admin/viewcategory.html', {'s': s})


def userregistration(request):
    if request.method == "POST":
        obj = registration()
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        obj.user_name = name
        obj.user_email = email
        obj.user_address = address
        obj.user_phone = phone
        if User.objects.filter(email=email).exists():
            return render(request, 'userregistration.html', {'r': 'Already Exists'})
        else:
            u = User()
            u.username = email

            u.email = email
            u.password = password
            u.last_name = 'User'
            u.is_active = 0
            u.save()
            obj.user_id = u
            obj.save()
            return render(request, 'userregistration.html', {'r': 'registered'})
    else:
        return render(request, 'userregistration.html', {})


def farmerregistration(request):
    if request.method == "POST":
        obj = registration()
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        obj.user_name = name
        obj.user_email = email
        obj.user_address = address
        obj.user_phone = phone
        if User.objects.filter(email=email).exists():
            return render(request, 'farmerregistration.html', {'r': 'Already Exists'})
        else:
            u = User()
            u.username = email

            u.email = email
            u.password = password
            u.last_name = 'Farmer'
            u.is_active = 0
            u.save()
            obj.user_id = u
            obj.save()
            return render(request, 'farmerregistration.html', {'r': 'registered'})
    else:
        return render(request, 'farmerregistration.html', {})


def supplierregistration(request):
    if request.method == "POST":
        obj = registration()
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        obj.user_name = name
        obj.user_email = email
        obj.user_address = address
        obj.user_phone = phone
        if User.objects.filter(email=email).exists():
            return render(request, 'supplierregistration.html', {'r': 'Already Exists'})
        else:
            u = User()
            u.username = email

            u.email = email
            u.password = password
            u.last_name = 'Supplier'
            u.is_active = 0
            u.save()
            obj.user_id = u
            obj.save()
            return render(request, 'supplierregistration.html', {'r': 'registered'})
    else:
        return render(request, 'supplierregistration.html', {})


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            u = authenticate(request, email=email, password=password, is_active=1)
            u = User.objects.get(email=email, password=password, is_active=1)
            log(request, u)
            if u.last_name == 'User':
                return render(request, 'reguser/userhome.html', {})
            elif u.last_name == 'Farmer':
                return render(request, 'farmer/farmerhome.html', {})
            elif u.last_name == 'Supplier':
                return render(request, 'supplier/supplierhome.html', {})
            elif u.last_name == 'admin':
                return render(request, 'admin/index.html', {})
        except:
            return render(request, 'login.html', {})
    else:
        return render(request, 'login.html', {})


def userhome(request):
    return render(request, 'reguser/userhome.html', {})


def farmerhome(request):
    print("gggggggggggggggggggggg")
    return render(request, 'farmer/farmerhome.html', {})


def supplierhome(request):
    print("gggggggggggggggggggggg")
    return render(request, 'supplier/supplierhome.html', {})


def adminhome(request):
    print("gggggggggggggggggggggg")
    return render(request, 'admin/adminhome.html', {})


def sup_addmaterial(request):
    if request.method == "POST":
        h = product()
        h.cat_id_id = request.POST.get('catname')
        h.p_name = request.POST.get('matname')
        h.p_desc = request.POST.get('matdesc')
        h.p_price = request.POST.get('matprice')
        h.p_img = request.FILES['image']
        username = request.user
        h.user_id = username
        h.save()
        return render(request, 'supplier/addmaterial.html', {'r': 'Inserted'})
    else:
        s = category.objects.all()
        return render(request, 'supplier/addmaterial.html', {'s': s})


def sup_viewproduct(request):
    s = product.objects.all()
    return render(request, 'supplier/viewproducts.html', {'s': s})