from django.shortcuts import render
from django.http import HttpResponseRedirect

# Google Cloud Storage LIBRARY
from google.cloud import storage
import google.auth

#Instantiates a client
# credentials,project = google.auth.default()
# storage_client = storage.Client()
#
# #The name for the new bucket
# bucket_name = "upload_documents"
#
# # Creates the new bucket
# bucket = storage_client.create_bucket(bucket_name)

#Uploading Documents function
def upload_documents(bucket_name,source_file_name,destination_blob_name):
    storage_client = storage.Client()
    storage_bucket = storage_client.get_bucket(bucket_name)
    blob = storage_bucket.blob(destination_blob_name)
    blob.upload_from_filename(source_file_name)
    print("Document Uploaded")

from .forms import DocumentUpload
# Create your views here.
def get_upload(request):
    # If this is a POST request, we will process the data -- sending it to Google Cloud Storage

    if request.method == 'POST':
        #create a form instance populated with data -- (Bound to the data previously entered that might need correction)
        name = request.POST['name']
        titleofdocument = request.POST['titleofdocument']
        doc_file = request.FILES['doc_file']
        name_of_file = doc_file.name
        print(doc_file)
        fullUpload = name + "-" + titleofdocument + "-" + name_of_file
        print(titleofdocument,name,doc_file)
        print(fullUpload)
        form = DocumentUpload(request.POST,request.FILES)
        upload_documents("upload_documents",int(bytes(int(doc_file))),fullUpload)

    else:
        form = DocumentUpload()

    return render(request, 'document-upload.html',{'form':form})
