from django import forms	
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    
    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')
        
    def save(self, commit=True):
        user = super(RegistrationForm, self).save(commit=False)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        
        if commit:
            user.save()
            
        return user 
        
#from django import forms
#from django.contrib.auth.forms import ReadOnlyPasswordHashField
#from main.models import CustomUser


#class CustomUserCreationForm(forms.ModelForm):
    ## A form for creating new users. Includes all the required fields, plus a repeated password.
    #password1 = forms.CharField(label="Password", widget=forms.PasswordInput)
    #password2 = forms.CharField(label="Password confirmation", widget=forms.PasswordInput)

    #class Meta:
        #model = CustomUser
        #fields = ("email", "celular")

    #def clean_password2(self):
        ## Check that the two password entries match
        #data = self.cleaned_data
        #password1 = data.get("password1")
        #password2 = data.get("password2")
        #if password1 and password2 and password1 != password2:
            #msg = "Passwords do not match"
            #raise forms.ValidationError(msg)
        #return password2

    #def save(self, commit=True):
        ## Save the provided password in hashed format
        #user = super(CustomUserCreationForm, self).save(commit=False)
        #data = self.cleaned_data
        #user.set_password(data["password1"])
        #if commit:
            #user.save()
        #return user


#class CustomUserChangeForm(forms.ModelForm):
    ## A form for updating users. Includes all the fields on the user, but replaces the password field
    ## with admin's password hash display field.
    #password = ReadOnlyPasswordHashField()

    #class Meta:
        #model = CustomUser
        #fields = "__all__"
    #def clean_password(self):
        ## Regardless of what the user provides, return the initial value. This is done here,
        ## rather than on the field, because the field does not have access to the initial value.
        #return self.initial["password"]        
