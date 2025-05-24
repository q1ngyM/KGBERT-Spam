# coding utf-8
import stanza

zh_nlp = stanza.Pipeline('zh', use_gpu=True)
text = "依林 美容 三八 女人 节 倾情 大放送 活动 超值 套餐 等你拿 活动 时间 月 日 一月 日           详情 进店 咨询 美丽 热线"

doc = zh_nlp(text)
for sent in doc.sentences:
    print("Sentence：" + sent.text)  # 断句
    print("Tokenize：" + ' '.join(token.text for token in sent.tokens))  # 中文分词
    print("UPOS: " + ' '.join(f'{word.text}/{word.upos}' for word in sent.words))  # 词性标注（UPOS）
    print("XPOS: " + ' '.join(f'{word.text}/{word.xpos}' for word in sent.words))  # 词性标注（XPOS）
    print("NER: " + ' '.join(f'{ent.text}/{ent.type}' for ent in sent.ents))  # 命名实体识别
