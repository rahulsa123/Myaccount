from django.shortcuts import render, redirect
from .models import ExpensesCategory ,IncomeCategory, Incomes, Expenses
from django.views.generic import TemplateView
# Create your views here.
from django.contrib.auth.decorators import login_required
from .forms import NewExpensesCategoryForm, NewIncomeCategoryForm, ExpenseForm, IncomeForm, BookFrom
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
@login_required
def home(request):
    return render(request, 'account/home.html', { 'title':'home'})


class ExpensesCategoryView(LoginRequiredMixin, TemplateView):
    template_name = "account/category.html"

    def get(self, request, *args, **kwargs):
        all_exp_cat = ExpensesCategory.objects.filter(user = request.user)
        exp_cat_form = NewExpensesCategoryForm(instance=request.user)
        context={
            'form': exp_cat_form,
            'title':"Expenses Category",
            'type': "expenses",
            'all_cat': all_exp_cat,

        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        exp_cat_form = NewExpensesCategoryForm(request.POST)
        all_exp_cat = ExpensesCategory.objects.filter(user = request.user)
        if exp_cat_form.is_valid():
            exp_cat = exp_cat_form.save(commit=False)
            exp_cat.user = request.user
            exp_cat.save()
            messages.success(request, f'New Expenses Category added')
            return redirect("/expenses_cat")
        else:
            context = {
                'form': exp_cat_form,
                'title': "Expenses Category",
                'all_cat': all_exp_cat,
                'type': "expenses",
            }
            return render(request, self.template_name, context)
        exp_cat_form = NewExpensesCategoryForm()
        context = {
            'form': exp_cat_form,
            'title': "Expenses Category",
            'all_cat': all_exp_cat,
            'type': "expenses",
        }
        return render(request, self.template_name, context)


class IncomeCategoryView(LoginRequiredMixin, TemplateView):
    template_name = "account/category.html"

    def get(self, request, *args, **kwargs):
        all_inc_cat = IncomeCategory.objects.filter(user = request.user)
        inc_cat_form = NewIncomeCategoryForm(instance=request.user)
        context={
            'form': inc_cat_form,
            'title':"Income Category",
            'type': "income",
            'all_cat': all_inc_cat,

        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        inc_cat_form = NewIncomeCategoryForm(request.POST)
        all_inc_cat = IncomeCategory.objects.filter(user = request.user)
        if inc_cat_form.is_valid():
            inc_cat = inc_cat_form.save(commit=False)
            inc_cat.user = request.user
            inc_cat.save()
            messages.success(request, f'New Income Category added')
            return redirect("/income_cat")
        else:
            context = {
                'form': inc_cat_form,
                'title': "Income Category",
                'type': "income",
                'all_cat': all_inc_cat,

            }
            return render(request, self.template_name, context)
        exp_cat_form = NewIncomeCategoryForm()
        context = {
            'form': exp_cat_form,
            'title': "Income Category",
            'type': "income",
            'all_cat': all_inc_cat,

        }
        return render(request, self.template_name, context)


class ExpensesView(LoginRequiredMixin, TemplateView):
    template_name = 'account/exp_or_inc_create.html'

    def get(self, request, *args, **kwargs):
        exp_form = ExpenseForm(instance=request.user)
        context = {
            'form': exp_form,
            'title': "Expenses",
            'type': "expenses",
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        exp_form = ExpenseForm(request.POST)
        if exp_form.is_valid():
            exp = exp_form.save(commit=False)
            exp.user = request.user
            print(exp.exp_ac)
            exp.save()
            messages.success(request, f'New Expenses Added')
            return redirect("/expenses")
        else:
            context = {
                'form': exp_form,
                'title': "Expenses",
                'type': "expenses",
            }
            return render(request, self.template_name, context)
        exp_form = ExpenseForm(instance=request.user)
        context = {
            'form': exp_form,
            'title': "Expenses",
            'type': "expenses",
        }
        return render(request, self.template_name, context)


class IncomeView(LoginRequiredMixin, TemplateView):
    template_name = 'account/exp_or_inc_create.html'

    def get(self, request, *args, **kwargs):
        inc_form = IncomeForm(instance=request.user)
        context = {
            'form': inc_form,
            'title': "income",
            'type': "income",
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        inc_form = IncomeForm(request.POST)
        if inc_form.is_valid():
            inc = inc_form.save(commit=False)
            inc.user = request.user
            print(type(inc), inc.inc_ac)
            inc.save()
            messages.success(request, f'New Income Added')
            return redirect("/income")
        else:

            context = {
                'form': inc_form,
                'title': "income",
                'type': "income",
            }
            return render(request, self.template_name, context)
        exp_form = IncomeForm(instance=request.user)
        context = {
            'form': exp_form,
            'title': "income",
            'type': "income",
        }
        return render(request, self.template_name, context)


class DayBook(LoginRequiredMixin , TemplateView):
    template_name = 'account/book.html'

    def get(self, request, *args, **kwargs):
        day_form= BookFrom()
        context ={
            'title': 'Day Book',
            'type': 'Day',
            'form': day_form,
        }
        return  render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        day_form = BookFrom(request.POST)
        if day_form.is_valid():
            new_day_form = BookFrom()
            income = Incomes.objects.filter(
                tran_date__gte=day_form.cleaned_data['from_date']).filter(
                tran_date__lte=day_form.cleaned_data['to_date'])
            expense = Expenses.objects.filter(
                tran_date__gte=day_form.cleaned_data['from_date']).filter(
                tran_date__lte=day_form.cleaned_data['to_date'])
            context = {
                'title': 'Day Book',
                'type': 'Day',
                'data_income': income,
                'data_expenses': expense,
                'form': new_day_form
            }
            return render(request, self.template_name, context)
        else:
            day_form = BookFrom()
            messages.error("please enter both values")
            return render(request, self.template_name, context={'title': 'Day Book', 'type': 'Day', 'form': day_form})


class CashBook(LoginRequiredMixin , TemplateView):
    template_name = 'account/book.html'

    def get(self, request, *args, **kwargs):
        cash_form= BookFrom()
        context ={
            'title': 'Cash Book',
            'type': 'Cash',
            'form': cash_form,
        }
        return  render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        cash_form = BookFrom(request.POST)
        if cash_form.is_valid():
            new_cash_form = BookFrom()
            income = Incomes.objects.filter(
                    receiv_by__exact='cash').filter(tran_date__gte=cash_form.cleaned_data['from_date']).filter(
                tran_date__lte=cash_form.cleaned_data['to_date'])
            expense = Expenses.objects.filter(pay_by__exact='cash').filter(
                tran_date__gte=cash_form.cleaned_data['from_date']).filter(
                tran_date__lte=cash_form.cleaned_data['to_date'])
            context = {
                'title': 'Cash Book',
                'type': 'Cash',
                'data_income': income,
                'data_expenses': expense,
                'form': new_cash_form
            }
            return render(request, self.template_name, context)
        else:
            cash_form = BookFrom()
            messages.error("please enter both values")
            return render(request, self.template_name, context={'title': 'Cash Book', 'type': 'Cash', 'form': cash_form})


class BankBook(LoginRequiredMixin , TemplateView):
    template_name = 'account/book.html'

    def get(self, request, *args, **kwargs):
        Bank_form= BookFrom()
        context ={
            'title': 'Bank Book',
            'type': 'Bank',
            'form': Bank_form,
        }
        return  render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        Bank_form = BookFrom(request.POST)
        if Bank_form.is_valid():
            new_Bank_form = BookFrom()
            income = Incomes.objects.exclude(
                    receiv_by__exact='cash').filter(tran_date__gte=Bank_form.cleaned_data['from_date']).filter(
                tran_date__lte=Bank_form.cleaned_data['to_date'])
            expense = Expenses.objects.exclude(pay_by__exact='cash').filter(
                tran_date__gte=Bank_form.cleaned_data['from_date']).filter(
                tran_date__lte=Bank_form.cleaned_data['to_date'])
            context = {
                'title': 'Bank Book',
                'type': 'Bank',
                'data_income': income,
                'data_expenses': expense,
                'form': new_Bank_form
            }
            return render(request, self.template_name, context)
        else:
            Bank_form = BookFrom()
            messages.error("please enter both values")
            return render(request, self.template_name, context={'title': 'Bank Book', 'type': 'Bank', 'form': Bank_form})


class BalanceSheetView(LoginRequiredMixin , TemplateView):
    template_name = 'account/book.html'

    def get(self, request, *args, **kwargs):
        bs_form= BookFrom()
        context ={
            'title': 'Balance Sheet',
            'type': 'Balance Sheet',
            'form': bs_form,
        }
        return  render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        bs_form = BookFrom(request.POST)
        if bs_form.is_valid():
            new_bs_form = BookFrom()
            income = Incomes.objects.filter(tran_date__gte=bs_form.cleaned_data['from_date']).filter(
                tran_date__lte=bs_form.cleaned_data['to_date'])
            expense = Expenses.objects.filter(
                tran_date__gte=bs_form.cleaned_data['from_date']).filter(
                tran_date__lte=bs_form.cleaned_data['to_date'])
            total=0
            for i in income:
                total += i.amount
            for i in expense:
                total -= i.amount
            context = {
                'title': 'Balance Sheet ',
                'type': 'Balance Sheet ',
                'data_income': income,
                'data_expenses': expense,
                'total': total,
                'form': new_bs_form
            }
            return render(request, self.template_name, context)
        else:
            bs_form = BookFrom()
            messages.error("please enter both values")
            return render(request, self.template_name, context={'title': 'Balance Sheet',
                                                                'type': 'Balance Sheet ', 'form': bs_form})

