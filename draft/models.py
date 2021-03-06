from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User


# Create your models here.

def directory_path_by_user(instance , filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    now = timezone.now()
    return '{0}/user_{1}/{2}'.format(now.strftime('%Y%m') , instance.user_id.id , filename)

class Draft(models.Model):
    title = models.CharField(max_length=200)
    created_dt = models.DateTimeField(default=timezone.now)
    last_modified_dt = models.DateTimeField(default=timezone.now)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    
class DraftResume(models.Model):
    draft_id = models.ForeignKey(Draft , on_delete=models.CASCADE , default=None)
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    created_dt = models.DateTimeField(default=timezone.now)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

class DraftPortfolio(models.Model):
    draft_id = models.ForeignKey(Draft , on_delete=models.CASCADE )
    title = models.CharField(max_length=200)
    desc = models.TextField(max_length=2000)
    
    # 0 : links , 1 : files , 2 : videos
    portfolio_type = models.IntegerField()
    attached_link = models.TextField(blank=True , max_length=1000)
    attached_file = models.FileField(blank=True , upload_to=directory_path_by_user)
    attached_video_tag = models.TextField(blank=True , max_length=1000)

    created_dt = models.DateTimeField(default=timezone.now)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

class DraftActivity(models.Model):
    draft_id = models.ForeignKey(Draft , on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    desc = models.TextField(max_length=2000)

    # 추가 내용
    activity_dt = models.DateField()

    created_dt = models.DateTimeField(default=timezone.now)
    user_id = models.ForeignKey(User , on_delete = models.CASCADE)


