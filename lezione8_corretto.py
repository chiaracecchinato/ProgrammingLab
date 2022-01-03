class Model():

    def fit(self, data):
        pass

    def predict(self, data):
        pass
        
class IncrementModel(Model):

    def __str__(self):
        return 'IncrementModel'

    def compute_avg_increment(self, data):
        #variabile di supporto per valore precdente
        prev_item=None
        n=len(data)
        #per l'incremento medio
        increments=0
        if data is None:
            print('i dati non sono presenti in lista')
        elif n>2:
            for item in data:
            #calcolo l'incremento
                if prev_item is not None:
                    increments+=item-prev_item
                    prev_item=item

            avg_increment=increments/(len(data)-1)
        else:
            print('i mesi sono minori di 2')

        return avg_increment

    def predict(self, predict_data):
        avg_increment=self.compute_avg_increment(predict_data)
        
        return predict_data[-1]+avg_increment

data=[50,52,60]
increment_model=IncrementModel()
prediction=increment_model.predict(data)
if not prediction==65:
    print('IncrementModel sul dataset di test non mi torna 65 ma "{}"'.format(prediction))
else:
    print('FitIncrementModel test passed')