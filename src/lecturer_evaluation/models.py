from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save

# Create your models here.

class Student(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=30)

    class meta:
        db_table = "students"
        verbose_name_plural = "students"
        verbose_name_plural = "students"

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # class Meta:
    #     app_label = 'app_auth'
    #     db_table = "app_user"

    def __str__(self):
        return self.user.username

def create_profile(sender, **kwargs):
    if kwargs['created']:
        user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)


class Lecturer(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return '%s %s' % (self.first_name, self.last_name)

    class meta:
        db_table = "lecturers"
        verbose_name = "lecturers"
        verbose_name_plural = "lecturers"


class Unit(models.Model):
    code = models.CharField(max_length=30)
    name = models.CharField(max_length=30)

    def __str__(self):
        return '%s %s' % (self.code, self.name)

    class meta:
        db_table = "units"
        verbose_name_plural = "units"
        verbose_name = "units"


class RegisteredUnit(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE, default=None)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, default=None)

    def __str__(self):
        return '%s %s %s' % (self.student, self.lecturer, self.unit)

    class meta:
        verbose_name = "registered_units"
        verbose_name_plural = "registered_units"
        db_table = "registered_units"



class Lecturer_Evaluated(models.Model):
    name = models.CharField(max_length=30)
    student= models.ForeignKey(User, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class meta:
        verbose_name = "lecturer_evaluated"
        db_table = "lecturer_evaluated"
        verbose_name_plural = "lecturer_evaluated"



class SectionOne(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE, default=None)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, default=None)
    q1 = models.CharField(max_length=5)
    q2 = models.CharField(max_length=5)
    q3 = models.CharField(max_length=5)

    class meta:
        verbose_name = "section_one"
        verbose_name_plural = "section_one"
        db_table = "section_one"
# 
    # def __str__(self):
    #   return self.lecturer

class SectionTwo(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    lecturer = models.ForeignKey(Lecturer, on_delete=models.CASCADE)
    unit = models.ForeignKey(Unit, on_delete=models.CASCADE, default=None)
    q1 = models.IntegerField()
    q2 = models.IntegerField()
    q3 = models.IntegerField()
    q4 = models.IntegerField()
    q5 = models.IntegerField()
    q6 = models.IntegerField()
    q7 = models.IntegerField()
    q8 = models.IntegerField()
    q9 = models.IntegerField()
    q10 = models.IntegerField()
    q11 = models.IntegerField()
    q12 = models.IntegerField()

    class meta:
        verbose_name = "section_two"
        verbose_name_plural = "section_two"
        db_table = "section_two"


class SectionThree(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    q1 = models.IntegerField()
    q2 = models.IntegerField()
    q3 = models.IntegerField()
    q4 = models.IntegerField()
    q5 = models.IntegerField()
    q6 = models.IntegerField()
    q7 = models.IntegerField()
    
    class meta:
        verbose_name = "section_three"
        verbose_name_plural = "section_three"
        db_table = "section_three"


class SectionFour(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    item = models.CharField(max_length=20, default=None)
    q1 = models.CharField(max_length=500)
    q2 = models.CharField(max_length=500)
        
    class meta:
        verbose_name = "section_four"
        verbose_name_plural = "section_four"
        db_table = "section_four"



class SectionFive(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    improvement = models.CharField(max_length=500)
            
    class meta:
        verbose_name = "section_five"
        verbose_name_plural = "section_fsive"
        db_table = "section_five"

