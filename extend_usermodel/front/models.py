from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Person(User):
    class Meta:
        proxy = True

    @classmethod
    def get_blacklist(cls):
        return cls.objects.filter(is_active=False).all()



class UserExtension(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE,related_name='extension')
    phone = models.CharField(max_length=100)
    school = models.CharField(max_length=100,null=True,blank=True)


from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save,sender=User)
def handle_user_extension(sender,instance,created,**kwargs):
    if created:
        UserExtension.objects.create(user=instance)
        print('create_success')
    else:
        instance.extension.save()
        print('extension save')