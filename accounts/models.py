# ---------- 고기우 작업 ----------
from django.db import models


class Member(models.Model):
    member_no = models.AutoField(db_column='member_no', primary_key=True)
    member_id = models.CharField(db_column='member_id', max_length=20)
    member_pw = models.CharField(db_column='member_pw', max_length=50)
    member_name = models.CharField(db_column='member_name', max_length=50)
    member_email = models.CharField(db_column='member_email', max_length=255)
    usage_flag = models.CharField(db_column='usage_flag', max_length=10, default=1)
    registdate = models.DateTimeField(db_column='registdate', )

    class Meta:
        managed = False
        db_table = 'member'

    def __str__(self):
        return "아이디 : " + self.member_id + ", 이메일 : " + self.member_email