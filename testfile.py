import data
import torch



default_path='./data/wikitext-2'



import os
import hashlib
fn = 'corpus.{}.data'.format(hashlib.md5(default_path.encode()).hexdigest())

print('fn is:', fn)

if os.path.exists(fn):
    print('Loading cached dataset...')
    corpus = torch.load(fn)
    print(corpus.dictionary)


else:
    print('Producing dataset...')
    corpus = data.Corpus(default_path)
    torch.save(corpus, fn)



print(default_path.encode().hex())
print(len(default_path.encode()))



print('dictionary :', corpus.dictionary)
print('train :', corpus.train)
print('valid :', corpus.valid)
print('test :', corpus.test)

for i in corpus.test:
    print(i)
    print(i.__str__())
    if i.__str__() != 'tensor(0)':
        for k in i:
            print(k)









'''
mydict = data.Dictionary()

mydict.add_word('goodgoodnet')
print(mydict)

print(mydict.idx2word)
print(mydict.word2idx)
print(mydict.counter)
print(mydict.total)

mydict.add_word('goodgoodnet')
print(mydict)

print(mydict.idx2word)
print(mydict.word2idx)

print(mydict.counter)
print(mydict.total)


word_list = ['hello', 'bazar', 'deddit', 'neggit', 'nonobabaro', 'hello', 'bazar', 'bazarit', 'netto', 'netto', 'netto',]

for word in word_list:
    mydict.add_word(word)



print('idx2word :', mydict.idx2word)
print('word2idx :', mydict.word2idx)
print('counter :', mydict.counter)
print('total :', mydict.total)
'''




















'''
class Car():
    def __init__(self, maker="Ford", model="Mustang", color="blue", max_speed=100, eng_volume=1.5,):
        self.maker = 'Ford'
        self.model = 'Mustang'
        self.color = 'red'
        self.max_speed = 200
        self.eng_volume = 2
        self.engine_working_now = False

    def start_driving(self):
        self.engine_working_now = True


    def __str__(self):
        return self.maker +' '+ self.model +' '+ self.color



mycar = Car()

print(mycar)
print(mycar.engine_working_now)

mycar.start_driving()

print(mycar.engine_working_now)
print(mycar.__sizeof__())

print(mycar.__init__())

print(mycar.__sizeof__())

print(mycar.__class__)
'''