from ckip import CkipSegmenter
from ckiptagger import WS, POS, NER

text = '詞是最小有意義且可以自由使用的語言單位。任何語言處理的系統都必須先能分辨文本中的詞才能進行進一步的處理'
corpus = [
    '詞是最小有意義且可以自由使用的語言單位',
    '任何語言處理的系統都必須先能分辨文本中的詞才能進行進一步的處理',
    '例如機器翻譯、語言分析、語言了解、資訊抽取',
    '因此中文自動分詞的工作成了語言處理不可或缺的技術',
    '基本上自動分詞多利用詞典中收錄的詞和文本做比對',
    '找出可能包含的詞，由於存在歧義的切分結果',
    '因此多數的中文分詞程式多討論如何解決分詞歧義的問題',
    '而較少討論如何處理詞典中未收錄的詞出現的問題（新詞如何辨認）',
]


segmenter = CkipSegmenter()
result = segmenter.seg(text)
segmenter.batch_seg(corpus)

# print('result.res: {}\n'.format(result.res))

# # result.tok and result.pos contains only tokens and pos-tags respectively.
# print('result.tok: {}\n'.format(result.tok))
# print('result.pos: {}\n'.format(result.pos))