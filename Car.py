class Car:
    def __init__(self):
        self.Aantalcilinders = ""
        self.Aantalzitplaatsen = ""
        self.Brandstofverbruikbuitenweg = ""
        self.Brandstofverbruikgecombineerd = ""
        self.Brandstofverbruikstad = ""
        self.Cilinderinhoud = ""
        self.CO2uitstootgecombineerd = ""
        self.Datumeerstetoelating = ""
        self.Handelsbenaming = ""
        self.Hoofdbrandstof = ""
        self.Inrichting = ""
        self.Massaleegvoertuig = ""
        self.Merk = ""
        self.Milieuclassificatie = ""
        self.Nevenbrandstof = ""
        self.Toegestanemaximummassavoertuig = ""
        self.Vermogen = ""
        self.Zuinigheidslabel = ""

    def fillAspects(self, aspects):
        self.Aantalcilinders = aspects[0].strip()
        self.Aantalzitplaatsen = aspects[1].strip()
        self.Brandstofverbruikbuitenweg = aspects[2].strip()
        self.Brandstofverbruikgecombineerd = aspects[3].strip()
        self.Brandstofverbruikstad = aspects[4].strip()
        self.Cilinderinhoud = aspects[5].strip()
        self.CO2uitstootgecombineerd = aspects[6].strip()
        self.Datumeerstetoelating = aspects[7].strip()
        self.Handelsbenaming = aspects[8].strip()
        self.Hoofdbrandstof = aspects[9].strip()
        self.Inrichting = aspects[10].strip()
        self.Massaleegvoertuig = aspects[11].strip()
        self.Merk = aspects[12].strip()
        self.Milieuclassificatie = aspects[13].strip()
        self.Nevenbrandstof = aspects[14].strip()
        self.Toegestanemaximummassavoertuig = aspects[15].strip()
        self.Vermogen = aspects[16].strip()
        self.Zuinigheidslabel = aspects[17].strip()

    def addAspect(self, nameAspect, aspect):
        aspect = aspect.strip()
        if nameAspect == "Aantalcilinders":
            self.Aantalcilinders = aspect
        if nameAspect == "Brandstofverbruikgecombineerd":
            self.Brandstofverbruikgecombineerd = aspect
        if nameAspect == "Cilinderinhoud":
            self.Cilinderinhoud = aspect
        if nameAspect == "CO2uitstootgecombineerd":
            self.CO2uitstootgecombineerd = aspect
        if nameAspect == "Hoofdbrandstof":
            self.Hoofdbrandstof = aspect
        if nameAspect == "Massaleegvoertuig":
            self.Massaleegvoertuig = aspect
        if nameAspect == "Vermogen":
            self.Vermogen = aspect
        if nameAspect == "Zuinigheidslabel":
            self.Zuinigheidslabel = aspect

    def printType(self):
        return self.Merk + " " + self.Handelsbenaming

    def returnPrintable(self):
        printable = "" #[1:-1]
        printable += self.Aantalcilinders + ","
        printable += self.Aantalzitplaatsen + ","
        printable += self.Brandstofverbruikbuitenweg + ","
        printable += self.Brandstofverbruikgecombineerd + ","
        printable += self.Brandstofverbruikstad + ","
        printable += self.Cilinderinhoud + ","
        printable += self.CO2uitstootgecombineerd + ","
        printable += self.Datumeerstetoelating + ","
        printable += self.Handelsbenaming + ","
        printable += self.Hoofdbrandstof + ","
        printable += self.Inrichting + ","
        printable += self.Massaleegvoertuig + ","
        printable += self.Merk + ","
        printable += self.Milieuclassificatie + ","
        printable += self.Nevenbrandstof + ","
        printable += self.Toegestanemaximummassavoertuig + ","
        printable += self.Vermogen + ","
        printable += self.Zuinigheidslabel + "\n"
        return printable

    def convertBrandstofToFloat(self, brandstof):
        if brandstof == "Benzine":
            return 1.0
        elif brandstof == "Diesel":
            return 2.0
        elif brandstof == "Elektriciteit":
            return 3.0
        elif brandstof == "LPG (Liquified Petrol Gas)":
            return 4.0
        elif brandstof == "CNG (Compressed Natural Gas)":
            return 5.0
        elif brandstof == "Alcohol":
            return 6.0
        elif brandstof == "Waterstof":
            return 7.0

    def convertZuinigheidsLabelToFloat(self, zuinigheidsLabel):
        if zuinigheidsLabel == "A":
            return 1.0
        elif zuinigheidsLabel == "B":
            return 2.0
        elif zuinigheidsLabel == "C":
            return 3.0
        elif zuinigheidsLabel == "D":
            return 4.0
        elif zuinigheidsLabel == "E":
            return 5.0
        elif zuinigheidsLabel == "F":
            return 6.0
        elif zuinigheidsLabel == "G":
            return 7.0

    def returnLinRegList(self):
        linRegList = []
        linRegList.append(float(self.Aantalcilinders))
        linRegList.append(float(self.Cilinderinhoud))
        linRegList.append(float(self.Massaleegvoertuig))
        linRegList.append(float(self.Vermogen))
        return linRegList

    def returnList(self):
        attributeList = []
        attributeList.append((float( self.Aantalcilinders )))
        attributeList.append((float( self.Brandstofverbruikgecombineerd )))
        attributeList.append((float( self.Cilinderinhoud )))
        attributeList.append((float( self.CO2uitstootgecombineerd )))
        attributeList.append(( self.convertBrandstofToFloat(self.Hoofdbrandstof) ))
        attributeList.append((float( self.Massaleegvoertuig )))
        attributeList.append((float( self.Vermogen )))
        attributeList.append(( self.convertZuinigheidsLabelToFloat(self.Zuinigheidslabel) ))

        return attributeList


