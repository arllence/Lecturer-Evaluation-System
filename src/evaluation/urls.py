"""evaluation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from lecturer_evaluation.views import home_view, evaluate_view, evaluate_section_ii_view, evaluate_section_iii_view, evaluate_section_iv_view, student_login_view, auth_view, loggedin, invalid_login, logout_view, section_one, section_two, section_three, section_four

#from my_app import views

app_name = "lecturer_eveluation"

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view, name='home'),

    path('evaluate/', evaluate_view, name='evaluate'),
    path('evaluate/2', evaluate_section_ii_view, name='evaluate-section-ii'),
    path('evaluate/3', evaluate_section_iii_view, name='evaluate-section-iii'),
    path('evaluate/4', evaluate_section_iv_view, name='evaluate-section-iv'),

    path('login/', student_login_view, name='student-login'),
    path('check/', auth_view, name='student-auth'),

    path('section/1', section_one, name='section-one'),
    path('section/2', section_two, name='section-two'),
    path('section/3', section_three, name='section-three'),
    path('section/4', section_four, name='section-four'),

    path('logged-in/', loggedin, name='student-logged-in'),
    path('invalid/', invalid_login, name='invalid-logged-in'),
    path('logout/', logout_view, name='student-logout'),
]
