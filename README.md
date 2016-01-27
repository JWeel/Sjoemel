# Sjoemel

Hier staan de programma's die gebruikt zijn voor het Leren en Beslissen project. Deze programma's hebben gebruik gemaakt van de scikit-learn toolkit en zijn geschreven in python. Python en scikit-learn moeten dus geïnstalleerd zijn om deze programma's uit te voeren. Anaconda is een python distributie waarbij scikit-learn automatisch wordt geïnstalleerd, dus om deze programma's te gebruiken wordt aanbevolen om Anaconda te installeren.

<hr />

Nu volgt instructries over het uitvoeren van de programma's, en wat zij doen:

#### Car.py

Car.py bevat de class Car, alle auto's uit de database worden ingelezen als Car.py objecten, zodat alle informatie over de auto's wordt behouden.
	
Dit programma hoeft niet uitgevoerd te worden, want het wordt automatisch aangeroepen in anomalyDetection.py en DummyLinRegTester.py.

#### anomalyDetection.py

Voer dit programma uit met de volgende commando:

    python anomalyDetection.py

Dit programma runt de clustering algoritmes en lineaire regressie op de dataset.

#### DummyLinRegTester.py

Voer dit programma uit met de volgende commando:

    python DummyLinRegTester.py

Dit programma leest de dataset in en verlaagd van 21 (willekeurig uitgezochte) auto's de CO2Uitstoot met 5 t/m 25%. Vervolgens past het lineaire regressie toe op de aangepaste dataset. Het programma schrijft in de console welke (en hoeveel) dummies gevonden worden.