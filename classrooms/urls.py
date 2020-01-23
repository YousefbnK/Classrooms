
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from classes import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('classrooms/', views.classroom_list, name='classroom-list'),
    path('classrooms/<int:classroom_id>/', views.classroom_detail, name='classroom-detail'),

    path('classrooms/create', views.classroom_create, name='classroom-create'),
    path('classrooms/<int:classroom_id>/update/', views.classroom_update, name='classroom-update'),
    path('classrooms/<int:classroom_id>/delete/', views.classroom_delete, name='classroom-delete'),
    path('signup/', views.classroom_signup, name='signup'),
    path('signin/', views.classroom_signin, name='signin'),
    path('signout/', views.classroom_signout, name='signout'),
    path('classrooms/<int:classroom_id>/addstudent/', views.student_create, name='student-create'),
    path('classrooms/<int:student_id>/updatestudent/', views.student_update, name='student-update'),
    path('classrooms/<int:student_id>/deletestudent/', views.student_delete, name='student-delete'),

]

if settings.DEBUG:
	urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
