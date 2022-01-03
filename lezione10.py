 class Model()

    def fit(self, data):

        pass

    def predict(self, data):

        pass
        
class IncrementModel(Model)

    def avg_increment(self, data):
        prev_item = None #variabile di supporto per il valore precedente

        incr=0 #per salavre l'incremento medio

        #calcolo l'incremento se sono al giro 1+ (prev_item non definito)
        for i in data:
            if prev_item is not None:

                incr=incr+(data[i]-prev_item)
                prev_item=i
        avg_incr=incr/(len(data)-1)
        return avg_incr

    def predict(self, data, n):
        #calcolo l'incremento medio sui dati della predict
        avg_incr=self.avg_increment(data)

        return data[-1]+avg_incr

class FitIncrementModel(IncrementModel):

    def fit(self, data):
        self.incr_medio_glo=self.avg_increment(data)

    def predict(self, data, n):
        
        parent_prediction=super().predict(data)

        parent_incr_tot=(parent_prediction)-data[-1]

        prediction_increment=(self.incr_medio_glo+parent_incr_tot)

        prediction=predict_data[-1]+prediction_increment

        return prediction
    


data[]=[8,19,31,41,50,52,60]
n=7
my_file=FitIncrementModel()
print(my_file.fit(data, n))
print(my_file.predict(data, n))
