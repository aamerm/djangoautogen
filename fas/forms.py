from django import forms
from .models import Employee


class EmployeeForm(forms.ModelForm):

    class Meta:
        model = Employee
        fields = ['name', 'email', 'phone', 'department']
        exclude = []
        widgets = None
        localized_fields = None
        labels = {}
        help_texts = {}
        error_messages = {}

    def __init__(self, *args, **kwargs):
        return super(EmployeeForm, self).__init__(*args, **kwargs)

    def is_valid(self):
        return super(EmployeeForm, self).is_valid()

    def full_clean(self):
        return super(EmployeeForm, self).full_clean()

    def clean_name(self):
        name = self.cleaned_data.get("name", None)
        return name

    def clean_email(self):
        email = self.cleaned_data.get("email", None)
        return email

    def clean_phone(self):
        phone = self.cleaned_data.get("phone", None)
        return phone

    def clean_department(self):
        department = self.cleaned_data.get("department", None)
        return department

    def clean(self):
        return super(EmployeeForm, self).clean()

    def validate_unique(self):
        return super(EmployeeForm, self).validate_unique()

    def save(self, commit=True):
        return super(EmployeeForm, self).save(commit)

