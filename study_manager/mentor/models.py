from django.db import models
from member.models import Members

class Mentor(models.Model):
    member_id=models.OneToOneField(Members, on_delete=models.CASCADE,related_name="mentor")
    date_employment=models.DateField(auto_now_add=True)
    salary=models.IntegerField()
