from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse

# Google Cloud Storage LIBRARY
from google.cloud import storage
import google.auth

from datetime import datetime

#Documents Model import
from .models import CustomerDocuments

doc_info = CustomerDocuments.objects.all()

def upload_documents(bucket_name,source_file_name,destination_blob_name):
    storage_client = storage.Client()
    storage_bucket = storage_client.get_bucket(bucket_name)
    blob = storage_bucket.blob(destination_blob_name)
    blob.upload_from_string(source_file_name)
    print("Document Uploaded")

def download_documents(bucket_name,source_file_name,destination_file_name):
    """Downloading objects(files) from bucket in Google Cloud Storage"""
    storage_client = storage.Client()
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(source_file_name)

    blob.download_to_string(destination_file_name)

from .forms import DocumentUpload
# Create your views here.
def get_upload(request):


    # If this is a POST request, we will process the data -- sending it to Google Cloud Storage

    if request.method == 'POST':
        #create a form instance populated with data -- (Bound to the data previously entered that might need correction)
        name = request.POST['name']
        titleofdocument = request.POST['titleofdocument']
        doc_file = request.FILES['doc_file'].read()
        doc_file2 = request.FILES['doc_file']
        name_of_file = doc_file2.name
        print(doc_file)
        fullUpload = name + "-" + titleofdocument + "-" + name_of_file
        print(titleofdocument,name,doc_file)
        print(fullUpload)
        form = DocumentUpload(request.POST,request.FILES)
        cusDocRecord = CustomerDocuments()
        cusDocRecord.name = name
        cusDocRecord.name_of_document = titleofdocument
        cusDocRecord.service = request.POST['service']
        cusDocRecord.date = datetime.now()
        cusDocRecord.save()
        upload_documents("upload_documents",doc_file,fullUpload)
        if HttpResponse == 200:
            return (request, 'success.html')

    else:
        form = DocumentUpload()

    return render(request, 'uploadtest.html',{'form':form,'docs':doc_info})

def download_objects(request):
    from google.cloud import storage
    client = storage.Client()
    bucket = client.get_bucket('upload_documents')

    # download
    blob = bucket.get_blob('upload_documents/John Doe-Testing-W2-04_Expressions.pdf')
    print(blob.download_as_string())
    pass
