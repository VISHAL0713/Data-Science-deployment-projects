import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder
from sklearn.ensemble import RandomForestClassifier
import pickle


### reading the data
data = pd.read_csv(r'D:\Flask\diabetes.csv')
print(data)

## label encoder to transform data to numeric form
le_fu = LabelEncoder()

X = pd.DataFrame(columns=['FS','FU'])

X['FS'] = data['Fasting Sugar']
X['FU'] = le_fu.fit_transform(data['Frequent Unination'])

y = data['Diabetes']

##random forest classifier
classifier = RandomForestClassifier()
classifier.fit(X,y)
classifier.predict([[115,0]])


### dumping into pickle

with open('my_model','wb') as f:
    pickle.dump(classifier,f)


##reusing the same model again
with open('my_model','rb') as f:
    model = pickle.load(f)
    
model.predict([[160,1]])


