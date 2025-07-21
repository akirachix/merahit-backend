from django import forms
from users.models import Users
import re
class UserCreationWithPasswordForm(forms.ModelForm):
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput,
        max_length=4,
        min_length=4,
        help_text="Enter a password."
    )
    class Meta:
        model = Users
        fields = ('phone_number', 'first_name', 'last_name', 'role')
    def clean_password(self):
        password = self.cleaned_data.get('password')
        if not re.fullmatch(r'\d{4}', password):
            raise forms.ValidationError("Password must be exactly 4 digits.")
        return password
    def save(self, commit=True):
        user = super().save(commit=False)
        password = self.cleaned_data['password']
        user.set_password(password)
        if commit:
            user.save()
        return user