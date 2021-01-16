from django import forms


class DiscriminationForm(forms.Form):
    image = forms.CharField(label="inputFile")
    print(image)
    # image = forms.FilePathField()
