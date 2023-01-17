from collections import OrderedDict


temps =  [('2000', -4.4), ('2001', -2.5), ('2002', -4.4), ('2003', -9.5)]

def check(temps:list) -> OrderedDict:
    
    ordered_temps = OrderedDict(sorted(temps, key=lambda temp: temp[1], reverse=True))
    return ordered_temps

print(check(temps))