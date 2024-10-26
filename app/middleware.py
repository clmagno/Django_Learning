# middleware.py
import logging

# Mag-set up ng logging
logging.basicConfig(level=logging.INFO, 
                    filename='file_uploads.log', 
                    format='%(asctime)s - %(message)s')
logger = logging.getLogger('file_upload_logger')
logger.setLevel(logging.INFO)  # I-set ang level sa INFO

# Gumawa ng file handler
file_handler = logging.FileHandler('file_uploads.log')
file_handler.setLevel(logging.INFO)

# I-set up ang log format
formatter = logging.Formatter('%(asctime)s - %(message)s')
file_handler.setFormatter(formatter)

# I-add ang handler sa logger
logger.addHandler(file_handler)
class FileUploadLoggerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        
        if request.method == 'POST' and request.FILES:
            for file in request.FILES.getlist('csv_file'):  # Palitan ang 'csv_file' ayon sa pangalan ng field
                # Log ang pangalan ng in-upload na file
                logging.info(f'File uploaded: {file.name} by user: {request.user.username if request.user.is_authenticated else "Anonymous"}')

        # Iproseso ang request at kunin ang response
        response = self.get_response(request)
        return response
