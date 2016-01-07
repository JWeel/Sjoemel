import csv #for reading in file

class Auto:
    def __init__(self, aspects):
        self.Aantalcilinders = aspects[0]
        self.Aantalzitplaatsen = aspects[1]
        self.Brandstofverbruikbuitenweg = aspects[2]
        self.Brandstofverbruikgecombineerd = aspects[3]
        self.Brandstofverbruikstad = aspects[4]
        self.Cilinderinhoud = aspects[5]
        self.CO2uitstootgecombineerd = aspects[6]
        self.Datumeerstetoelating = aspects[7]
        self.Handelsbenaming = aspects[8]
        self.Hoofdbrandstof = aspects[9]
        self.Inrichting = aspects[10]
        self.Massaleegvoertuig = aspects[11]
        self.Merk = aspects[12]
        self.Milieuclassificatie = aspects[13]
        self.Nevenbrandstof = aspects[14]
        self.Toegestanemaximummassavoertuig = aspects[15]
        self.Vermogen = aspects[16]
        self.Zuinigheidslabel = aspects[17]
    
    def printCar(self):
        print self.Merk, self.Handelsbenaming

    def returnPrintable(self):
        printable = "" #[1:-1]
        printable += self.Aantalcilinders[1:-1] + ","
        printable += self.Aantalzitplaatsen[2:-1] + ","
        printable += self.Brandstofverbruikbuitenweg[2:-1] + ","
        printable += self.Brandstofverbruikgecombineerd[2:-1] + ","
        printable += self.Brandstofverbruikstad[2:-1] + ","
        printable += self.Cilinderinhoud[2:-1] + ","
        printable += self.CO2uitstootgecombineerd[2:-1] + ","
        printable += self.Datumeerstetoelating[2:-1] + ","
        printable += self.Handelsbenaming[2:-1] + ","
        printable += self.Hoofdbrandstof[2:-1] + ","
        printable += self.Inrichting[2:-1] + ","
        printable += self.Massaleegvoertuig[2:-1] + ","
        printable += self.Merk[2:-1] + ","
        printable += self.Milieuclassificatie[2:-1] + ","
        printable += self.Nevenbrandstof[2:-1] + ","
        printable += self.Toegestanemaximummassavoertuig[2:-1] + ","
        printable += self.Vermogen[2:-1] + ","
        printable += self.Zuinigheidslabel[2:-1] + "\n"
        return printable




#splitts the data on the ';'.
class SKV(csv.excel):
    delimiter = ";"

csv.register_dialect("SKV", SKV)


def compareCars(car1, car2):
    if (car1.Aantalcilinders == car2.Aantalcilinders and
    car1.Aantalzitplaatsen == car2.Aantalzitplaatsen and 
    car1.Brandstofverbruikbuitenweg == car2.Brandstofverbruikbuitenweg and
    car1.Brandstofverbruikgecombineerd == car2.Brandstofverbruikgecombineerd and
    car1.Brandstofverbruikstad == car2.Brandstofverbruikstad and
    car1.Cilinderinhoud == car2.Cilinderinhoud and
    car1.CO2uitstootgecombineerd == car2.CO2uitstootgecombineerd and
    #car1.Datumeerstetoelating == car2.Datumeerstetoelating and
    car1.Handelsbenaming == car2.Handelsbenaming and
    car1.Hoofdbrandstof == car2.Hoofdbrandstof and
    car1.Inrichting == car2.Inrichting and
    car1.Massaleegvoertuig == car2.Massaleegvoertuig and
    car1.Merk == car2.Merk and
    car1.Milieuclassificatie == car2.Milieuclassificatie and
    car1.Nevenbrandstof == car2.Nevenbrandstof and
    car1.Toegestanemaximummassavoertuig == car2.Toegestanemaximummassavoertuig and
    car1.Vermogen == car2.Vermogen and
    car1.Zuinigheidslabel == car2.Zuinigheidslabel):
        return True


def getData(dataFile):
    x = []
    y = []
    with open(dataFile, "rU") as csvfile:
        aspects = ""
        aspects2 = ""
        cars = []
        reader = csv.reader(csvfile, "SKV")
        for row in reader:
            cars.append(Auto(row))
        j = 0
        print len(cars)
        uniqueCars = []
        uniqueCars.append(cars[0])
        
        f = open("naam.csv", 'w')
        for i in range(len(cars)):
            found = False
            for foundCars in uniqueCars:
                if compareCars(cars[i], foundCars):
                    found = True
                    break
            if not found:
                uniqueCars.append(cars[i])
                print i
                f.write(cars[i].returnPrintable())
        print len(uniqueCars)
        f.close()

if __name__ == '__main__':
    getData("minder_kolommen2.csv")