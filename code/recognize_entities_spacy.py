# 使用Spacy的英文模型（预训练+自定义实体）
import spacy
nlp = spacy.load("en_core_web_lg")
# text = "Subject: looking for medication ? we ` re the best source .it is difficult to make our material condition better by the best law , but it is easy enough to ruin it by bad laws .excuse me . . . : ) you just found thebest and simpliest site formedication on the net . no perscription , easydelivery .private , secure , and easy .better see rightly on a pound a week than squint on a million .we ` ve goanything that you will ever want .erection treatment pills , anti - depressant pills , weight loss , andmore ! http : / / splicings . bombahakcx . com / 3 /knowledge and human power are synonymous .only high - quality stuff for low rates !100 % moneyback guarantee !there is no god , nature sufficeth unto herself in no wise hath she need of an author ."
text = "whats bruv hope great break rewarding semester"
doc = nlp(text)
print([(ent.text, ent.label_) for ent in doc.ents])