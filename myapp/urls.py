from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    path("", views.index, name='index'),

    #path("logout", views.logout_admin, name="logout_admin"),

    #path("admin_login", views.index1, name="login"),

    path("appointment", views.appointment, name='appointment'),

    path("login", views.login1, name="login"),
    #path("logout", views.handleLogout, name='handleLogout'),
    path("index1", views.index1, name='home'),

    path("view_doctor", views.view_doctor, name='view_doctor'),
    path("add_doctor", views.Add_Doctor, name='add_doctor'),
    path("delete_doctor(?P<int:pid>)", views.Delete_Doctor, name='delete_doctor'),

    path("view_patient", views.view_patient, name='view_patient'),
    path("add_patient", views.Add_Patient, name='add_patient'),
    path("delete_patient(?P<int:pid>)", views.Delete_Patient, name='delete_patient'),

    path("view_appointment", views.view_appointment, name='view_appointment'),
    path("add_appointment", views.Add_Appointment, name='add_appointment'),
    path("delete_appointment(?P<int:pid>)", views.Delete_Appointment, name='delete_appointment'),




    path("facilities", views.facilities, name="facilities"),
    path("contact", views.contact, name="contact"),


]