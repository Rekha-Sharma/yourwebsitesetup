from django.contrib import admin
from .models import Ticket
from .models import User

admin.site.register(Ticket)
admin.site.register(User)
   