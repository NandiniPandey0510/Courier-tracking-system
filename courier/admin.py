from django.contrib import admin
from .models import *

admin.site.register(Signup)
admin.site.register(Feedback)
admin.site.register(ParcelRequest)
admin.site.register(Receiver)
admin.site.register(Payment)

