import datetime

from vertexai.generative_models import GenerativeModel
from vertexai import generative_models


class Vertex:
    location = "asia-northeast1"
    prompt = """あなたはプロの議事録作成者です。内容に書かれた文章は会議を録音し、録音したデータを文字起こししたものです。
    こちらを制約条件に従いわかりやすくまとめてください。内容が不明な部分は推測して要約してください。

# 制約条件
・音声は日本語です。要約する文章も日本語で出力してください。
・markdownで見やすく段落やインデントも考慮して出力してください。
・要点をまとめ、簡潔に書いて下さい。
・誤字・脱字があるため、話の内容を予測して置き換えてください。
・発言者の名前が分かる場合そちらも記載してください。不明な場合は「スピーカーA、スピーカーB」といった形にしてください。
・議論が起きている場合はその結果も書いてください。
・最後にToDoリストを期日付きでまとめて書いてください。期日がわからない場合は省略可。

# 内容"""
    model = GenerativeModel("gemini-1.0-pro-vision-001")

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
        print("Waiting for vertex ai to complete...")
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
                generative_models.HarmCategory.HARM_CATEGORY_HATE_SPEECH: generative_models.HarmBlockThreshold.BLOCK_ONLY_HIGH,
                generative_models.HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT: generative_models.HarmBlockThreshold.BLOCK_ONLY_HIGH,
                generative_models.HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT: generative_models.HarmBlockThreshold.BLOCK_ONLY_HIGH,
                generative_models.HarmCategory.HARM_CATEGORY_HARASSMENT: generative_models.HarmBlockThreshold.BLOCK_ONLY_HIGH,
            },
            # リアルタイムに出力するか
            stream=True,
        )

        contents = []
        try:
            for response in responses:
                if response.text:
                    contents.append(response.text)
        except Exception as e:
            print("This article cannot be summarized.")
            today = datetime.datetime.now()
            today_str = today.strftime('%Y%m%d%H%M%S')
            with open(f'./out/{today_str}_error_sentence.txt', 'w', encoding='utf-8') as f:
                f.write(request)

        result = "".join(contents)

        # with open('spoon.txt', 'w', encoding='utf-8') as f:
        #     f.write(text)

        return result
