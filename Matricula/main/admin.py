from django.contrib import admin
#from django.contrib.auth.admin import UserAdmin
#from main.models import ExpandedUser


#admin.site.register(ExpandedUser)
#from main.models import CustomUser
#from main.forms import CustomUserCreationForm, CustomUserChangeForm


#class CustomUserAdmin(UserAdmin):
    ## Forms to add and change user instances
    #form = CustomUserChangeForm
    #add_form = CustomUserCreationForm

    ## The fields to be used in displaying the User model. These override the definitions on the
    ## base UserAdmin that reference specific fields on auth.User.
    #list_display = ("email", "celular", "is_staff")
    #list_filter = ("is_staff", "is_superuser", "is_active", "groups")
    #search_fields = ("email", "celular")
    #ordering = ("email",)
    #filter_horizontal = ("groups", "user_permissions",)
    #fieldsets = (
        #(None, {"fields": ("email", "password")}),
        #("Personal info", {"fields": ("celular",)}),
        #("Permissions", {"fields": ("is_active", "is_staff", "is_superuser", "groups", "user_permissions")}),
        #("Important dates", {"fields": ("last_login",)}),
    #)

    #add_fieldsets = (
        #(None, {
            #"classes": ("wide",),
            #"fields": ("email", "celular", "password1", "password2")}
        #),
    #)

## Register the new Customuser and CustomUserAdmin classes
#admin.site.register(CustomUser, CustomUserAdmin)