from django import forms
from .models import SalesEntry, DailyPurchase, StockRequisition



class SalesEntryForm(forms.ModelForm):
    class Meta:
        model = SalesEntry
        fields = ['date', 'phonepe_upi', 'card_pmt', 'zomato', 'swiggy', 'bms', 'cash', 'expenditure']



class DailyPurchaseForm(forms.ModelForm):
    class Meta:
        model = DailyPurchase
        fields = ['item_type', 'item_name', 'unit', 'quantity', 'price_per_unit', 'tax']



class StockRequisitionForm(forms.ModelForm):
    class Meta:
        model = StockRequisition
        fields = ['date', 'item_type', 'item_name', 'unit', 'closing', 'required', 'delivered']
        widgets = {
            'date': forms.DateInput(attrs={'type': 'date'}),
            'closing': forms.NumberInput(attrs={'class': 'form-control'}),
            'required': forms.NumberInput(attrs={'class': 'form-control'}),
            'delivered': forms.NumberInput(attrs={'class': 'form-control'}),
        }