from django.contrib import admin

# Register your models here.
from .models import Booking, Food, Contact



admin.site.register(Booking)

admin.site.register(Food)


admin.site.register(Contact)