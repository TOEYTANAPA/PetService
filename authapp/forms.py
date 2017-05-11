import re
from django import forms
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from authapp.models import Review
from django.forms import ModelForm, Textarea,FileInput



RATING_CHOICES = (
        (1, '1'),
        (2, '2'),
        (3, '3'),
        (4, '4'),
        (5, '5'),
)
   
class RatingForm(forms.Form):
  # attrs={'class':'star'}
    rate = forms.MultipleChoiceField(required=False,widget=forms.RadioSelect(),choices=RATING_CHOICES)
    comment = forms.CharField(widget=forms.Textarea(attrs={'cols': 5, 'rows': 5,'placeholder': "Comment and Share your happy dog's photo."}))
    pic = forms.ImageField(widget=forms.FileInput(attrs={'id': 'imgInp'}))

# class Rating(forms.ModelForm):
#     class Meta:
#         model = Review
#         exclude = ('Review',)
#         widgets = {'rating':forms.RadioSelect,}
    

class RegistrationForm(forms.Form):
    

    # username = forms.RegexField(regex=r'^\w+$', widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Username"), error_messages={ 'invalid': _("This value must contain only letters, numbers and underscores.") })
    username = forms.EmailField(widget=forms.TextInput(attrs=dict(required=True, max_length=50)), label=_("Email address"))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=50, render_value=False)), label=_("Password"))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs=dict(required=True, max_length=50, render_value=False)), label=_("Password (again)"))
    phonenumber = forms.CharField(widget=forms.TextInput(attrs=dict(required=True, max_length=30)), label=_("Phone Number"))
    
    def clean_username(self):
        try:
            user = User.objects.get(username__iexact=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']
        raise forms.ValidationError(_("The email address already exists. Please try another one."))
   
    # def clean_username(self):
    #     try:
    #         user = User.objects.get(email__iexact=self.cleaned_data['email'])
    #     except User.DoesNotExist:
    #         return self.cleaned_data['email']
    #     raise forms.ValidationError(_(u"Another user is already registered with the email address %(email)s.")
    #                                     % {'email':self.cleaned_data['email']} )

    def clean(self):
        if 'password1' in self.cleaned_data and 'password2' in self.cleaned_data:
            if self.cleaned_data['password1'] != self.cleaned_data['password2']:
                raise forms.ValidationError(_("The two password fields did not match."))
        return self.cleaned_data

    # def clean_email(self):
    #     if 'email' not in self.cleaned_data:
    #         return self.cleaned_data

    #     if User.objects.filter( email__iexact = self.cleaned_data['email'] ).count() != 0:
    #         raise forms.ValidationError(_(u"Another user is already registered with the email address %(email)s.")
    #                                     % {'email':self.cleaned_data['email']} )
    #     return self.cleaned_data
