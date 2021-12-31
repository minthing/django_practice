from django.db import models
from django.conf import settings
from imagekit.models import ProcessedImageField #이미지 처리 관련 기능
from imagekit.processors import ResizeToFill #이미지 사이즈 관련
import re #정규표현식

#image 확장자
def user_path(instance, fileName):
  from rendom import choice
  import choice
  arr = [choice(string.ascii_letters) for _ in range(8)]
  pid = ''.join(arr)
  extension = fileName.split('.')[-1]
  return 'accounts/{}/{}.{}'.format(instance.user.username, pid, extension)

class Profile(models.Model):
  user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
  nickname = models.CharField('nickname', max_length=30, unique=True)
  picture = ProcessedImageField(upload_to=user_path,processors=[ResizeToFill(150,150)],format='PNG',options={'quality':90},blank=True)
  about = models.CharField(max_length=100, blank=True)

  GENDER_C =(
    ('선택안함', '선택안함'),
    ('여성', '여성'),
    ('남성', '남성')
    )

  gender = models.CharField('gender', max_length=10, choices=GENDER_C, default = 'N')