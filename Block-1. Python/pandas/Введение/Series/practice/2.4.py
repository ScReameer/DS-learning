import pandas as pd


names = ['chlorhexidine', 'cyntomycin', 'afobazol']
counts = [15, 18, 7]

def create_medications(names, counts):
    
    medications = pd.Series(data=counts, index=names)
    return medications

def get_percent(medications, name):
    
    get_count = medications.loc[name]
    percent = get_count / sum(medications.to_list()) * 100
    return percent

medications = create_medications(names, counts)

print(get_percent(medications, "chlorhexidine")) #37.5