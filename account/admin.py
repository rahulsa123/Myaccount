from django.contrib import admin
from .models import BankBook,CashBook,Incomes,Expenses,IncomeCategory,ExpensesCategory
# Register your models here.
admin.site.register(BankBook)
admin.site.register(CashBook)
admin.site.register(Incomes)
admin.site.register(Expenses)
admin.site.register(IncomeCategory)
admin.site.register(ExpensesCategory)
