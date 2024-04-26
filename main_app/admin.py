from django.contrib import admin
from .models import Finch, Feeding, Toy

admin.site.register([Finch, Feeding, Toy])
# Register your models here.
