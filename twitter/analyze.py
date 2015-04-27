import pickle
import pandas as pd

with open('a_giants.pickle','rb') as handle:
    data = pickle.load(handle)

data = pd.DataFrame(data)
print(data[data['neg']>0]['text'])
