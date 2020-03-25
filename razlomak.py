
def main():
    pass

if __name__ == '__main__':
    main()

class Razlomak(object):


    def __init__(self,brojnik,nazivnik):

        self._brojnik = brojnik
        self._nazivnik = nazivnik

    @property

    def brojnik(self):
        return self._brojnik

    @brojnik.setter

    def brojnik(self,value):
        self._brojnik = value

    @property

    def nazivnik(self):
        return self._nazivnik

    @nazivnik.setter

    def nazivnik(self,value):
        self.nazivnik = value

    def skrati(self):
        nd = 1
        for i in range (1,self.brojnik+1):
            if(self.brojnik % i ==0 and self.nazivnik % i ==0):
                nd = i
                i = i+1
        return self.brojnik / nd and self.nazivnik / nd


    def __repr__(self):

        return "Razlomak("+repr(self._brojnik) + ',' + repr(self._nazivnik)+")"

    def __str__(self):

        return 'Razlomak' + str(self._brojnik)+ '' +str(self._nazivnik)

    def __eq__(self,other):

        return self.brojnik/self.nazivnik == other.brojnik/other.nazivnik

    def __lt__(self,other):

        return self.brojnik/self.nazivnik < other.brojnik/other.nazivnik

    def __le__(self,other):

         return self.brojnik/self.nazivnik <= other.brojnik/other.nazivnik

    def __mul__(self,other):

        return Razlomak(self.brojnik*other.brojnik,self.nazivnik*other.nazivnik)

    def __mod__(self,other):

        return Razlomak(self.brojnik*other.nazivnik,self.nazivnik*other.brojnik)

    def __add__(self,other):

        a = self.nazivnik
        b = other.nazivnik
        nv = 1
        if (a<b):
            nv = a
            if (b%a ==0):
                b=b/a
            else:
                b = b
            nv = a*b
        else:
            nv = b
            if (a%b==0):
                a = a/b
            else:
                a = a
            nv = a*b
        return Razlomak(nv/self.nazivnik*self.brojnik+nv/other.nazivnik*other.brojnik,nv)

    def __sub__(self,other):
        a=self.nazivnik
        b = other.nazivnik
        nv = 1
        if (a<b):
            nv = a
            if (b%a==0):
                b = b/a
            else:
                b=b
            nv = a*b
        else:
            nv = b
            if (a%b==0):
                a = a/b
            else:
                a=a
            nv = a*b

        return Razlomak(nv/self.nazivnik*self.brojnik-nv/other.nazivnik*other.brojnik,nv)






