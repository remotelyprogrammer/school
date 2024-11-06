from . import views
from django.urls import path

app_name = 'students'

urlpatterns = [
    path('create/', views.CreateStudentView.as_view(), name='create-student'),
    path('', views.home, name='student-home'),
    path('<int:student_id>/address/', views.add_or_update_address, name='add_or_update_address'),
    path('<int:student_id>/', views.student_detail, name='student_detail'),
    path('<int:student_id>/contacts/add/', views.AddContactView.as_view(), name='add_contact'),

]