def compareCars(car1, car2):
    if (car1.Aantalcilinders == car2.Aantalcilinders and
    #car1.Aantalzitplaatsen == car2.Aantalzitplaatsen and 
    #car1.Brandstofverbruikbuitenweg == car2.Brandstofverbruikbuitenweg and
    car1.Brandstofverbruikgecombineerd == car2.Brandstofverbruikgecombineerd and
    #car1.Brandstofverbruikstad == car2.Brandstofverbruikstad and
    car1.Cilinderinhoud == car2.Cilinderinhoud and
    car1.CO2uitstootgecombineerd == car2.CO2uitstootgecombineerd and
    #car1.Datumeerstetoelating == car2.Datumeerstetoelating and
    #car1.Handelsbenaming == car2.Handelsbenaming and
    car1.Hoofdbrandstof == car2.Hoofdbrandstof and
    #car1.Inrichting == car2.Inrichting and
    car1.Massaleegvoertuig == car2.Massaleegvoertuig and
    #car1.Merk == car2.Merk and
    #car1.Milieuclassificatie == car2.Milieuclassificatie and
    #car1.Nevenbrandstof == car2.Nevenbrandstof and
    #car1.Toegestanemaximummassavoertuig == car2.Toegestanemaximummassavoertuig and
    car1.Vermogen == car2.Vermogen and
    car1.Zuinigheidslabel == car2.Zuinigheidslabel):
        return True

def similarityCars(car1, car2):
    similarityCars = 0
    similarityCars += (float(car1.Aantalcilinders) - float(car2.Aantalcilinders)) ** 2.0
    similarityCars += (float(car1.Brandstofverbruikgecombineerd) - float(car2.Brandstofverbruikgecombineerd)) ** 2.0
    similarityCars += (float(car1.Cilinderinhoud) - float(car2.Cilinderinhoud)) ** 2.0
    similarityCars += (float(car1.CO2uitstootgecombineerd) - float(car2.CO2uitstootgecombineerd)) ** 2.0
    if car1.Hoofdbrandstof != car2.Hoofdbrandstof:
        similarityCars += 100000
    similarityCars += (float(car1.Massaleegvoertuig) - float(car2.Massaleegvoertuig)) ** 2.0
    similarityCars += (float(car1.Vermogen) - float(car2.Vermogen)) ** 2.0
    if car1.Zuinigheidslabel != car2.Zuinigheidslabel:
        similarityCars += 100000
    return similarityCars