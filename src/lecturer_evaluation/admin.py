from django.contrib import admin

# Register your models here.
from .models import Student, Lecturer, Unit, SectionOne,SectionTwo, SectionThree, SectionFour, Lecturer_Evaluated, SectionFive, RegisteredUnit, UserProfile

admin.site.register(Student)
admin.site.register(UserProfile)
admin.site.register(Lecturer)
admin.site.register(Unit)
admin.site.register(SectionOne)
admin.site.register(SectionTwo)
admin.site.register(SectionThree)
admin.site.register(SectionFour)
admin.site.register(SectionFive)
admin.site.register(Lecturer_Evaluated)
admin.site.register(RegisteredUnit)
