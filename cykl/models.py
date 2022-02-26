from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class cykl(models.Model):
    
    present_at=models.IntegerField(default=-1)
    use_date=models.IntegerField(default=0)
    in_time=models.IntegerField(default=-1)
    out_time=models.IntegerField(default=-1)
    no_rides=models.IntegerField(default=0)
    

    
