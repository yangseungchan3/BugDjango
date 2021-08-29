from django.contrib import admin

# Register your models here.
from .models import UserInfo,Board,Photo

admin.site.register(UserInfo)
admin.site.register(Board)
admin.site.register(Photo)