from django.db import models
from student.models import student
from mentor.models import Mentor
# Create your models here.
class Tasks(models.Model):
    CATEGORY=[
        ("math","M"),
        ("physics","P"),
        ("chemist","CH"),
        ("lecture","L")
    ]
    categoy=models.CharField(choices=CATEGORY,max_length=50)
    student_id=models.ForeignKey(student,on_delete=models.CASCADE,blank=True,related_name="tasks")
    mentor_id=models.ForeignKey(Mentor,on_delete=models.CASCADE,blank=True,related_name="tasks")
    start_date=models.DateTimeField()
    finish_date=models.DateTimeField()
    definitoin=models.TextField(blank=True)
    situation=models.BooleanField(default=False)

