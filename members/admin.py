from django.contrib import admin

# Register your models here.
from .models import Member, Payment

class MemberAdmin(admin.ModelAdmin):
    list_display = ['phonenumber', 'lastname', 'wallet']
    search_fields = ['phonenumber', 'firstname', 'lastname']

class PaymentAdmin(admin.ModelAdmin):
    list_display = ['member', 'payment']
    autocomplete_fields = ['member']


admin.site.register(Member, admin_class=MemberAdmin)
admin.site.register(Payment, admin_class=PaymentAdmin)
