from io import BytesIO

from PIL import Image
from django.core.files import File
from django.db import models
from django.conf import settings
import os
from pathlib import Path
import datetime
import random
from django.urls import reverse
from client.models import User
# from django.contrib.auth.models import User




def upload_file_name(instance, filename):
    _, ext = os.path.splitext(filename)
    return "{}/{:%Y-%m-%d-%H-%M-%S}-{}.{}".format(
        datetime.datetime.now().strftime("%Y%m"),
        datetime.datetime.now(), random.randint(1000, 9999), ext)

class Post(models.Model):
    user = models.ForeignKey(User,on_delete=models.RESTRICT)
    subject = models.CharField(max_length=50, blank=True)
    content = models.TextField()
    video = models.FileField(blank=True, null=True, upload_to=upload_file_name)
    shown = models.IntegerField(default=0)
    like = models.IntegerField(default=0)
    dislike = models.IntegerField(default=0)
    comment = models.CharField(max_length=200, blank=True)
    added_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

   

    
    @property
    def video_url(self):
        if self.video:
            return os.path.join(settings.MEDIA_URL, str(self.video))

        return Path(settings.STATIC_URL).joinpath("assets/no-video.jpg")


