from django.contrib import admin
from django.urls import path
from Quiz.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home,name='home'),
    path('addQuestion/', addQuestion,name='addQuestion'),
    path('addQuizz', addQuizz,name='addQuizz/'),
    path('login/', loginPage,name='login'),
    path('logout/', logoutPage,name='logout'),
    path('register/', registerPage,name='register'),

]
urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
