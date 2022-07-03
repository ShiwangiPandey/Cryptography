from django.db import models

# Create your models here.

class recieved_file(models.Model):
    file= models.FileField(upload_to='Files/',null=True,default=None)
    key=models.CharField(max_length=20,null=True,default=None)


class dfile(models.Model):
    dtext=models.FileField(upload_to='dec_files/',null=True,default=None)
    
    

