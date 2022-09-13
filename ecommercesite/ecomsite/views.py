import json

from django.http import HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from .models import C1,ourstory,whychooseus,oursuppliers,homesoldproducts,weworkwith,manageyoursec,ourfleet,regionsweserver,RegisterUser,contactus,products,ProductCategory,ProductBrand2,Suppliers,Cart,Wish
from django.contrib.auth.hashers import make_password,check_password
def home(request):
    crousal = C1.objects.all()
    nSlides = len(crousal)
    os1 = ourstory.objects.all()
    w1 = whychooseus.objects.all()
    os2 = oursuppliers.objects.all()
    hsp=homesoldproducts.objects.all()
    www=weworkwith.objects.all()
    mys=manageyoursec.objects.all()
    of=ourfleet.objects.all()
    rws=regionsweserver.objects.all()
    pr = products.objects.all()
    params = {'no_of_slides': nSlides, 'range': range(0, nSlides), 'crousal': crousal,'os1':os1, 'w1':w1, 'os2':os2,'hsp':hsp, 'www':www, 'mys':mys, 'of':of, 'rws':rws, 'pr':pr}
    return render(request, 'ecomsite/home.html', params)

def register(request):
    error={}
    if request.method == "POST":
        firstname = request.POST.get('firstname', '')
        lastname = request.POST.get('lastname', '')
        phone = request.POST.get('phone', '')
        password = request.POST.get('password', '')
        confirmpassword =request.POST.get('confirmpassword', '')
        if password != confirmpassword:
            error['error'] = 'Confirm Password did not match';
            return render(request, 'ecomsite/register.html', {'error': error})
        email = request.POST.get('email', '')
        streetaddress = request.POST.get('streetaddress', '')
        city = request.POST.get('city', '')
        postalcode = request.POST.get('postalcode', '')
        province = request.POST.get('province', '')
        country = request.POST.get('country', '')
        reg = RegisterUser(firstname=firstname,lastname=lastname,phone=phone,password=make_password(password), email=email,streetaddress=streetaddress, city=city,postalcode=postalcode,province=province,country=country)
        reg.save()
    return render(request,'ecomsite/register.html',{})

def login(request):
    print(request.session)
    if 'user_id' in request.session:
        return redirect('home')

    error = {}
    if request.method == 'POST':
        uname = request.POST.get('email')
        pwd = request.POST.get('password')
        try:
            check_user = RegisterUser.objects.get(email=uname)

            if check_user:
                print(check_user)
                if check_password(pwd, check_user.password):
                    request.session['user_id'] = check_user.r_id
                    request.session['user_name'] = check_user.firstname
                    return redirect('home')
                else:
                    error['error'] = 'Credentilas does not match';
                    return render(request, 'ecomsite/login.html', {'error': error})

            else:
                error['error'] = 'User not found';
                return render(request, 'ecomsite/login.html', {'error': error})
        except:
            error['error'] = 'User not found';
            return render(request, 'ecomsite/login.html', {'error': error})

    return render(request, 'ecomsite/login.html', {'error': error})


def logout(request):
    try:
        del request.session['user_id']
        del request.session['user_name']
    except Exception as e:
        print(e)
    return redirect('home')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        desc = request.POST.get('desc', '')
        cont = contactus(name=name, email=email, phone=phone, desc=desc)
        cont.save()
    return render(request, "ecomsite/contactus.html")

def about(request):
    os1 = ourstory.objects.all()
    w1 = whychooseus.objects.all()
    os2 = oursuppliers.objects.all()
    www = weworkwith.objects.all()
    mys = manageyoursec.objects.all()
    of = ourfleet.objects.all()
    rws = regionsweserver.objects.all()
    params={'os1':os1, 'w1':w1, 'os2':os2, 'www':www, 'mys':mys, 'of':of, 'rws':rws}
    return render(request, 'ecomsite/aboutus.html', params)

def product(request):
    hsp = homesoldproducts.objects.all()
    www = weworkwith.objects.all()
    mys = manageyoursec.objects.all()
    of = ourfleet.objects.all()
    rws = regionsweserver.objects.all()
    pr=products.objects.all()
    pc=ProductCategory.objects.all()
    pb=ProductBrand2.objects.all()
    sup=Suppliers.objects.all()
    params = {'hsp':hsp,'www': www, 'mys': mys, 'of': of, 'rws': rws, 'pr':pr,'pc':pc,'pb':pb,'sup':sup}
    return render(request, 'ecomsite/products.html', params)

