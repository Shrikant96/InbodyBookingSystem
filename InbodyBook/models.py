from django.db import models
from django.db.models.fields import CharField
from django.db.models.query_utils import RegisterLookupMixin

# Create your models here.

# ***** Region *****
class IndiaRegions(models.Model):
    region = models.CharField(max_length=20)

    def __str__(self):
        return self.region

# ***** User Model *****
class InbodyUser(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=254)
    mobile = models.BigIntegerField()
    
    def __str__(self):
        return self.name

# ***** Meachine Model *****
class Machine(models.Model):
    meachine_name = models.CharField(max_length=20)
    booked = models.BooleanField(default=False)
    # **** Relationship ****
    region = models.ForeignKey(IndiaRegions, on_delete=models.CASCADE)
    qr_code = models.ImageField(upload_to='images/machine_qr_code',default="non.png")

    def __str__(self):
        return self.meachine_name

# ***** Institution Model *****
class Institution(models.Model):
 
    institution_name=models.CharField(max_length=100)
    client_name = models.CharField(max_length=100)
    client_mobile = models.BigIntegerField()
    client_email = models.EmailField(max_length=254, blank=True, null=True)
    city =  models.CharField(max_length=20)
    state = models.CharField(max_length=30)
    addr1 = models.CharField(max_length=100)
    addr2 = models.CharField(max_length=100, null=True, blank=True)
    zip_code = models.IntegerField()
    # region = models.CharField(max_length=20)
    start_date = models.DateField()
    end_date = models.DateField()
    demo_meachine = models.CharField(max_length=50)
    # *** Relationships keys ***
    inbodyUser = models.ForeignKey(InbodyUser, on_delete=models.CASCADE)
    meachine_name = models.ForeignKey(Machine,on_delete=models.CASCADE)

    def __str__(self):
        return self.institution_name


