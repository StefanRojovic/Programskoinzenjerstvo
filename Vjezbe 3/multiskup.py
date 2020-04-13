
def main():
    pass

if __name__ == '__main__':
    main()

class MultiSkup(object):
    def __init__(self , rjecnik = None):
        self._rjecnik = {}
        self._elements = []

        if rjecnik is not None :
            self._rjecnik = rjecnik
            for i in self._rjecnik :
                if i not in self._elements:
                    self._elements.append(i)

    def __str__(self):
        str_arr = []
        for  i in self._elements :
            str_arr.append("%r%r" % (i , self._rjecnik.count(i)))
        return "{{"+" , ".join(str_arr)+"}}"

    def __iter__(self):
        return iter (self._rjecnik)

    def __repr__(self):
        return "MultiSkup("+repr(self._rjecnik)+")"

    def add (self, num , times = 1):
        for i in range (times):
            self._rjecnik.append (num)

    def remove (self , num , times = 1):
        for i in range (times):
            self._rjecnik.remove (num)


print('*** test 1 ***')
a = MultiSkup([1,1,2,2,2,3,3,4])
print(a)

print('*** test 2 ***')
a = MultiSkup([1,1,2,2,2,3,3,4])
for el in a:
 print(el)
print(repr(a))

print('*** test 3 ***')
a = MultiSkup([1,1,2,2,2,3,3,4])
a.add(4)
print(a)
a.add(2,3)
print(a)
a.remove(4,2)
print(a)