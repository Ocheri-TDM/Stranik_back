from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate

class RegisterForm(UserCreationForm):
    first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Имя', 'class': 'form__input'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Фамилия', 'class': 'form__input'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Электронная почта', 'class': 'form__input'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Пароль', 'class': 'form__input'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Подтвердите пароль', 'class': 'form__input'}))

    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email', 'password1', 'password2')

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError("Этот email уже используется.")
        return email

    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data.get('email') 
        if commit:
            user.save()
        return user


class CustomLoginForm(forms.Form):
    email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Электронная почта', 'class': 'form__input'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Пароль', 'class': 'form__input'}))

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data.get('email')
        password = cleaned_data.get('password')

        if not email or not password:
            raise forms.ValidationError("Заполните все поля")

        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            raise forms.ValidationError("Пользователь с таким email не найден")

        user = authenticate(username=user.username, password=password)
        if user is None:
            raise forms.ValidationError("Неверный пароль")

        self.user = user
        return cleaned_data


from django import forms
from .models import UserProfile

class ProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ["profile_picture"]


class UserProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=30, required=False, label="Имя")
    last_name = forms.CharField(max_length=30, required=False, label="Фамилия")
    email = forms.EmailField(required=False, label="Электронная почта")
    phone = forms.CharField(max_length=15, required=False, label="Номер телефона")
    
    class Meta:
        model = UserProfile
        fields = ["profile_picture", "first_name", "last_name", "email", "phone"]

    def save(self, user, commit=True):
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        user.email = self.cleaned_data["email"]
        user.save()

        profile, created = UserProfile.objects.get_or_create(user=user)
        
        # Если передан новый аватар, обновляем его
        profile_picture = self.cleaned_data.get("profile_picture")
        if profile_picture:
            profile.profile_picture = profile_picture
        
        if commit:
            profile.save()

        return profile