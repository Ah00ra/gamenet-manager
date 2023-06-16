from django.contrib import admin

# Register your models here.
from .models import Member, Payment, Game

class MemberAdmin(admin.ModelAdmin):
    list_display = ['phonenumber', 'lastname', 'wallet']
    search_fields = ['phonenumber', 'firstname', 'lastname']

class PaymentAdmin(admin.ModelAdmin):
    list_display = ['member', 'payment']
    autocomplete_fields = ['member']


class GameAdmin(admin.ModelAdmin):
    list_display = ['game', 'price_per_hour']

admin.site.register(Member, admin_class=MemberAdmin)
admin.site.register(Payment, admin_class=PaymentAdmin)
admin.site.register(Game, admin_class=GameAdmin)
