from django import forms

from django_filters import FilterSet

from teachers.models import Teacher


class TeacherBaseForm(forms.ModelForm):
    class Meta:
        model = Teacher
        fields = [
            # '__all__'
            'first_name',
            'last_name',
            'birthday',
            'email',
            'phone',
        ]

        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }


class TeacherCreateForm(TeacherBaseForm):
    class Meta(TeacherBaseForm.Meta):
        pass


class TeacherUpdateForm(TeacherBaseForm):
    class Meta(TeacherBaseForm.Meta):
        exclude = [
            'email',
        ]


class TeacherFilterForm(FilterSet):
    class Meta:
        model = Teacher
        fields = {
            'first_name': ['exact', 'icontains'],
            'last_name': ['exact', 'startswith'],
        }

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
