from django.contrib import admin
from authapp.models import Person,Dog,Review,Car1,Car2,Booking
# Register your models here.
class Car1Admin(admin.ModelAdmin):
	list_display=[f.name for f in Car1._meta.fields]

admin.site.register(Car1,Car1Admin)


class Car2Admin(admin.ModelAdmin):
	list_display=[f.name for f in Car2._meta.fields]

admin.site.register(Car2,Car2Admin)

class BookingAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Booking._meta.fields]

admin.site.register(Booking,BookingAdmin)
class PersonAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Person._meta.fields]

admin.site.register(Person,PersonAdmin)

class DogAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Dog._meta.fields]

admin.site.register(Dog,DogAdmin)

class ReviewAdmin(admin.ModelAdmin):
	list_display=[f.name for f in Review._meta.fields]

admin.site.register(Review,ReviewAdmin)