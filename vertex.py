import datetime

from vertexai.generative_models import GenerativeModel
from vertexai.preview import generative_models


class Vertex:
    location = "asia-northeast1"
    prompt = """あなたは、プロの議事録作成者です。
以下の制約条件、内容を元に要点をまとめ、議事録を作成してください。

# 制約条件
・要点をまとめ、簡潔に書いて下さい。
・誤字・脱字があるため、話の内容を予測して置き換えてください。
・見やすいフォーマットにしてください。
・議論が起きている場合はその結果も書いてください。
・最後にToDoリストを期日付きでまとめて書いてください。期日がわからない場合は省略可。

# 内容"""
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
            today = datetime.date.today()
            today_str = today.strftime('%Y%m%d')
            with open(f'../out/{today_str}_error_sentence.txt', 'w', encoding='utf-8') as f:
                f.write(request)

        result = "".join(contents)

        # with open('spoon.txt', 'w', encoding='utf-8') as f:
        #     f.write(text)

        return result
