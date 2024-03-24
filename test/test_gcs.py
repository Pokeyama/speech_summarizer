import os
import unittest
from gcs import GCS

bucket_id = os.getenv('SPEECH_SUMMARIZER_BUCKET_ID')

class TestGCS(unittest.TestCase):
    # def test_upload(self):
        # gcs = GCS(project_id)
        # print(gcs.upload("../resource/sample.mp3"))

    def test_delete(self):
        gcs = GCS(bucket_id)
        print(gcs.upload("../resource/sample.mp3"))
        gcs.delete()


if __name__ == '__main__':
    unittest.main()
