from django.contrib import admin
from .models import Home
from .models import Picture

from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from .models import Member

# Define an inline admin descriptor for Member model
# which acts a bit like a singleton
class MemberInline(admin.StackedInline):
    model = Member
    can_delete = False
    verbose_name_plural = 'member'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (MemberInline, )

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)





class HomesAdmin(admin.ModelAdmin):
    list_display = ['__str__','id','name','address','about','timestamp','updated']
    search_fields = ['name']

admin.site.register(Home,HomesAdmin)

class PictureAdmin(admin.ModelAdmin):
    list_display = ['__str__','id','homeid','image','timestamp','updated']




admin.site.register(Picture,PictureAdmin)