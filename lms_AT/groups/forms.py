from django import forms

from groups.models import Group


class GroupBaseForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = [
            'name',
            'description',
            'start',
            'end'
        ]

        widgets = {
            'start': forms.DateInput(attrs={'type': 'date'}),
            'end': forms.DateInput(attrs={'type': 'date'})
        }


class GroupCreateForm(GroupBaseForm):
    class Meta(GroupBaseForm.Meta):
        pass


class GroupUpdateForm(GroupBaseForm):
    class Meta(GroupBaseForm.Meta):
        exclude = [
            'start_date',
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
