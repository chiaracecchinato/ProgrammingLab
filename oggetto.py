class CSVFile():
    def __init__(self, name):
        self.name=name
    
    def get_data(self):
        my_file=open('shampoo_sales.csv', 'r')
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