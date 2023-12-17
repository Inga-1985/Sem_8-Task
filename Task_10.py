import pandas as pd
import random

lst = ['robot'] * 10 + ['human'] * 10
random.shuffle(lst)

data = pd.DataFrame({'whoAmI': lst})
one_hot_encoded = pd.DataFrame(columns=set(lst))

for value in set(lst):
    one_hot_encoded[value] = (data['whoAmI'] == value).astype(int)

one_hot_encoded.head()