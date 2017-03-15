from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _


#class ExpandedUser(AbstractUser):
  #  Numero = models.CharField(_("Numero"), max_length=20, blank=True)





































#from django.db import models
#from django.contrib.auth.models import (BaseUserManager, AbstractBaseUser, PermissionsMixin)


#class CustomUserManager(BaseUserManager):
    #def create_user(self, email,celular, password=None):
        #""" Creates and saves a User with the given email, city, and password. """
        #if not email:
            #msg = "Ingrese su correo"
            #raise ValueError(msg)

        #if not celular:
            #msg = "Ingrese su numero de telefono"
            #raise ValueError(msg)

        #user = self.model(
            #email=CustomUserManager.normalize_email(email),
            #celular=celular,
        #)

        #user.set_password(password)
        #user.save(using=self._db)
        #return user

    #def create_superuser(self, email, celular, password):
        #""" Creates and saves a superuser with the given email, city and password. """
        #user = self.create_user( email, password=password, celular=celular)
        #user.is_admin = True
        #user.is_staff = True
        #user.is_superuser = True 
        #user.save(using=self._db)
        #return user

#USERNAME_FIELD = "email"
#REQUIRED_FIELDS = ["celular", ]


#class CustomUser(AbstractBaseUser, PermissionsMixin):
    ## Inherits from both the AbstractBaseUser and PermissionMixin.
    #email = models.EmailField(verbose_name ="email address", max_length=255, unique=True, db_index=True,)
    #celular = models.CharField(max_length=255)
    #is_active = models.BooleanField(default=True)
    #is_admin = models.BooleanField(default=False)
    #is_staff = models.BooleanField(default=False)

    #objects = CustomUserManager()

    #USERNAME_FIELD = USERNAME_FIELD
    #REQUIRED_FIELDS = REQUIRED_FIELDS

    #def get_full_name(self):
        ## The user is identified by their email and city
        #return self.email, self.celular

    #def get_short_name(self):
        ## The user is identified by their email address
        #return self.email

    #def __unicode__(self):
        #return self.email
        
