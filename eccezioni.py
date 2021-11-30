class CSVFile():
    def __init__(self, name):
        self.name=name
        #if name is not isinstance(name, ):
            raise Expection('Il nome del file non è una stringa')
    
    def get_data(self, start=None, end=None):
        if start is not isinstance((start&&end), int):
            raise Exception('valore inserito non numerico')
        my_file=open('shampoo_sales.csv', 'r')
        if start < 0:
            raise Execption('inizio non valido')
        if end > line:
            raise Exception('fine più grande delle linee totali')
        for line in my_file:
            elements=line.split(',')

        values = []

        if elements[0] != 'Date':
            date=elements[0]
            value_S=elements[1]

            values.append((date + ' ' + value_S))
        print(values)
        my_file.close()

my_file = CSVFile('shampoo_sales')
print(my_file.get_data())