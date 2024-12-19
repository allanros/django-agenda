from django import forms
from contact.models import Contact

class ContactForm(forms.ModelForm):
    description = forms.CharField(
        widget=forms.Textarea(
            attrs={
                'rows': 5,
                'placeholder': 'Enter your message here'
            },
        ),
        label='Descrição',
        help_text='Digite sua mensagem aqui',
        required=False,
    )

    picture = forms.ImageField(
        widget=forms.FileInput(
            attrs={
                'accept': 'image/*',
                
            }
        )
    )

    class Meta:
        model = Contact
        fields = (
            'first_name',
            'last_name',
            'phone',
            'email',
            'description',
            'category',
            'picture',
        )

    def clean(self):
        cleaned_data = self.cleaned_data
        return super().clean()
    
    def clean_first_name(self):
        first_name = self.cleaned_data.get('first_name')
        
        if first_name == 'admin':
            self.add_error(
                'first_name',
                forms.ValidationError(
                    'The name admin is not allowed',
                    code='invalid',
                )
            )

        return first_name
