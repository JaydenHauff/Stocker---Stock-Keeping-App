import os
from tabulate import tabulate



def search(word):
    with open('list.txt', 'r') as f:
        m = f.readlines()
        for i in m:
            l = i.split(',')
            # print(l)
            if word in l:
                print(f'{l[0]}.  {l[1]}  ------>  {l[2]}{l[3]}')


class AddEditDeleteSearch:

    @classmethod
    def addData(cls, id, name, price, mode):
        mode = '/' + mode
        with open('list.txt', 'a') as f:
            f.write(id + ',' + name + ',' + price + ',' + mode + ',\n')

    @classmethod
    def getData(cls):
        with open('list.txt', 'r') as f:
            t = f.readlines()
            c = 0
            k = []
            for i in t:
                c += 1
                temp = i.split(',')
                temp.pop()
                k.append(temp)

        print(tabulate(k,headers=['ID No.', 'Name', 'Price', 'Mode']))

    @classmethod
    #takes the user entered id as an argument in string datatype
    def edit(cls, cid: str):
        f = open('list.txt', 'r')
        f_temp = open('temp.txt', 'w')
        s = f.readlines()
        # print(s)
        for i in s:
            # print(i)
            temp = str(i)
            t = temp.split(',')
            # print(t)
            t1 = str(t[0])
            if t1 == cid:
                price = str(input('  Enter The New Price: '))
                f_temp.write(t[0] + ',' + t[1] + ',' + price + ',' + t[3] + ',\n')
            else:
                f_temp.write(t[0] + ',' + t[1] + ',' + t[2] + ',' + t[3] + ',\n')

        f.close()
        f_temp.close()
        os.remove('list.txt')
        os.rename('temp.txt', 'list.txt')

    @classmethod
    # takes the user entered id as an argument in string datatype
    def delete(cls, did: str):
        f = open('list.txt', 'r')
        f_temp = open('temp.txt', 'w')
        s = f.readlines()
        # print(s)
        for i in s:
            # print(i)
            temp = str(i)
            t = temp.split(',')
            # print(t)
            t1 = str(t[0])
            if t1 != did:
                f_temp.write(t[0] + ',' + t[1] + ',' + t[2] + ',' + t[3] + ',\n')

        f.close()
        f_temp.close()
        os.remove('list.txt')
        os.rename('temp.txt', 'list.txt')
