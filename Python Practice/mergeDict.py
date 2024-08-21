

dict1 = {'a':10,'b':20}
dict2 = {'b':30,'c':40}

merged = dict1

for key in dict2:
    if key in merged:
        merged[key] += dict2[key]
    else:
        merged[key] = dict2[key]

print(merged)