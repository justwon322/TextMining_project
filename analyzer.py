import preprocess
from gensim.models import Word2Vec

cali_list = preprocess.output('cali')
ny_list = preprocess.output('newyork')

# Word2Vec 모델 학습
model = Word2Vec(ny_list, min_count=0,window=20) # options:

result = model.most_similar(positive=['pizza'])

model2 = Word2Vec(cali_list, min_count=0,window=20) # options:

result2 = model2.most_similar(positive=['pizza'])
print(result)
print(result2)
