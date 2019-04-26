from django.http import HttpResponse
from django.http import HttpResponseRedirect 
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import auth 
from django.template.context_processors import csrf 
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages 
from .models import Lecturer, Unit, SectionOne, SectionTwo, SectionThree, SectionFour, SectionFive, Lecturer_Evaluated, RegisteredUnit
from django.contrib.auth.models import User



# from django.models import Student

# Create your views here.
def home_view(request, *args, **kwargs):
	return render(request, "home.html", {})

def evaluate_view(request, *args, **kwargs):
	if request.user.is_authenticated:
		return render(request, "evaluate.html", context={"registered_units": RegisteredUnit.objects.all().order_by(
     'id', 'lecturer', 'lecturer_id', 'student', 'student_id', 'unit', 'unit_id')})
	else:
		return render(request, "login.html")


def evaluate_section_ii_view(request, *args, **kwargs):
	if request.user.is_authenticated:
		return render(request, "evaluate-section-ii.html", {})
	else:
		return render(request, "login.html")

def evaluate_section_iii_view(request, *args, **kwargs):
	if request.user.is_authenticated:
		return render(request, "evaluate-section-iii.html", {})
	else:
		return render(request, "login.html")

def evaluate_section_iv_view(request, *args, **kwargs):
	return render(request, "evaluate-section-iv.html", {})

def student_login_view(request, *args, **kwargs):
	c = {}
	c.update(csrf(request))
	return render(request, "login.html", c)

def auth_view(request, *args, **kwargs):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, "Logged in successfully!")
				return redirect('../evaluate', {})
			else: 
				messages.error(request, f"Invalid Registration number or Password!")
				return redirect('../login')
		else:
				messages.error(request, f"Invalid Registration number or Password!")
				return redirect('../login')
	form = AuthenticationForm()
	return render(request, "login.html")




def section_one(request, *args, **kwargs):
	if request.method == "POST":
		unit_id_r = request.POST.get('unit')

		unit_id_r = unit_id_r.split('#')	

		unit_id = int(unit_id_r[0])
		lecturer_id = int(unit_id_r[1])
		lecturer = str(unit_id_r[2])

		# unit_id = 1
		# lecturer_id = 1
		# lecturer = "KATHRYNE KAREN"

		q1 = request.POST.get('section-1-a')
		q2 = request.POST.get('section-1-b')
		q3 = request.POST.get('section-1-c')

		# user = User.objects.get(id=user_id)
		# user = User.objects.get(username=request.user.username)
		login = request.user.id
		user = User.objects.get(id=login)
		unit = Unit.objects.get(id=unit_id)
		
		lec = Lecturer.objects.get(id=lecturer_id)
		
		section1a = Lecturer_Evaluated(name=lecturer, unit_id=unit, student_id=user)
		section1a.save()

		section1 = SectionOne(student=user, lecturer=lec, unit=unit, q1=q1, q2=q2, q3=q3)
		section1.save()

		return render(request, "evaluate-section-ii.html", context={"lecturer_id": lecturer_id, "unit_id": unit_id})
	else:
		return redirect('../../evaluate/')


def section_two(request, *args, **kwargs):
	if request.method == "POST":	
		lecturer_id = request.POST.get('lecturer_id')
		unit_id = request.POST.get('unit_id')	
		q1 = request.POST.get('section-2-a')
		q2 = request.POST.get('section-2-b')
		q3 = request.POST.get('section-2-c')
		q4 = request.POST.get('section-2-d')
		q5 = request.POST.get('section-2-e')
		q6 = request.POST.get('section-2-f')
		q7 = request.POST.get('section-2-g')
		q8 = request.POST.get('section-2-h')
		q9 = request.POST.get('section-2-i')
		q10 = request.POST.get('section-2-j')
		q11 = request.POST.get('section-2-k')
		q12 = request.POST.get('section-2-l')

		login = request.user.id
		user = User.objects.get(id=login)
		unit = Unit.objects.get(id=unit_id)
		lec = Lecturer.objects.get(id=lecturer_id)
		section2 = SectionTwo(student=user, lecturer=lec, unit=unit, q1=q1, q2=q2, q3=q3, q4=q4, q5=q5, q6=q6, q7=q7, q8=q8, q9=q9, q10=q10, q11=q11, q12=q12)
		section2.save()
		return render(request, "evaluate-section-iii.html", {})
	else:
		return redirect('../../evaluate/2')



def section_three(request, *args, **kwargs):
	if request.method == "POST":		
		q1 = request.POST.get('section-3-a')
		q2 = request.POST.get('section-3-b')
		q3 = request.POST.get('section-3-c')
		q4 = request.POST.get('section-3-d')
		q5 = request.POST.get('section-3-e')
		q6 = request.POST.get('section-3-f')
		q7 = request.POST.get('section-3-g')

		login = request.user.id
		user = User.objects.get(id=login)
	
		section3 = SectionThree(student=user, q1=q1, q2=q2, q3=q3, q4=q4, q5=q5, q6=q6, q7=q7)
		section3.save()
		return render(request, "evaluate-section-iv.html", {})
	else:
		return redirect('../../evaluate/3')



def section_four(request, *args, **kwargs):
	if request.method == "POST":		
		item1 = request.POST.get('Lecturer')
		item2 = request.POST.get('ICT')
		item3 = request.POST.get('Examination-Office')
		item4 = request.POST.get('Library')
		item5 = request.POST.get('comment')
		q1 = request.POST.get('library-comment-a')
		q2 = request.POST.get('library-comment-b')
		q3 = request.POST.get('ict-comment-a')
		q4 = request.POST.get('ict-comment-b')
		q5 = request.POST.get('exam-comment-a')
		q6 = request.POST.get('exam-comment-b')
		q7 = request.POST.get('lecturer-comment-a')
		q8 = request.POST.get('lecturer-comment-b')
		
		login = request.user.id
		user = User.objects.get(id=login)
	
		section4a = SectionFour(student=user, item=item1, q1=q7, q2=q8)
		section4b = SectionFour(student=user, item=item2, q1=q3, q2=q4)
		section4c = SectionFour(student=user, item=item3, q1=q5, q2=q6)
		section4d = SectionFour(student=user, item=item4, q1=q1, q2=q2)
		section4e = SectionFive(student=user, improvement=item5,)
		section4a.save()
		section4b.save()
		section4c.save()
		section4d.save()
		section4e.save()
		return render(request, "home.html", {})
	else:
		return redirect('../../evaluate/4')





def loggedin(request, *args, **kwargs):
	return render(request, "evaluate.html", {'full_name': request.user.regno})

def invalid_login(request, *args, **kwargs):
	return render(request, "login.html", {})

def logout_view(request, *args, **kwargs):
	logout(request)
	messages.info(request, "Logged out successfully!")
	return redirect("home")
	

