# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AccountAccount(models.Model):
    openid = models.CharField(max_length=30, blank=True, null=True)
    create_time = models.DateTimeField()
    active_ip = models.CharField(max_length=30, blank=True, null=True)
    active_time = models.DateTimeField(blank=True, null=True)
    nickname = models.CharField(max_length=30)
    headimgurl = models.CharField(max_length=255)
    sex = models.CharField(max_length=1)
    country = models.CharField(max_length=30)
    province = models.CharField(max_length=30)
    city = models.CharField(max_length=30)
    telephone = models.CharField(max_length=11, blank=True, null=True)
    status = models.CharField(max_length=10)
    subscribed = models.IntegerField()
    introduction = models.CharField(max_length=1024)
    role = models.CharField(max_length=15)
    unionid = models.CharField(unique=True, max_length=64, blank=True, null=True)
    is_robot = models.IntegerField()
    address = models.CharField(max_length=300)
    is_vip = models.IntegerField()
    mobile_openid = models.CharField(max_length=30, blank=True, null=True)
    name = models.CharField(max_length=30)
    pc_openid = models.CharField(max_length=30, blank=True, null=True)
    device_token = models.CharField(max_length=100, blank=True, null=True)
    wechat = models.CharField(max_length=100, blank=True, null=True)
    wxa_openid = models.CharField(max_length=30, blank=True, null=True)
    register_source = models.CharField(max_length=10)
    webo_uid = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'account_account'

    def start(self):
        self.subscribed = 0
