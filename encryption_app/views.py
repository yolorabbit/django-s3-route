from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .utils import generate_encryption_key, encrypt_file, upload_to_s3
import os

# Create your views here.

@csrf_exempt	# Only for the testing, We will remove it in the production.
def upload_and_encrypt_file(request):
    if request.method == 'POST' and request.FILES.get('file'):
    	uploaded_file = request.FILES['file']
    	file_name = uploaded_file.name
    	
    	encryption_key = generate_encryption_key()
    	encrypted_content = encrypt_file(uploaded_file.read(), encryption_key)
    	
    	s3_file_url = upload_to_s3(file_name, encrypted_content)
    	
    	return JsonResponse({
    		'status': 'success'
    		'file_url': s3_file_url,
    		'encryption_key': encryption_key.decode()
    	})
    return JsonResponse({ 'status': 'error', 'message': 'Invalid request'}, status=400)
