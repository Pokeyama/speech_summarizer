import os
import unittest

from SpeechToText import SpeechToText
from gcs import GCS

bucket_id = os.getenv('SPEECH_SUMMARIZER_BUCKET_ID')
project_id = os.getenv('SPEECH_SUMMARIZER_PROJECT_ID')


class TestSpeechToText(unittest.TestCase):
    def test_recognize(self):
        gcs = GCS(bucket_id)
        # https://aozoraroudoku.jp/voice/rdp/rd1163.html
        gcs_path = gcs.upload("../resource/sample.mp3")
        speech = SpeechToText(project_id)
        # self.assertEqual(True, False)  # add assertion here
        print(speech.recognize(gcs_path))
        gcs.delete()


if __name__ == '__main__':
    unittest.main()
