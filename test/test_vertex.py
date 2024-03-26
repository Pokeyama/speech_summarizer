import os
import unittest

from vertex import Vertex

project_id = os.getenv('SPEECH_SUMMARIZER_PROJECT_ID')


class TestVertex(unittest.TestCase):
    def test_execute_001(self):
        vertex = Vertex(project_id)
        result = vertex.execute("次の会議は来週行う。それまでにgeminiの使い方について学んでおくこと。")
        # self.assertEqual(True, False)  # add assertion here
        print(result)

    def test_execute_002(self):
        vertex = Vertex(project_id)
        result = vertex.execute(
            "映画 館 の 予約 で 空席 ばっかり だっ た 時 まで さん は どの 辺り の 席 を 取り ます か え 斜め の 端っこっ す ね あの な ん だろう 左右 の 端 っこ の どっち か です ね "
            "基本 的 に 取る の は 真ん中 ぐらい の 左右 の 端っこ を 取り ます 大体 みんなっ て どこ 取る ん だろう ね いや めちゃめちゃ 斜め から 見る のっ て バカ に し とん の かって "
            "言わ れ そう な ん だ けど な ん だろう なん で 端っこ 取ん の みたい に すげえ 言わ れる ん だ けど やっぱ 画面 端 が 好き な ん で ね うん 左右 に こう な ん だろう な "
            "ま 可能 な 限り ね ガチャ を ね 回避 し て いき たい わけ です よ 可能 な 限り 隣 の 林人 ガチャ を 回避 し て いき たい の で ま 基本 的 に は ね ま 横 の 方 に し "
            "がち な ん です よ ね 知り合い と 行く 時 と か は ま さすが に 真ん中 の 方 取り ます けど ガチ で 1人 で 行っ て ま 何 と か する 時 と か は そう ね ま ちょっと 横 "
            "の 方 取り がち です ま あと は ま 座席 の 形 次第 です けど その 最 に 右 か 左 か どっち か に ね あの 隙間 が ある ところ が 好き です ね ちょっと 前 失礼 し ます "
            "つっ て ね 出 て か なく て 住む 場所 そう 意外 と ハジ 派 が い なかっ た ね みんな 真ん中 の 人 だ ばっかり だっ た ま 映画 を 没入 感 あり で 見 たい なっ て なる と "
            "真ん中 行っ たく な ん です けど 最前 は ね 絶対 に やめ た 方 が いいっ す ね あの 首 が 終わる か 腰 が 行く か どっち か ね あれ ね かなり 難易 度 高い ま 焼けくそ の "
            "真ん中 は かなり あり な ん です けど 真ん中 で 見 てる と ね 俺 真ん中 じゃ ない や 最前 で 最前 で 見 てる と もう すごい 姿勢 で 見る こと に なる から その まま ね "
            "ウトウト し ちゃう か も しれ ん な はい そんな 感じ で ま 自分 の ね 好き な ところ で いき ましょう 。")
        # self.assertEqual(True, False)  # add assertion here
        print(result)

    def test_execute_003(self):
        vertex = Vertex(project_id)
        result = vertex.execute("夢 の 九 作 作  ペン と インキ  ペンサキ が 陰気 に こう 言い まし た  お前 ぐらい 嫌 な もの は ない  私 が いくら 金 の 異服 を 着 "
                                "て い て も  お前 は すぐ に 錆び さし て 役 に 立た なく し て しまう  私 は お前 みたい な もの 大嫌い さ  インキ は こう 答え まし "
                                "た  ペン は さびる の が 役目 じゃ ない  陰器 は なくなる の が 務め じゃ ない  一緒 に なっ て 字 を 書く の が 役目 さ  さびる の が "
                                "嫌 なら 鉄 に 生まれ て こ ない 方 が いい じゃ ない か  陰器 が 嫌 なら 何 だっ て ペン に 生まれ て き た ん だ え ")
        print(result)


if __name__ == '__main__':
    unittest.main()
