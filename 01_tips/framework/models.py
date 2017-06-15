from django.db import models
from django.contrib.auth.models import User

class Role(models.Model):
    id_role = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    weight = models.IntegerField(default=0)
    
    class Meta:
        db_table = 'eff_role'      

class UserRole(models.Model):
    id_userrole = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, db_column='id_user')
    role = models.ForeignKey(Role, db_column='id_role')

    class Meta:
        db_table = 'eff_userrole'     