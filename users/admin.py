from django.contrib import admin

from .models import Company, Number, Profile


class NumberAdmin(admin.ModelAdmin):
    pass


class NumberInLine(admin.TabularInline):
    model = Number


class ProfileAdmin(admin.ModelAdmin):
    inlines = [NumberInLine]


class CompanyAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}


admin.site.register(Company, CompanyAdmin)
admin.site.register(Profile, ProfileAdmin)
admin.site.register(Number, NumberAdmin)
