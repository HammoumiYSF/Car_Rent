from django.contrib import admin
from first_app.models import Topic,Webpage,accessrecord,login

admin.site.register(accessrecord)
admin.site.register(Topic)
admin.site.register(Webpage)
admin.site.register(login)

# Register your models here.
