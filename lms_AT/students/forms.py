from django import forms

from students.models import Student


class CreateStudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = [
            # '__all__'
            'first_name',
            'last_name',
            'birthday',
            'email',
            'phone',
        ]

    def clean(self):
        pass

    def clean_first_name(self):
        value = self.cleaned_data.get('first_name')

        return value.title()

    def clean_last_name(self):
        value = self.cleaned_data.get('last_name')
        
        return value.title()

    def clean_birthday(self):
        value = self.cleaned_data.get('birthday')

        return value

    def clean_email(self):
        value = self.cleaned_data.get('email')

        return value

    def clean_phone(self):
        val = self.cleaned_data.get('phone')
        sym = ['+', '(', ')', '-']
        value = ''
        for i in val:
            if i.isnumeric() or i in sym:
                value = value + i
            else:
                continue

        return value
