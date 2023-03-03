from django import forms

from django_filters import FilterSet

from students.models import Student


class StudentBaseForm(forms.ModelForm):
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

        widgets = {
            'birthday': forms.DateInput(attrs={'type': 'date'})
        }


class StudentCreateForm(StudentBaseForm):
    class Meta(StudentBaseForm.Meta):
        pass


class StudentUpdateForm(StudentBaseForm):
    class Meta(StudentBaseForm.Meta):
        exclude = [
            'email',
        ]


class StudentFilterForm(FilterSet):
    class Meta:
        model = Student
        fields = {
            'first_name': ['exact', 'icontains'],
            'last_name': ['exact', 'startswith'],
        }
