class CSVFile():
    def __init__(self, name):
        self.name=name
    
    def get_data(self):
        my_file=open('shampoo_sales.csv', 'r')
        for line in my_file:
            elements=line.split(',')
            elements[-1]=elements[-1].strip()
            values = []
            data = []
            
            if elements[0] != 'Date':
                date=elements[0]
                value_S=elements[1]
                data.append(date)
                values.append(str(value_S))
                #lista_finale.append(data+values)
                
            print(data+values)
        my_file.close()

my_file = CSVFile('shampoo_sales')
my_file.get_data()