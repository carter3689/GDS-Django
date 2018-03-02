from django.shortcuts import render
from django.http import HttpResponseRedirect,HttpResponse

# Google Cloud Storage LIBRARY
from google.cloud import storage
import google.auth

#FileStack Import
from filestack import Client
import locale

from datetime import datetime

#Boto3 Import
import boto3

#Documents Model import
from .models import CustomerDocuments

doc_info = CustomerDocuments.objects.all()

# Django-Filetransfers import
from filetransfers.api import prepare_upload

from .forms import DocumentUpload

from django.urls import reverse

# def upload_documents(bucket_name,source_file_name,destination_blob_name):
#     storage_client = storage.Client()
#     storage_bucket = storage_client.get_bucket(bucket_name)
#     blob = storage_bucket.blob(destination_blob_name)
#     blob.upload_from_string(source_file_name)
#     print("Document Uploaded")

# def upload_documents(Filename, Bucket, Key):
#     #AWS Upload
#     s3 = boto3.resource('s3')
#     s3.meta.client.upload_file()
#
# def download_documents(bucket_name,source_file_name,destination_file_name):
#     """Downloading objects(files) from bucket in Google Cloud Storage"""
#     storage_client = storage.Client()
#     bucket = storage_client.get_bucket(bucket_name)
#     blob = bucket.blob(source_file_name)
#
#     blob.download_to_string(destination_file_name)

from .forms import DocumentUpload
# Create your views here.
def get_upload(request):
    view_url = reverse('document-upload')
    if request.method == 'POST':
        form = DocumentUpload(request.POST,request.FILES)
        form.save()
        return HttpResponseRedirect(view_url)

    upload_url,upload_data = prepare_upload(request,view_url)
    form = DocumentUpload()
    return render(request,'uploads/upload.html', {'form': form, 'upload_url':upload_url, 'upload_data':upload_data})





    # # If this is a POST request, we will process the data -- sending it to Google Cloud Storage
    #
    # if request.method == 'POST':
    #     #create a form instance populated with data -- (Bound to the data previously entered that might need correction)
    #     locale.getdefaultlocale()
    #     name = request.POST['name']
    #     titleofdocument = request.POST['titleofdocument']
    #     doc_file = request.FILES['doc_file'].read()
    #     doc_file2 = request.FILES['doc_file']
    #     name_of_file = doc_file2.name
    #     print(doc_file)
    #     fullUpload = name + "/" + titleofdocument + "/" + name_of_file
    #     print(titleofdocument,name,doc_file)
    #     print(fullUpload)
    #     form = DocumentUpload(request.POST,request.FILES)
    #     cusDocRecord = CustomerDocuments()
    #     cusDocRecord.name = name
    #     cusDocRecord.name_of_document = titleofdocument
    #     cusDocRecord.service = request.POST['service']
    #     cusDocRecord.date = datetime.now()
    #     cusDocRecord.save()
    #     upload_documents(doc_file)
    #     if HttpResponse == 200:
    #         return (request, 'success.html')
    #
    # else:
    #     form = DocumentUpload()
    #
    # return render(request, 'uploadtest.html',{'form':form,'docs':doc_info})

def download_handler(request, pk):
    upload = get_object_or_404(UploadModel, pk=pk)
    return public_download_url(request, upload.file)
    # client = Client('AtX4SgHdWQNuh7lHEyx7Dz')
    # client.zip(destination_path = 'cdn.filestackcontent.com/', files = ['ElvhwPITRnyvbiNgW52e',"IOZ4Dxl9QPe5HQXPoRdB"])
