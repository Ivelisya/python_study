import pickle
class Myclass:
    def __init__(self,name,value):
        self.name = name
        self.value = value
        self.internal_data = "this"

    def __getstate__(self):
        state = {'name' : self.name,'value':self.value}
        return state
    def __setstate__(self,state):
        self.name = state['name']
        self.value = state['value']
        self.internal_data = None
    def display(self):
        print(f"Name: {self.name}, Value: {self.value}, Internal Data: {self.internal_data}")
obj  = Myclass("My object",123)
obj.display()
filename = "my_class.pkl"
with open(filename,"wb") as f:
    pickle.dump(obj,f)
with open(filename,"rb") as f:
    load_f = pickle.load(f)
load_f.display()