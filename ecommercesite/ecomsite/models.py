from django.db import models

# Create your models here.



class C1(models.Model):
    c_id=models.AutoField(primary_key=True)
    car_name=models.CharField(max_length=50)
    curcive_text=models.CharField(max_length=50)
    bold_text=models.CharField(max_length=50)
    big_bold_text=models.CharField(max_length=50)
    since_date=models.CharField(max_length=50)
    carousal_link=models.CharField(max_length=50)
    carousal_image=models.ImageField(upload_to="ecomsite/images",default="")
    def __str__(self):
        return self.car_name

class ourstory(models.Model):
    ostory_id=models.AutoField(primary_key=True)
    ostory_curcive_text=models.CharField(max_length=50)
    ostory_bold_text=models.CharField(max_length=50)
    ostory_p1=models.CharField(max_length=200)
    ostory_p2=models.CharField(max_length=200)
    ostory_link = models.CharField(max_length=50)
    def __str__(self):
        return self.ostory_bold_text

class whychooseus(models.Model):
    wcu_id=models.AutoField(primary_key=True)
    wcu_image = models.ImageField(upload_to="ecomsite/images", default="")
    wcu_title=models.CharField(max_length=100)
    wcu_subtitle=models.CharField(max_length=100)
    wcu_p=models.CharField(max_length=200)

    def __str__(self):
        return self.wcu_title

class oursuppliers(models.Model):
    osuppliers_id=models.AutoField(primary_key=True)
    osuppliers_title = models.CharField(max_length=100, default="")
    osuppliers_image = models.ImageField(upload_to="ecomsite/images", default="")

    def __str__(self):
        return self.osuppliers_title


class homesoldproducts(models.Model):
    hsp_id=models.AutoField(primary_key=True)
    hsp_curcive_text = models.CharField(max_length=50)
    hsp_title1 = models.CharField(max_length=100, default="")
    hsp_title2 = models.CharField(max_length=100, default="")
    hsp_subtitle = models.CharField(max_length=100, default="")
    hsp_image = models.ImageField(upload_to="ecomsite/images", default="")

    def __str__(self):
        return self.hsp_title1

class weworkwith(models.Model):
    www_id=models.AutoField(primary_key=True)
    www_title = models.CharField(max_length=100, default="")
    www_image = models.ImageField(upload_to="ecomsite/images", default="")

    def __str__(self):
        return self.www_title

class manageyoursec(models.Model):
    mys_id=models.AutoField(primary_key=True)
    mys_title = models.CharField(max_length=100, default="")
    mys_icon1 = models.ImageField(upload_to="ecomsite/images", default="")
    mys_icon2 =models.ImageField(upload_to="ecomsite/images", default="")
    mys_icon3 = models.ImageField(upload_to="ecomsite/images", default="")
    mys_image = models.ImageField(upload_to="ecomsite/images", default="")

    def __str__(self):
        return self.mys_title

class ourfleet(models.Model):
    of_id=models.AutoField(primary_key=True)
    of_title = models.CharField(max_length=100, default="")
    of_desc1 = models.TextField()
    of_desc2 = models.TextField()
    of_link = models.CharField(max_length=50)


    def __str__(self):
        return self.of_title

class regionsweserver(models.Model):
    rws_id=models.AutoField(primary_key=True)
    rws_title = models.CharField(max_length=100, default="")
    rws_p1 = models.TextField()
    rws_p2 = models.TextField()
    rws_link = models.CharField(max_length=50)
    rws_image = models.ImageField(upload_to="ecomsite/images", default="")


    def __str__(self):
        return self.rws_title

class RegisterUser(models.Model):
    r_id=models.AutoField(primary_key=True)
    firstname= models.CharField(max_length=100, default="")
    lastname= models.CharField(max_length=100, default="")
    phone= models.CharField(max_length=100, default="")
    password= models.CharField(max_length=100, default="")
    confirmpassword= models.CharField(max_length=100, default="")
    email= models.CharField(max_length=100, default="")
    streetaddress= models.CharField(max_length=200, default="")
    city= models.CharField(max_length=100, default="")
    postalcode= models.CharField(max_length=100, default="")
    province= models.CharField(max_length=100, default="")
    country= models.CharField(max_length=100, default="")
    streetaddress1= models.CharField(max_length=200, default="")
    city1= models.CharField(max_length=100, default="")
    postalcode1= models.CharField(max_length=100, default="")
    province1= models.CharField(max_length=100, default="")
    country1= models.CharField(max_length=100, default="")


    def __str__(self):
        return self.firstname


class contactus(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=70, default="")
    phone = models.CharField(max_length=70, default="")
    desc = models.CharField(max_length=500, default="")

    def __str__(self):
        return self.name

class ProductCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class ProductBrand(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Suppliers(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class products(models.Model):
    pr_id=models.AutoField(primary_key=True)
    pr_title = models.CharField(max_length=100, default="")
    pr_category = models.ForeignKey('ProductCategory', on_delete=models.PROTECT)
    pr_brn = models.ForeignKey('ProductBrand2', on_delete=models.CASCADE, null=True)
    pr_supplier = models.ForeignKey('Suppliers', on_delete=models.CASCADE, null=True)
    pr_price = models.CharField(max_length=100, default="7.99")
    pr_desc = models.TextField()
    pr_detail = models.TextField(default="Lorem ipsum dolor sit amet, consectetuer adipiscing elit, sed diam non ummy nibh euismod tincidunt ut laoreet dolore magna aliquam eratv olu tpat. Ut wisi enim ad minim veniam lorem ipsum dolor sit amet, con sect etuer adipiscing elit, sed diam nonummy.")
    flash_sale=models.BooleanField(default=False)
    seasonal_sale=models.BooleanField(default=False)
    show_on_home=models.BooleanField(default=False)
    pr_image = models.ImageField(upload_to="ecomsite/images", default="")


    def __str__(self):
        return self.pr_title

class ProductBrand2(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name



class Cart(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=100, default="")
    product_id = models.CharField(max_length=100, default="")
    quantity = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.user_id


class Wish(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=100, default="")
    product_id = models.CharField(max_length=100, default="")
    quantity = models.CharField(max_length=100, default="")

    def __str__(self):
        return self.user_id
