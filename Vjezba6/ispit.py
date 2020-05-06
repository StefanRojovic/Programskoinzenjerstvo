import json
import sqlite3

def main():
    pass

if __name__ == '__main__':
    main()

    class Ispiti(dict):

        def dodaj(self , student ,kolegij , ocjena):
            if student not in self:
                self[student] = {}
            self[student][kolegij] = ocjena

        def izbrisi(self , student , kolegij):
            if kolegij in self[student]:
                self[student].pop(kolegij)

        def promijeni(self , student , kolegij , ocjena):
            self[student][kolegij] = ocjena

        def spremi_datoteka(self , datoteka):
            with open(datoteka , 'w') as f:
                studenti = self.keys()
                for i in range(len(self)):
                    kolegiji = self[studenti[i]].keys()
                    for j in range(len(kolegiji)):
                        novi = studenti[i] , kolegiji[j] , self[studenti[i]][kolegiji[j]]
                        nova = "%s \t %s \t %s\n" %(studenti[i] , kolegiji[j] , self[studenti[i]][kolegiji[j]])
                        f.write(nova)
        @staticmethod
        def ucitaj_datoteka(datoteka):
            novi = ispiti()
            with open(datoteka , 'r') as f:
                for i in range(len(open("ispiti.txt").readlines())):
                    line = f.readline()
                    student = (line.splitlines()[0]).split("\t")
                    novi.dodaj(student[0] , student[1] , student[2])
                return novi

        def spremi_json(self , datoteka):
            with open(datoteka , 'w') as f:
                json.dump(self , f)


        @staticmethod
        def ucitaj_json(datoteka):
            with open(datoteka) as f:
                student = json.load(f)
                return student

print("*** TEST datoteka ***")
isp = Ispiti()
isp.dodaj("Ante Antic", "Linearna algebra", 5)
isp.dodaj("Ante Antic", "Programiranje 1", 4)
isp.dodaj("Marija Marijic", "Linearna algebra", 4)
isp.dodaj("Marija Marijic", "Matematicka analiza", 5)
isp.spremi_datoteka("ispiti.txt")
print(open("ispiti.txt").read())
isp = Ispiti.ucitaj_datoteka("ispiti.txt")
print(isp)

print("*** TEST json ***")
isp = Ispiti()
isp.dodaj("Ante Antić", "Linearna algebra", 5)
isp.dodaj("Ante Antić", "Programiranje 1", 4)
isp.dodaj("Ante Antić", "Linearna algebra", 4)
isp.dodaj("Ante Antić", "Matematička analiza", 5)
isp.spremi_json("ispiti.json")
print(open("ispiti.json").read())
isp = Ispiti.ucitaj_json("ispiti.txt")
print(isp)






