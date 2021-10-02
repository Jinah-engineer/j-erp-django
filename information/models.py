from django.db import models


class employee(models.Model):
    employee_id = models.AutoField(db_column='employee_id', primary_key=True)
    employee_name = models.CharField(db_column='employee_name', max_length=255)
    employee_rank = models.CharField(db_column='employee_rank', max_length=50)
    hiredate = models.DateTimeField(db_column='hiredate')

    class Meta:
        db_table = 'emplyee'