def flashsale(request):
    hsp = homesoldproducts.objects.all()
    www = weworkwith.objects.all()
    mys = manageyoursec.objects.all()
    of = ourfleet.objects.all()
    rws = regionsweserver.objects.all()
    pr = products.objects.all()
    pc = ProductCategory.objects.all()
    pb = ProductBrand2.objects.all()
    sup = Suppliers.objects.all()
    params = {'hsp': hsp, 'www': www, 'mys': mys, 'of': of, 'rws': rws, 'pr': pr,'pc':pc,'pb':pb,'sup':sup}
    return render(request, 'ecomsite/flashsale.html', params)

def seasonalsale(request):
    hsp = homesoldproducts.objects.all()
    www = weworkwith.objects.all()
    mys = manageyoursec.objects.all()
    of = ourfleet.objects.all()
    rws = regionsweserver.objects.all()
    pr = products.objects.all()
    pc = ProductCategory.objects.all()
    pb = ProductBrand2.objects.all()
    sup = Suppliers.objects.all()
    params = {'hsp': hsp, 'www': www, 'mys': mys, 'of': of, 'rws': rws, 'pr': pr,'pb':pb,'pc':pc,'sup':sup}
    return render(request, 'ecomsite/seasonalpromotion.html', params)

def search(request):
    query=request.GET['query']
    prid=ProductCategory.objects.filter(name=query)
    allPosts= products.objects.filter(pr_category__in=prid)
    hsp = homesoldproducts.objects.all()
    www = weworkwith.objects.all()
    mys = manageyoursec.objects.all()
    of = ourfleet.objects.all()
    rws = regionsweserver.objects.all()
    pr = products.objects.all()
    pc = ProductCategory.objects.all()
    pb = ProductBrand2.objects.all()
    sup = Suppliers.objects.all()
    params = {'allposts': allPosts,'hsp': hsp, 'www': www, 'mys': mys, 'of': of, 'rws': rws, 'pr': pr,'pc':pc,'pb':pb,'sup':sup}
    return render(request, 'ecomsite/products.html', params)

def productdetail(request,id):
    print(id)
    plist = products.objects.all()
    a=products.objects.filter(pr_id=id)
    p = {'plist': plist,'id':id,'a':a}
    return render(request,'ecomsite/productdetail.html',p)

def cart(request):
    cart_items = []
    sub_total = 0
    total_quantity=0
    sess = request.session['user_id']
    result = Cart.objects.filter(user_id=sess).values('product_id', 'quantity', 'id', 'user_id')
    for row in result:
        product_info_object = products.objects.filter(pr_id=row['product_id']).values('pr_title','pr_price','pr_image')
        product_info = product_info_object[0]
        cart_item = {'id': row['id'], 'product_name': product_info['pr_title'], 'quantity': row['quantity'],
                     'product_price': product_info['pr_price'],
                     'total_price': float(row['quantity']) * float(product_info['pr_price']),
                     'product_image': product_info['pr_image']}
        cart_items.append(cart_item)
        sub_total=sub_total + float(row['quantity']) * float(product_info['pr_price'])
        total_quantity=total_quantity+int(cart_item['quantity'])

    rounded_sub_total="{:.2f}".format(sub_total)
    if request.method == "POST":
        for up_item in cart_items:
            updated_quantity = request.POST.get('item_' + str(up_item['id']))
            Update_cart = Cart.objects.get(id=up_item['id'])
            Update_cart.quantity = updated_quantity
            Update_cart.save()
        return redirect('cart')


    plist={'cart_items':cart_items,'rounded_sub_total':rounded_sub_total,'total_quantity':total_quantity}


    return render(request,'ecomsite/cart.html',plist)

