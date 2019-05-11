from django import forms

from .models import ExpensesCategory, IncomeCategory, Expenses, Incomes


class DateInput(forms.DateInput):
    input_type = 'date'



class NewExpensesCategoryForm(forms.ModelForm):
    exp_catname = forms.CharField(max_length=25, label='Expenses Category Name :')
    exp_catdetails = forms.CharField(label='Expenses Category Details :', widget=forms.Textarea(attrs={'rows': 3, 'cols': 20, 'style':'color:black;'}))

    class Meta:
        model = ExpensesCategory
        fields = ['exp_catname', "exp_catdetails"]


class NewIncomeCategoryForm(forms.ModelForm):
    inc_catname = forms.CharField(max_length=25, label='Income Category Name :')
    inc_catdetails = forms.CharField(label='Income Category Details :',widget=forms.Textarea(attrs={'rows': 3, 'cols': 20, 'style':'color:black;'}))

    class Meta:
        model = IncomeCategory
        fields = ['inc_catname', "inc_catdetails"]


class ExpenseForm(forms.ModelForm):
    pay_by = forms.ChoiceField(choices=(('cash', 'cash'), ('upi', 'upi'), ('bank', 'bank'), ('draft', 'draft')))
    tran_date = forms.DateField(label="Date", widget=DateInput())
    def __init__(self, *args,**kwargs):
        super(ExpenseForm, self).__init__(*args, **kwargs)

        self.fields['exp_ac'].label = "Expenses Account"
        self.fields['amount'].label = "Amount"
        self.fields['pay_by'].label = "Pay By"
        self.fields['remark'].label = "Remark"

        if 'instance' in kwargs:
            self.fields['exp_catid'] = forms.ModelChoiceField(queryset=ExpensesCategory.objects.filter(user=kwargs['instance']))
            self.fields['exp_catid'].label = "Expense Category"

    class Meta:
        model = Expenses
        fields = ['exp_ac','exp_catid', 'amount', 'pay_by', 'remark', 'tran_date']
        widgets ={
            'remark': forms.Textarea(attrs={'rows':'5','cols':'20'}),

        }


class IncomeForm(forms.ModelForm):
    receiv_by = forms.ChoiceField(choices=(('cash', 'cash'), ('upi', 'upi'), ('bank', 'bank'), ('draft', 'draft')))
    tran_date = forms.DateField(label="Date", widget=DateInput())
    def __init__(self, *args,**kwargs):
        super(IncomeForm, self).__init__(*args, **kwargs)

        self.fields['inc_ac'].label = "Income Account"
        self.fields['amount'].label = "Amount"
        self.fields['receiv_by'].label = "receive By"
        self.fields['remark'].label = "Remark"

        if 'instance' in kwargs:
            self.fields['inc_catid'] = forms.ModelChoiceField(queryset=IncomeCategory.objects.filter(user=kwargs['instance']))
            self.fields['inc_catid'].label = "Income Category"

    class Meta:
        model = Incomes
        fields = ['inc_ac','inc_catid', 'amount', 'receiv_by', 'remark', 'tran_date']
        widgets ={
            'remark': forms.Textarea(attrs={'rows': '5', 'cols': '20'}),

        }


class BookFrom(forms.Form):
    from_date = forms.DateField(label='From', widget=DateInput())
    to_date = forms.DateField(label='To', widget=DateInput())
    from_date.widget.attrs.update({'style': 'float:left; width;40%;'})
    to_date.widget.attrs.update({'style': 'float:left; width;40%;'})
