from django.contrib import admin
from apps.profiles.models import Profile  
from django.utils.translation import gettext_lazy as _

class ProfileAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'pseudo', 'bio', 'birth_date', 'gender', 'adress', 'town', 'country',)
    # list_filter = ('gender',)
    fieldsets = (
        # (User, {'fields': ('user')}),
        
        (_('Personal info'), {'fields': ('pseudo', 'img_profile', 'birth_date', 'gender')}),
        
        (_('Location'), {'fields': ('adress', 'town', 'country'),}),
        # (_('User description'), {'fields': ('description', 'bio')}),
        
        # (_('User description'), {'fields': ('description', '')}),
        (_('Social network'), {'fields': ('link_linkedin', 'link_gitthub', 'link_twitter', 'link_mysite')}),
    )

    # add_fieldsets = (
    #     (None, {
    #         'classes': ('wide',),
    #         'fields': ('first_name', 'last_name', 'email', 'password1', 'password2', 'is_active', 'is_email_verified', 'is_staff')}
    #     ),
    # )
    search_fields = ('pseudo', 'gender', 'town', 'country',)
    ordering = ('-date_updated',)
    
    def full_name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"
    
admin.site.register(Profile, ProfileAdmin)
