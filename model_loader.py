import boto3
import os
import streamlit as st

@st.cache(suppress_st_warning=True)
def download_weights(bucket_name, s3_folder, aws_access_key_id, aws_secret_access_key, local_dir=None):
    """
    Download an entire folder from an S3 bucket.

    :param bucket_name: the name of the S3 bucket.
    :param s3_folder: the folder in the S3 bucket.
    :param aws_access_key_id: AWS access key id.
    :param aws_secret_access_key: AWS secret access key.
    :param local_dir: the local directory to download to. If None, files will be downloaded to the current directory.
    """
    # Check if directory already exists and contains files
    if local_dir and os.path.exists(local_dir) and os.listdir(local_dir):
        print(f"Directory {local_dir} already exists and contains files, skipping download.")
        return

    s3 = boto3.resource('s3', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)
    bucket = s3.Bucket(bucket_name)
    
    # Get the total number of objects to download for the progress bar
    total_objects = len(list(bucket.objects.filter(Prefix=s3_folder)))
    progress_bar = st.progress(0)

    try:
        for i, obj in enumerate(bucket.objects.filter(Prefix=s3_folder)):
            target = obj.key if local_dir is None \
                else os.path.join(local_dir, os.path.relpath(obj.key, s3_folder))
            if not os.path.exists(os.path.dirname(target)):
                os.makedirs(os.path.dirname(target))
            bucket.download_file(obj.key, target)
            
            # Update the progress bar
            progress_bar.progress((i + 1) / total_objects)
        
        st.success("Models downloaded successfully!")
    except Exception as e:
        st.error(f"Error occurred while downloading: {e}")


