from django.urls import path
from . import views
from django.conf.urls import include
from django.contrib import admin

app_name = 'account'

urlpatterns = [
	# post views
	# path('admin/', admin.site.urls),
	# path('account/', include('account.urls')),
	# path('login/', views.user_login, name='login'),
	path('login/', views.user_login, name='login'),
]