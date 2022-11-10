from unicodedata import name
from django.urls import  path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.index_nin, name="index_nin"),
    path('profile',views.Profile, name="profile"),
    path('tin',views.tin, name="tin"),
    path('vnin',views.basics, name="vnin"),
    path('general',views.my_portal, name="my_portal"),
    path('v_by_ninw',views.v_by_ninw, name="v_by_ninw"),
    path('v_by_phone',views.v_by_phone, name="v_by_phone"),
    path('v_by_vnin',views.v_by_vnin, name='v_by_vnin'),
    path('wallet',views.wallet, name="wallet"),
    path('voters',views.voters, name="voters"),
    path('bvn',views.bvn, name='bvn'),
    path('dashboard',views.dashboard, name="dashboard"),
    path('int_pass',views.int_pass, name="int_pass"),
    path('bbm',views.bbm, name='bbm'),
    path('admin/', admin.site.urls),
    path('<str:ref>', views.verify_payment, name = "verify-payment"),
    path('slip/',views.pdf, name="slip"),
    
    
]