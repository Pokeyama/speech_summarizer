from vertexai.generative_models import GenerativeModel
from vertexai.preview import generative_models


class Vertex:
    location = "us-central1"
    prompt = """これから入力する文章は会議の音声を文字起こししたものです。
    セクション毎に整理して、わかりやすく要約してください。"""
    model = GenerativeModel("gemini-1.0-pro")

    def __init__(self, project: str):
        """
        Constructor

        Args:
            project (str): Project ID associated with your Google Cloud project
        """
        self.project = project

    def execute(self, request: str) -> str:
        """
        Generates a summary from the input transcript text.

        Args:
            request (str): Input transcript text

        Returns:
            str: Generated summary text
        """
        responses = self.model.generate_content(
            self.prompt + request,
            generation_config={
                # 出力されるトークンの制限 だいたいx4
                "max_output_tokens": 2048,
                # すべての単語に大してどの確率以上を採用するか
                "temperature": 0.4,
                # 選択候補の語句の中でどの確率以上を採用するか
                "top_p": 0.4,
                # 選択された語句の中で上位何個を採用とするか（採用された語句の中からランダム）
                "top_k": 32
            },
            # 文章の安全性（悪意）の尺度
            safety_settings={
                generative_models.HarmCategory.HARM_CATEGORY_HATE_SPEECH: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
                generative_models.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
                generative_models.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
                generative_models.HarmCategory.HARM_CATEGORY_HARASSMENT: generative_models.HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
            },
            # リアルタイムに出力するか
            stream=True,
        )

        contents = []
        for response in responses:
            contents.append(response.text)

        text = "".join(contents)

        # with open('spoon.txt', 'w', encoding='utf-8') as f:
        #     f.write(text)

        return text

