from django.urls import path
from accounts.views import adopt_or_get_involved, buy_medicine, login_page, logout, medicine_list, order_list, out_of_stock, purchase_success, volunteer_register
from accounts.views import register_page,activate_email
from accounts.views import adopter_register
# from products.views import

urlpatterns = [
     path('login/',login_page, name="login"),
     path('register/', register_page, name="register"),
     path('logout/',logout, name='logout'),
     path('activate/<email_token>/', activate_email, name="activate_email"),
     path('adopt/', adopt_or_get_involved, name="adopt_or_get_involved"),
     path('volunteer/register/', volunteer_register, name='volunteer_register'),
     path('adopter_register/', adopter_register, name='adopter_register'),
     path('medicines/', medicine_list, name='medicine_list'),
     path('medicines/buy/<int:medicine_id>/', buy_medicine, name='buy_medicine'),
     path('medicines/purchase-success/', purchase_success, name='purchase_success'),
     path('medicines/out-of-stock/', out_of_stock, name='out_of_stock'),
     path('orders/', order_list, name='order_list'),

]