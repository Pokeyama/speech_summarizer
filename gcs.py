import random
import string
from google.cloud import storage


class GCS:
    object_prefix = 'audio/'
    gcs_uri = ""

    def __init__(self, bucket_name: str):
        """
        Constructor

        Args:
            bucket_name (str): Bucket name
        """
        self.bucket_name = bucket_name
        self.object_name = self.object_prefix + self.random_name(8)

        client = storage.Client()
        bucket = client.bucket(self.bucket_name)
        self.blob = bucket.blob(self.object_name)

    def upload(self, file_path: str) -> str:
        """
        Uploads a file to GCS and returns the GCS URI.

        Args:
            file_path (str): Path of the file to upload

        Returns:
            str: GCS URI
        """
        self.blob.upload_from_filename(file_path)
        self.gcs_uri = f'gs://{self.bucket_name}/{self.object_name}'
        return self.gcs_uri

    def delete(self):
        """
        Deletes an object from GCS.
        """
        if self.gcs_uri == "":
            return

        self.blob.reload()
        generation_match_precondition = self.blob.generation
        self.blob.delete(if_generation_match=generation_match_precondition)

    @staticmethod
    def random_name(n: int):
        """
        Generates a random name.

        Args:
            n (int): Length of the string to generate

        Returns:
            str: Random name
        """
        rand_lst = [random.choice(string.ascii_letters + string.digits) for i in range(n)]
        return ''.join(rand_lst)