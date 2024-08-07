from django import forms
from jalali_date.fields import JalaliDateField
from jalali_date.widgets import AdminJalaliDateWidget
from .models import Birthdate

class BirthdateForm(forms.ModelForm):
    
    class Meta:
        model=Birthdate
        fields ='__all__'

    def __init__(self,*args,**kwargs):
        super(BirthdateForm,self).__init__(*args,**kwargs)
        self.fields["BirthDate"]=JalaliDateField(label=('تاریخ تولد'),
            widget=AdminJalaliDateWidget)                                         
                                                  
        
