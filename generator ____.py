# dict1={i+999:f"product no {i} price "for i in range(1,10)}
# dict1={x:y for y,x in dict1.items()}
# print(dict1)
dictt={i:f"product no{i}"for i in range(1,10)}
dicts={x:y for y,x in dictt.items()}
print(dictt)
print(dicts)