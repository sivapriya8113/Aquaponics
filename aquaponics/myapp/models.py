from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class registration(models.Model):
	user_id=models.ForeignKey(User,on_delete=models.CASCADE)
	user_name=models.CharField(max_length=200)
	user_email=models.CharField(max_length=200)
	user_phone=models.CharField(max_length=200)
	user_address=models.CharField(max_length=200)
	u_id=models.AutoField(primary_key=True)

class category(models.Model):
	cat_id=models.AutoField(primary_key=True)
	cat_name=models.CharField(max_length=200)
	cat_img=models.FileField(upload_to='media')

class product(models.Model):
	p_id=models.AutoField(primary_key=True)
	p_name=models.CharField(max_length=200)
	cat_id=models.ForeignKey(category,on_delete=models.CASCADE)
	p_desc=models.CharField(max_length=200)
	p_price=models.IntegerField()
	p_img=models.FileField(upload_to='media')
	user_id=models.FileField(upload_to='media')

class guideline(models.Model):
	g_id=models.AutoField(primary_key=True)
	g_name=models.CharField(max_length=200)
	g_desc=models.CharField(max_length=800)
	g_img=models.FileField(upload_to='media')

class comment(models.Model):
	c_id=models.AutoField(primary_key=True)
	c_uname=models.CharField(max_length=200)
	c_comment=models.CharField(max_length=800)
	c_reply=models.CharField(max_length=800)

class feedback(models.Model):
	f_id=models.AutoField(primary_key=True)
	f_uname=models.CharField(max_length=200)
	f_feedback=models.CharField(max_length=800)
