# speech_summarizer

## Overview
This repository provides Python code to summarize meeting transcripts. It uses Vertex AI's generative models to generate clear and concise summaries organized by section.

## GCP Service Account Key Path Must Be Registered in Environment Variables
To use Vertex AI, you need a service account key for your GCP project. The path to the service account key must be registered in an environment variable.

```shell
# Linux/Mac
export GOOGLE_APPLICATION_CREDENTIALS="/path/to/secret-key.json"

# Windows
set GOOGLE_APPLICATION_CREDENTIALS="C:\path\to\secret-key.json"
```

## Usage
Install Python 3.7 or later.
Install the required libraries by running the following command:

#### sample
```sh
  $ cd speech_summarizer
  $ pip install -r requirements.txt
  $ python3 main.py -a {audio_path} \
        -p {project_id} \
        -b {bucket_id}
```

If you have not set the environment variable GOOGLE_APPLICATION_CREDENTIALS, you can specify the path to the service account key on the command line using the -e option.

```shell
  $ python3 main.py -a {audio_path} \
        -p {project_id} \
        -b {bucket_id} \
        -e /path/to/secret-key.json
```

## Notes
The quality of the generated summary depends on the quality of the meeting transcript.
Generating summaries for long transcripts may take some time.