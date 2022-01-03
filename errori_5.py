class CSVFile:
    def __init__(self, name):
        
        self.name = name
        
        self.can_read = True
        try:
            my_file = open(self.name, 'r')
            my_file.readline()
        except Exception as e:
            self.can_read = False
            print('Errore in apertura del file: "{}"'.format(e))
    
    def get_data(self):
        if not self.can_read:
            #se non va nell'init -> quindi è false -> file illeggibile
            print('Errore, file non aperto o illeggibile')

            #esco dalla funzione senza tornare nulla
            return None
        else:
            #inizializzo una lista per salvarci tutti i dati
            data = []

            my_file=open(self.name, 'r')
            for line in my_file:
                elements=line.split(',')

                #posso anche pulire il carattere di newline dall'ultimo elemento (\n) con la fuznione strip()
                elements[-1]=elements[-1].strip()
                if elements[0]!='Date':
                    data.append(elements)
            my_file.close()
            return data

#classe per file numericalcsv

class NumericalCSV(CSVFile):
    #richiamo la get_data del genitore
    def get_data(self):
        string_data=CSVFile.get_data(self)

    #preparo la lista per contenere i dati in formato numerico
        numerical_data = []

    #ciclo su tutte le righe corrispondenti al file originale
        for string_row in string_data:
        #preparo una lista di supprto per salvare la riga in 'formato' numerico (- primo elemento)
            numerical_row=[]

        #ciclo su tutti gli elementi della riga con un 'enumerate' così i è ancora libero -> posizione dell'elemento nella riga
            for i, element in enumerate(string_row):
                if i==0:
                #primo elemento lo lascio in formato string_data
                    numerical_row.append(element)

                else:
                #converto a float tutti gli altri -> metto anche l'errore nel caso in cui si rompa il ciclo altrimenti si salta di una riga
                    try:
                        numerical_row.append(float(element))
                    except Exceptionas as e:
                        print('Errore in conversione del valore "{}" a numerico: "{}"'.format(element,e))
                        break
        
        #devo aggiungere una riga in formato numerico alla lista esterna <=> ho processato tutti gli elementi
        #controllo pure la lunghezza ma avrei anche potuto mettere una variabile di supporto o fare 2 break a cascata
            if len(numerical_row) == len(string_row):
                numerical_data.append(numerical_row)
        
        return numerical_data

#corpo del programma

my_file = CSVFile(name='shampoo_sales.csv')
print('Nome del file: "{}"'.format(my_file.name))
print('Dati contenuti nel file: "{}"'.format(my_file.get_data()))

my_file_num=NumericalCSV(name='shampoo_sales.csv')
print('Nome del file: "{}"'.format(my_file_num.name))
print('Dati contenuti nel file: "{}"'.format(my_file_num.get_data()))