def cart_info(request):
    sub_total = 0
    total_quantity=0
    sess = request.session['user_id']
    result = Cart.objects.filter(user_id=sess).values('product_id', 'quantity', 'id', 'user_id')
    for row in result:
        product_info_object = products.objects.filter(pr_id=row['product_id']).values('pr_title','pr_price','pr_image')
        product_info = product_info_object[0]

        sub_total=sub_total + float(row['quantity']) * float(product_info['pr_price'])
        total_quantity=total_quantity+int(row['quantity'])

    rounded_sub_total="{:.2f}".format(sub_total)
    plist={'sub_total':rounded_sub_total,'total_qty':total_quantity}

    return JsonResponse({'error': True, 'msg': 'Success','data':plist});


def compare(request):
        list = json.loads(request.POST['products'])
        list2 = []
        for i in range(len(list)-1):
            t = int(list[i])
            if len(list2)<3:
                list2.append(t)
            else:
                list2.pop(0)
                list2.append(t)
        rlist=list2[::-1]
        print(rlist)


        plist = products.objects.filter(pr_id__in=rlist)

        p = { 'plist': plist}

        list = json.loads(request.POST['products'])
        return render(request, 'ecomsite/recent_products.html', p)

def add_to_cart(request):
    product_id = json.loads(request.POST['product_id'])
    user = json.loads(request.POST['user'])
    result = Cart.objects.filter(user_id=user,product_id=product_id).values('id','user_id','product_id')
    if result.exists():
        cart_value =list(result)[0]
        Update_cart = Cart.objects.get(id=cart_value['id'])
        Update_cart.quantity = int(Update_cart.quantity) + 1
        Update_cart.save()
    else:
        cart=Cart(user_id=user,product_id=product_id,quantity=1)
        cart.save()
    return JsonResponse({'error': True, 'msg': 'Success'});

def delete_crt_item(request,id):

    result = Cart.objects.filter(id=id)
    result.delete()
    return redirect('cart')



def wish(request):
    wish_items = []
    sub_total = 0
    total_quantity=0
    sess = request.session['user_id']
    result = Wish.objects.filter(user_id=sess).values('product_id', 'quantity', 'id', 'user_id')
    for row in result:
        product_info_object = products.objects.filter(pr_id=row['product_id']).values('pr_title','pr_price','pr_image')
        product_info = product_info_object[0]
        Wish_item = {'id': row['id'], 'product_name': product_info['pr_title'], 'quantity': row['quantity'],
                     'product_price': product_info['pr_price'],
                     'total_price': float(row['quantity']) * float(product_info['pr_price']),
                     'product_image': product_info['pr_image']}
        wish_items.append(Wish_item)
        sub_total=sub_total + float(row['quantity']) * float(product_info['pr_price'])
        total_quantity=total_quantity+int(Wish_item['quantity'])

    rounded_sub_total="{:.2f}".format(sub_total)
    if request.method == "POST":
        for up_item in wish_items:
            updated_quantity = request.POST.get('item_' + str(up_item['id']))
            Update_cart = Cart.objects.get(id=up_item['id'])
            Update_cart.quantity = updated_quantity
            Update_cart.save()
        return redirect('wish')
    plist = {'cart_items': wish_items, 'rounded_sub_total': rounded_sub_total, 'total_quantity': total_quantity}

    return render(request, 'ecomsite/wish.html', plist)



def add_to_wish(request):
    product_id = json.loads(request.POST['product_id'])
    user = json.loads(request.POST['user'])
    result = Wish.objects.filter(user_id=user,product_id=product_id).values('id','user_id','product_id')
    if result.exists():
        cart_value =list(result)[0]
        Update_cart = Wish.objects.get(id=cart_value['id'])
        Update_cart.quantity = int(Update_cart.quantity) + 1
        Update_cart.save()
    else:
        cart=Wish(user_id=user,product_id=product_id,quantity=1)
        cart.save()
    return JsonResponse({'error': True, 'msg': 'Success'});



def delete_list_item(request,id):

    result = Wish.objects.filter(id=id)
    result.delete()
    return redirect('wish')

def delete_list(request):
    ids = request.session['user_id']
    print(ids)
    result = Wish.objects.filter(user_id=ids)
    result.delete()
    print(result)
    return redirect('wish')

def delete_cart(request):
    ids = request.session['user_id']
    print(ids)
    result = Cart.objects.filter(user_id=ids)
    result.delete()
    print(result)
    return redirect('cart')