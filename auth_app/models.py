from django.db import models


# Create your models here.
class CallTouchModel(models.Model):
    name = models.CharField(auto_created='CallTouch', max_length=50, default='CallTouch')
    ct_node = models.CharField(max_length=150)
    ct_token = models.CharField(max_length=150)
    ct_cabinet_id = models.IntegerField()
    ct_created_date = models.DateField(auto_now=True)
    ct_user_id = models.IntegerField(default=0)
    ct_start_date = models.CharField(max_length=50)
    ct_days_back = models.IntegerField()


class LinksToCheck(models.Model):
    links_original_link = models.CharField(max_length=150)
    links_upload_date = models.DateField(auto_now=True)
    links_user_id = models.IntegerField(default=0)


class LinksCheckResult(models.Model):
    user_id = models.IntegerField(default=0)
    upload_date = models.DateField(auto_now=True)
    original_link = models.CharField(max_length=150)
    original_link_status_code = models.CharField(max_length=50)
    redirect_link = models.CharField(max_length=150)
    redirect_link_status_code = models.CharField(max_length=50)
    history = models.CharField(max_length=150)
    history_check_date = models.CharField(max_length=150)
