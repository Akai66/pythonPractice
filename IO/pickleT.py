#序列化
import pickle
# with open('../data/serialize.txt','wb') as f:
#     d={'name':'Jack','age':18}
#     pickle.dump(d,f)
with open('../data/serialize.txt','rb') as f:
    d=pickle.load(f)
    print(pickle.dumps(d))
