class patient:

    #patient's data
    def __init__(self, temperature = 0):
        self.data = {'complaint': "", 'heartrate': 0, 'temperature': temperature, 'infection': False, 'diagnosis':"" }

    #Function: Diagnose
    def diagnose(self):
        if self.data['temperature'] > 100:
            self.data['diagnosis'] = "dead"
        else:
            self.data['diagnosis'] = "alive"

    #Function: Print the diagnose
    def print_diagnose(self):
        print ("Your diagnonsis is: ", self.data['diagnosis'])

patients = []
patients.append(patient(102))

print (patients[0].data['temperature'])
