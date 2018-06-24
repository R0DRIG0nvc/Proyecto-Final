from django.contrib import admin
from distribute.models import Send
# Register your models here.


@admin.register(Send)
class SendAdmin(admin.ModelAdmin):
    pass
