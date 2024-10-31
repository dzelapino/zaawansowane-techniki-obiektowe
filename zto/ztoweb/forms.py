from django import forms

from ztoweb.models import Hero, Profile


class HeroForm(forms.ModelForm):
    class Meta:
        model = Hero

        fields = '__all__'

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile

        fields = '__all__'

class LoginForm(forms.Form):
    login = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        login = self.cleaned_data.get('login')
        password = self.cleaned_data.get('password')
        if login and password:
            profile = Profile.objects.get(login=login)
            if profile.check_password(password):
                print("Is valid")
                # Generate key
            else:
                self.add_error('password', f'Invalid password for {login}')
