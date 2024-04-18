import datetime

from google.cloud.speech_v2 import SpeechClient
from google.cloud.speech_v2.types import cloud_speech
from google.api_core import client_options


class SpeechToText:
    api_endpoint = "us-central1-speech.googleapis.com"
    language_code = "ja-JP"
    timeout = 300

    def __init__(self, project_id: str):
        """
        Constructor

        Args:
            project_id (str): Project ID associated with your Google Cloud project
        """
        self.project_id = project_id

        # Configure Speech Client with regional endpoint
        client_options_var = client_options.ClientOptions(
            api_endpoint=self.api_endpoint
        )
        self.client = SpeechClient(client_options=client_options_var)

        # Define RecognitionConfig for language and model
        self.config = cloud_speech.RecognitionConfig(
            auto_decoding_config=cloud_speech.AutoDetectDecodingConfig(),
            language_codes=[self.language_code],
            model="chirp",
        )

    def recognize(self, gcs_path: str):
        """
        Performs speech-to-text transcription on a GCS audio file.

        Args:
            gcs_path (str): URI of the audio file stored in Google Cloud Storage

        Returns:
            str: Combined transcript text from the recognized speech segments
        """
        file_metadata = cloud_speech.BatchRecognizeFileMetadata(uri=gcs_path)

        request = cloud_speech.BatchRecognizeRequest(
            recognizer=f"projects/{self.project_id}/locations/us-central1/recognizers/_",
            config=self.config,
            files=[file_metadata],
            recognition_output_config=cloud_speech.RecognitionOutputConfig(
                inline_response_config=cloud_speech.InlineOutputConfig(),
            ),
            processing_strategy=cloud_speech.BatchRecognizeRequest.ProcessingStrategy.DYNAMIC_BATCHING,
        )

        operation = self.client.batch_recognize(request=request)
        print("Waiting for speech to text to complete...")
        response = operation.result(self.timeout)

        transcript_builder = []
        for result in response.results[gcs_path].transcript.results:
            if len(result.alternatives) > 0:
                transcript_builder.append(result.alternatives[0].transcript)

        today = datetime.datetime.now()
        today_str = today.strftime('%Y%m%d%H%M%S')
        with open(f'./out/{today_str}_speech_string.txt', 'w',
                  encoding='utf-8') as f:
            f.write("".join(transcript_builder))
        return "".join(transcript_builder)

    @staticmethod
    def calculate_average(confidence_list):
        """
        Calculates the average confidence score from a list of confidence values (0-100).

        Args:
            confidence_list (list): List of confidence scores (0-100)

        Returns:
            float: Average confidence score (0-100)
        """
        if not confidence_list:
            return 0
        return sum(confidence_list) / len(confidence_list)
