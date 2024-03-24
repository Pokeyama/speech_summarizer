"""
This module takes an audio file as input, transcribes it using the Speech-to-Text API,
summarizes the transcript using Vertex AI, and saves the summary to a text file.

It relies on Google Cloud services for speech-to-text and summarization,
and uses GCS for intermediate storage of the audio file.
"""

import datetime
import os


def main(args):
    """
   The main function coordinates the workflow of the module.

   Args:
       args (argparse.Namespace): A namespace containing parsed command-line arguments.
   """

    try:
        """
       Sets up authentication for Google Cloud services and imports necessary modules.
       """
        if os.getenv('GOOGLE_APPLICATION_CREDENTIALS') is None:
            if args.env_path is None:
                raise Exception("GOOGLE_APPLICATION_CREDENTIALS is required to run.")
            os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = args.env_path

        from SpeechToText import SpeechToText
        from gcs import GCS
        from vertex import Vertex

        # Uploads the audio file to GCS
        gcs = GCS(args.bucket_id)
        gcs_path = gcs.upload(args.audio_path)
        print(gcs_path)

        # Transcribes the audio file using Speech-to-Text
        speech_to_text = SpeechToText(args.project_id)
        audio_text = speech_to_text.recognize(gcs_path)

        # Summarizes the transcript using Vertex AI
        vertex = Vertex(args.project_id)
        result = vertex.execute(audio_text)

        # Deletes the audio file from GCS
        gcs.delete()

        # Saves the summary to a text file
        today = datetime.date.today()
        today_str = today.strftime('%Y%m%d')
        with open(f'./out/{today_str}_summary.txt', 'w', encoding='utf-8') as f:
            f.write(result)

        print(f"Success. Output is saved in ./out/{today_str}_summary.txt")

    except Exception as e:
        """
       Handles any exceptions that occur during the process.
       """
        print(f"{e}")


if __name__ == '__main__':
    """
   Parses command-line arguments and calls the main function.
   """
    import argparse

    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--audio_path', help='required argument --audio_path', required=True)
    parser.add_argument('-p', '--project_id', help='required argument --project_id', required=True)
    parser.add_argument('-b', '--bucket_id', help='required argument --bucket_id', required=True)
    parser.add_argument('-e', '--env_path', required=False)
    args = parser.parse_args()
    main(args)
