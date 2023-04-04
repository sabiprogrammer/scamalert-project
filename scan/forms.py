from django import forms
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
                'placeholder': 'briefly explain here...',
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
