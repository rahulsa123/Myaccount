from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
# Create your models here.


class BankBook(models.Model):
    acc = models.CharField(max_length=45,)
    tran_date = models.DateField(default=timezone.now)
    amount = models.FloatField()
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    operation = models.CharField(max_length=45)


    def __str__(self):
        return f'BankBook of { self.acc}'


class CashBook(models.Model):
    acc = models.CharField(max_length=45,)
    tran_date = models.DateField(default=timezone.now)
    amount = models.FloatField()
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    operation = models.CharField(max_length=45)
    def __str__(self):
        return f'CashBook of { self.acc}'


class ExpensesCategory(models.Model):
    exp_catname = models.CharField(max_length=45)
    exp_catdetails = models.TextField()
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    def __str__(self):
        return f'ExpensesCategory {self.exp_catname} '


class IncomeCategory(models.Model):
    inc_catname = models.CharField(max_length=45)
    inc_catdetails = models.TextField()
    user = models.ForeignKey(User,on_delete = models.CASCADE)

    def __str__(self):
        return f'IncomeCategory {self.inc_catname} '


class Expenses(models.Model):
    exp_ac = models.CharField(max_length = 45)
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    exp_catid = models.ForeignKey(ExpensesCategory,on_delete = models.CASCADE)
    amount = models.FloatField()
    tran_date = models.DateField(default=timezone.now)
    pay_by = models.CharField(max_length=45)
    remark = models.TextField()

    def __str__(self):
        return f'Expenses {self.exp_ac}'


class Incomes(models.Model):
    inc_ac = models.CharField(max_length = 45)
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    inc_catid = models.ForeignKey(IncomeCategory, on_delete = models.CASCADE)
    amount = models.FloatField()
    tran_date = models.DateField(default=timezone.now)
    receiv_by = models.CharField(max_length=45)
    remark = models.TextField()

    def __str__(self):
        return f'Incomes {self.inc_ac}'
