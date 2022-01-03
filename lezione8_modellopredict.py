class Model:

    def fit(self, data):

        raise NotImplementedError('Metodo non implementato')

    def predict(self, data):

        raise NotImplementedError('Metodo non implementato')
        
class IncrementModel(Model):

    def predict(self, data, n):
        #prev_value = None se usiamo for item in data
        #for item in data:
        i = 0
        if (data == None):
            print('i dati non sono presenti in lista')

        if(n>2):
            for i in data:
                incr=incr+(data[i+1]+data[i])
        else:
            print('i mesi sono minori di 2')
        
        prediction=incr+data[n]
        return prediction

data=[50,52,60]
