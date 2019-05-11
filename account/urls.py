from django.urls import path
from .views import home, ExpensesCategoryView, IncomeCategoryView, ExpensesView, IncomeView, DayBook, CashBook, BankBook, BalanceSheetView

urlpatterns = [
    path("", home, name="account-home"),
    path("expenses_cat/", ExpensesCategoryView.as_view(), name="expenses_cat"),
    path("income_cat/", IncomeCategoryView.as_view(), name="income_cat"),
    path("expenses/", ExpensesView.as_view(), name="expenses"),
    path("income/", IncomeView.as_view(), name="income"),
    path("day_book/", DayBook.as_view(), name="day_book"),
    path("cash_book/", CashBook.as_view(), name="cash_book"),
    path("bank_book/", BankBook.as_view(), name="bank_book"),
    path("balance_sheet_book/", BalanceSheetView.as_view(), name="balance_sheet_book"),
]
