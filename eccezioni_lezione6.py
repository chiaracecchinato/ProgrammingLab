class CSVFile():
    def __init__(self, name):
        try:
            self.name=name
        except:
            #if name is not isinstance(name, str):
            print('Il nome del file non è una stringa')
    
    def get_data(self, start=None, end=None):
        self.start=start
        self.end=end
        if self.start is not isinstance((self.start, int):
            print('valore inserito non numerico')
        else:
            my_file=open('shampoo_sales.csv', 'r')
            if start < 0:
                print('inizio non valido')
        if end > line:
            print('fine più grande delle linee totali')
        else:
            for line in my_file:
                elements=line.split(',')
                values = []
                if elements[0] != 'Date':
                    date=elements[0]
                    value_S=elements[1]
                    values.append((date + ' ' + value_S))
        print(values)
        my_file.close()

my_file = CSVFile(name='shampoo_sales.csv')
my_file.get_data(start=3, end=7)