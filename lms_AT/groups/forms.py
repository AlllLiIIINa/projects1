from django import forms

from groups.models import Group


class CreateGroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = [
            # '__all__'
            'name',
            'description',
            'start',
        ]


class UpdateGroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = [
            # '__all__'
            'name',
            'description',
        ]

    def clean(self):
        pass

    def clean_name(self):
        value = self.cleaned_data.get('name')

        return value.title()

    def clean_description(self):
        value = self.cleaned_data.get('description')

        return value.title()

    def clean_start(self):
        value = self.cleaned_data.get('start')

        return value
