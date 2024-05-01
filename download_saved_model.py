import gdown
import tarfile
import os

# Define the Google Drive file URL (34 gb)
file_url = 'https://drive.google.com/uc?id=1mq6fg69Ofm32-1HjEunoFtPg8ymAIcOp'

# Define the directory to save the downloaded file and extracted contents
extract_dir = './saved_model'
os.makedirs(extract_dir, exist_ok=True)

# Download the file
tar_file_path = os.path.join(".", 'saved_model.tar')
gdown.download(file_url, tar_file_path, quiet=False)

# Untar the file
with tarfile.open(tar_file_path, 'r') as tar_ref:
    tar_ref.extractall(extract_dir)

# Remove the tar file
os.remove(tar_file_path)

print("Model downloaded and extracted successfully")