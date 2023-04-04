from django import forms
from .models import SharedStoriesModel

WHO_ARE_YOU_REPORTING_CHOICES = (
    ('0', 'a single person'),
    ('1', 'a company/organization'),
    ('2', 'a phone number'),
    ('3', 'social media personel'),
    ('4', 'a website/forum/online group'),
    ('5', 'group of people'),
)
WHICH_INFORAMTION_DO_YOU_HAVE_CHOICES = (
    ('0', 'full name'),
    ('1', 'phone number'),
    ('2', 'bank details'),
    ('3', 'website, forum, or group link'),
    ('4', 'other names or nickname'),
    ('5', 'profession'),
    ('5', 'profile picture/logo'),
    ('5', 'social media link/username'),
)
LOSS_SUFFERED_CHOICES = (
    ('Banking details', 'banking details'),
    ('Money', 'money'),
    ('Personal information', 'personal information'),
    ('Goods', 'goods'),
    ('Nothing', 'nothing'),
)


class SharedStoriesForm(forms.ModelForm):
    class Meta:
        model = SharedStoriesModel
        fields = '__all__'

        widgets = {
            'is_victim': forms.RadioSelect(attrs={
                'class': 'list-options-container',
            }),
            'is_anonymous': forms.RadioSelect(attrs={
                'class': 'list-options-container',
            }),

            'who_are_you_reporting': forms.CheckboxSelectMultiple(
            attrs={
                'class': 'list-options-container',
            }, 
            choices=WHO_ARE_YOU_REPORTING_CHOICES),

            'which_information_do_you_have': forms.CheckboxSelectMultiple(
            attrs={
                'class': 'list-options-container',
            }, 
            choices=WHICH_INFORAMTION_DO_YOU_HAVE_CHOICES),
            
            'scammer_gender': forms.Select(attrs={
                'id': 'scammer-gender',
            }),
            'scammer_age_range': forms.Select(attrs={
                'id': 'scammer-age-range',
            }),
            'describe_what_happened': forms.Textarea(attrs={
                'placeholder': 'tell your story here...',
            }),
            'loss_suffered': forms.CheckboxSelectMultiple(attrs={
                'class': 'list-options-container',
            }, choices=LOSS_SUFFERED_CHOICES),
            'scammer_profile_pic': forms.FileInput(attrs={
                'id': 'pic-upload-input',
                'hidden': 'hidden',
            }),
            'scam_evidence': forms.FileInput(attrs={
                'id': 'evidence1',
                'hidden': 'hidden',
            }),
        }

    def clean_scammer_fullname_or_website(self):
        fullname = self.cleaned_data['scammer_fullname_or_website']
        return fullname.lower().strip() if fullname else ""
    
    def clean_scammer_bank_name(self):
        bank_name = self.cleaned_data['scammer_bank_name']
        return bank_name.lower().strip() if bank_name else ""
    
    def clean_scammer_othernames_nickname(self):
        othernames = self.cleaned_data['scammer_othernames_nickname']
        return othernames.lower().strip() if othernames else ""
    
    def clean_scammer_profession(self):
        profession = self.cleaned_data['scammer_profession']
        return profession.lower().strip() if profession else ""
    
    def clean_scammer_website_or_group_link(self):
        website = self.cleaned_data['scammer_website_or_group_link']
        return website.lower().strip() if website else ""

    '''
    def clean_who_are_you_reporting(self):
        return ','.join(self.cleaned_data['who_are_you_reporting'])

    def clean_which_information_do_you_have(self):
        return ','.join(self.cleaned_data['which_information_do_you_have'])

    def clean_loss_suffered(self):
        return ','.join(self.cleaned_data['loss_suffered'])
    '''
