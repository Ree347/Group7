from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from django.contrib.auth import views as auth_view
from . import views
from .forms import LoginForm, MyPasswordResetForm


urlpatterns = [
    path('', views.home),
    path('about/', views.about, name="about"),
    path('contact/', views.contact, name="contact"),
    path("category/<slug:val>", views.CategoryView.as_view(), name="category"),
    path("category-title/<val>", views.CategoryTitle.as_view(), name="category-title"),
    path("productdetail/<int:pk>", views.ProductDetail.as_view(), name="productdetail"),
    path("profile/", views.ProfileView.as_view(), name="profile"),
    path("address/", views.address, name="address"),
    path('updateAddress/<int:pk>', views.updateAddress.as_view(), name='updateAddress'),
    path("refunds/", views.RequestRefundView.as_view(), name="refund" ),
    path('compare/', views.CompareProductView.as_view(), name='compare' ),
    
    path('add-to-cart/', views.add_to_cart, name='add-to-cart'),
    path('cart/', views.show_cart, name='showcart'),
    path('checkout/', views.checkout.as_view(), name='checkout'),
    path('paymentdone/', views.payment_done, name='paymentdone'),
    path('orders/', views.orders, name='orders'),
    

    path('pluscart/', views.plus_cart),
    path('minuscart/', views.minus_cart),
    path('removecart/', views.remove_cart),
    path('sell_add_item', views.seller_add_item, name='seller_add_item'),


    #login authentication
    path('registration/', views.CustomerRegistrationView.as_view(), name='customerregistration'),
    path('accounts/login/', auth_view.LoginView.as_view(template_name='app/login.html', authentication_form=LoginForm), name='login'),
    path('password-reset/', auth_view.PasswordResetView.as_view(template_name='app/password_reset.html', form_class=MyPasswordResetForm), name='password_reset'),
    path('logout/', auth_view.LogoutView.as_view(next_page='login'), name='logout'),
    
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
