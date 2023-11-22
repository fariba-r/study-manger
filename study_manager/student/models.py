from django.db import models
from mentor.models import Mentor
from member.models import Members

class student(models.Model):
    member_id=models.OneToOneField(Members,on_delete=models.CASCADE,related_name="student")
    mentor_id=models.ForeignKey(Mentor, on_delete=models.CASCADE,related_name="student",blank=True)
    GRADE=[
        ("thenth","10"),
        ("eleventh","11"),
        ("towelveth","12")
    ]
    grade=models.CharField(choices=GRADE,max_length=9)

