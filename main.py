from random import randrange


def random():
    DATA = read()
    num = randrange(len(DATA))
    return DATA[num].upper()

def read():
    DATA = []
    with open('./archivos/data.txt','r',encoding='utf-8') as r:
        DATA = [x[:-1] for x in r]
    return DATA


def run():
    print(random())




if __name__=='__main__':
    run()
