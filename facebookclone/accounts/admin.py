from django.contrib import admin
from .models import Profile

# 데이터 베이스의 내용을 다룰 수 있는 툴

#데코레이터

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
  list_display = ['id', 'nickname', 'user']
  list_display_links = ['nickname', 'user']
  search_fields = ['nickname']