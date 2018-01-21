from django import forms

SERVICES = (('Taxes','Taxes'),('Bookkeeping','Bookkeeping'),('Consulting','Consulting'))
class DocumentUpload(forms.Form):
    name = forms.CharField(label = "Enter Your Full Name", max_length = 100)
    titleofdocument = forms.CharField(label="Enter the name of your document",max_length = 100)
    service = forms.ChoiceField(label="What sevice is this document for?", choices = SERVICES)
    doc_file = forms.FileField(label="Upload file")
