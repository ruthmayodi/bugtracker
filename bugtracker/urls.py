"""bugtracker URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from homepage import views

urlpatterns = [
    path('', views.index_view, name='home'),
    path('new_ticket/', views.add_ticket_view),
    path('ticket_view/<int:ticket_id>/', views.ticket_view, name='ticketView'),
    path('user_view/<int:user_id>/', views.user_view),
    path('edit_ticket/<int:ticket_id>/', views.edit_ticket_view),
    path('assign_ticket/<int:ticket_id>/', views.assign_ticket_view),
    path('complete_ticket/<int:ticket_id>/', views.complete_ticket_view),
    path('invalid_ticket/<int:ticket_id>/', views.invalid_ticket_view),
    path('return_ticket/<int:ticket_id>/', views.return_ticket_view),
    path('reopen_ticket/<int:ticket_id>/', views.reopen_ticket_view),
    path('login/', views.login_view),
    path('logout/', views.logout_view),
    path('admin/', admin.site.urls),

]
