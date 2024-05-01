import gdown
import tarfile
import os

# Define the Google Drive file URL (34 gb)
file_url = 'https://drive.google.com/uc?id=1mq6fg69Ofm32-1HjEunoFtPg8ymAIcOp'

# Download the file
tar_file_path ="saved_model.tar"
gdown.download(file_url, tar_file_path, quiet=False)

# Untar the file
with tarfile.open(tar_file_path, 'r') as tar_ref:
    tar_ref.extractall(".")

# Remove the tar file
os.remove(tar_file_path)

print("Model downloaded and extracted successfully")