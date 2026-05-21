from django.db import models
from django.contrib.auth.models import User

class Signup(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    mobile = models.CharField(max_length=20,null=True)
    image = models.FileField(null=True)
    gender = models.CharField(max_length=10,null=True)
    dob = models.CharField(max_length=10,null=True)
    address = models.CharField(max_length=50,null=True)
    def _str_(self):
        return self.user.username

class Feedback(models.Model):
    feedback_name = models.CharField(max_length=20,null=True)
    feedback_contact = models.CharField(max_length=30, null=True)
    feedback_email = models.CharField(max_length=10,null=True)
    feedback_comment = models.CharField(max_length=15,null=True)

class ParcelRequest(models.Model):
    first_name=models.CharField(max_length=40,null=True)
    last_name=models.CharField(max_length=40,null=True)
    email=models.CharField(max_length=40,null=True)
    mobile=models.CharField(max_length=40,null=True)
    parcel_type=models.CharField(max_length=40,null=True)
    request_date=models.CharField(max_length=50,null=True)
    gov_id=models.CharField(max_length=40,null=True)
    gov_no=models.CharField(max_length=40,null=True)
    weight=models.CharField(max_length=40,null=True)
    address=models.CharField(max_length=200,null=True)
    status=models.CharField(max_length=40,null=True)
    parcel_id=models.IntegerField(max_length=50,null=True)
    test=models.IntegerField(max_length=50,null=True)

class Receiver(models.Model):
    name=models.CharField(max_length=50,null=True)
    contact=models.CharField(max_length=50,null=True)
    pin=models.CharField(max_length=50,null=True)
    house=models.CharField(max_length=50,null=True)
    city=models.CharField(max_length=50,null=True)
    state=models.CharField(max_length=50,null=True)
    send_date=models.CharField(max_length=50,null=True)
    parcel_id=models.IntegerField(max_length=50,null=True)
    parcel_status=models.CharField(max_length=200,null=True)
    parcel_date=models.CharField(max_length=200,null=True)
    parcel_msg=models.CharField(max_length=200,null=True)

class Payment(models.Model):
    p_id = models.CharField(max_length=40,null=True)
    uname = models.CharField(max_length=40,null=True)
    uemail = models.CharField(max_length=40,null=True)
    contact = models.CharField(max_length=40,null=True)
    amount = models.CharField(max_length=40,null=True)
    dt = models.CharField(max_length=40,null=True)
    mode = models.CharField(max_length=40,null=True)
    cno = models.CharField(max_length=40,null=True)
    cdate = models.CharField(max_length=40,null=True)
    cvv = models.CharField(max_length=40,null=True)
    status = models.CharField(max_length=40,null=True)
