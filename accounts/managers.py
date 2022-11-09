from django.contrib.auth.models import BaseUserManager

class CustomUserManager(BaseUserManager):
    use_in_migrations=True

    def create_user(self,email,password=None,**extra_fields):
        if not email:
            raise ValueError("User must have Email address")
        if not password:
            raise ValueError("User must have a password")
        
        user=self.model(email=self.normalize_email(email),)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self,email,first_name,last_name,password=None,**extra_fields):
        user=self.create_user(email,first_name=first_name,last_name=last_name,password=password,**extra_fields)
        user.is_staff=True
        user.is_superuser=True
        user.save(using=self.db)
        return user


