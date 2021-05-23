from django.db import models
import re

class UserManager(models.Manager):
    def create_validator(self, reqPOST):
        errors = {}
        if len(reqPOST['first_name']) < 1:
            errors['first_name'] = "First name is too short"
        if len(reqPOST['last_name']) < 1:
            errors['last_name'] = "Last name is too short"
        if len(reqPOST['alias_gamert']) < 2:
            errors['alias_gamert'] = "Alias is too short"
        if len(reqPOST['email']) < 6:
            errors['email'] = "Email is too short"
        if len(reqPOST['password']) < 8:
            errors['password'] = "Password is too short"
        if reqPOST['password'] != reqPOST['confirm_pw']:
            errors['match'] = "Password and password confirmation don't match"
        EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(reqPOST['email']):
            errors['regex'] = "Email in wrong format"
        users_with_email = User.objects.filter(email=reqPOST['email'])
        if len(users_with_email) >= 1:
            errors['dup'] = "Email taken, user another"
        return errors

class User(models.Model):
    first_name = models.TextField()
    last_name = models.TextField()
    alias_gamert = models.TextField()
    email = models.TextField()
    password = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    objects = UserManager()