import os
from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _

User = get_user_model()

def rename_img(instance, filename):
    upload_to = 'image_profile'
    ext = filename.split('.')[-1]
    filename = f"{instance.user.first_name}_{instance.user.pk}_{instance.date_updated}.{ext}"
    return os.path.join(upload_to, filename)

def pseudo_rename(instance, filename):
    upload_to = 'image_profile'
    ext = filename.split('.')[-1]
    filename = f"{instance.user.first_name}_{instance.user.pk}_{instance.date_updated}.{ext}"
    return os.path.join(upload_to, filename)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    pseudo = models.CharField(max_length=20, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    img_profile = models.ImageField(_("image profile"), upload_to=rename_img, blank=True, null=True)
    birth_date = models.DateField(_("birth date"), null=True, blank=True)
    gender = models.CharField(_("gender"), max_length=15, choices=(('M', 'Male'), ('F', 'Female')))
    adress = models.CharField(_("adress"),max_length=30, blank=True)
    town = models.CharField(_("town"),max_length=30, blank=True)
    country = models.CharField(_("country"), max_length=30, blank=True)
    description = models.TextField(_("description"), blank=True)
    link_linkedin = models.CharField(_("linkedin profile link"), max_length=5000)
    link_gitthub = models.CharField(_("gitthub profile link"), max_length=5000)
    link_twitter = models.CharField(_("twitter profile link"), max_length=5000)
    link_mysite = models.CharField(_("mysite link"), max_length=5000)
    date_updated = models.DateTimeField(_("date updated"), auto_now=True)
    
    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
    
    class Meta:
        verbose_name = _('Profile')
        verbose_name_plural = _('Profiles')
    
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()