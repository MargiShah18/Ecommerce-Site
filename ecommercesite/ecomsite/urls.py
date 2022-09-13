from django.urls import path
from .views import home, register,login,contact,about,product,flashsale,seasonalsale,search,productdetail,cart,compare
from . import views
urlpatterns = [
    path('', home, name='home'),
    path('register/',register, name="register"),
    path('login/',login, name="login"),
    path('contactus/',contact, name="contact"),
    path('aboutus/',about, name="about"),
    path('products/',product, name="product"),
    path('flashsale/',flashsale, name="flashsale"),
    path('seasonalpromotion/',seasonalsale, name="seasonalsale"),
    path('search/',search, name="search"),
    path('cart/',cart, name="cart"),
    path('wish/',views.wish, name="wish"),
    path('login/',views.login, name="login"),
    path('logout/',views.logout, name="logout"),
    path('productdetail/<int:id>',productdetail, name="productdetail"),
    path('productdetail/get_recent_products',compare, name="get_recent_products"),
    path('products/add_to_cart', views.add_to_cart, name='add_to_cart'),
    path('products/add_to_wish', views.add_to_wish, name='add_to_wish'),
    path('cart_info', views.cart_info, name='cart_info'),
    path('delete_crt_item/<int:id>', views.delete_crt_item, name='delete_crt_item'),
    path('delete_list_item/<int:id>', views.delete_list_item, name='delete_list_item'),
    path('delete_list/', views.delete_list, name='delete_list'),
    path('delete_cart/', views.delete_cart, name='delete_cart')
]