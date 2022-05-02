import os
from django.db import models
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _

User = get_user_model()

def rename_img_video(instance, filename):
    ext = filename.split('.')[-1]
    filename += f"{instance.date_updated}"
    if ext.lower() in ['.png', '.jpg', '.gif']:
        return os.path.join(f'{instance.user.first_name}/image_post', filename)
    return os.path.join(f'{instance.user.first_name}/video_post', filename)


class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post')
    message = models.TextField(_("message"), blank=True)
    video = models.ImageField(_("video"), upload_to=rename_img_video, blank=True, null=True)
    img = models.ImageField(_("image"), upload_to=rename_img_video, blank=True, null=True)
    date_created = models.DateTimeField(_("date created"), auto_now_add=True)
    date_updated = models.DateTimeField(_("date updated"), auto_now=True)

    
    def __str__(self):
        return f"{self.post} - {self.user.first_name}"
    
    def save(self, *args, **kwargs):
        # self.slug = slugify(self.title)
        super().save(*args, **kwargs)
    
    class Meta:
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')

# class Liker(models.Model):
#     user = models.ManyToManyField(User, on_delete=models.CASCADE, related_name='user_like')
#     liker = models.ForeignKey(_("liker"), blank=True)
#     count_like = models.IntegerField(_("count like"), default=0)