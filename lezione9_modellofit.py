 class Model()

    def fit(self, data):

        raise NotImplementedError('Metodo non implementato')

    def predict(self, data):

        raise NotImplementedError('Metodo non implementato')
        
class IncrementModel(Model)

    def predict(self, data, n):
        self.data=data
        self.n=n
        #prev_value = None se usiamo for item in data
        #for item in data:
        i = 0
        if (data[] = None):
            raise Exception as e:
            print('i dati non sono presenti in lista')

        if(n>2):
            for i in data:
                incr=incr+(data[i+1]-data[i])
            incr=(incr/n)
        else:
            raise Exception as e:
            print('i mesi sono minori di 2')
        
        prediction=incr+data[n]
        return prediction

class FitIncrementModel(IncrementModel):

    def fit(self, data, n, incr_medio_glo):
        self.data=data
        self.n=n
        self.incr_medio_glo=incr_medio_glo

        n=n-3

        i=0
        for i in data:
            incr=incr+data([i+1]-data[i])
        incr_medio_glo=(incr/n)
        return incr_medio_glo
    
    def predict(self, data, n):
        
        incr_tot=((((super.predict.prediction)-data[n])+fit.incr_medio_glo)/2)
        return incr_tot


data[]=[8,19,31,41,50,52,60]
n=7
my_file=FitIncrementModel()
print(my_file.fit(data, n))
print(my_file.predict(data, n))
