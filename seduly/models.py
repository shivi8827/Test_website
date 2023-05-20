from django.db import models
#S


class metric(models.Model):
    

    #id = models.IntegerField(dprimary_key=True, efault=0) 
    time = models.DateTimeField(default=0)
    voltage = models.IntegerField(default=0) 
    current = models.IntegerField(default=0) 





