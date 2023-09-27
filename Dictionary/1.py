# dictionary = A changeable unordered collection of unique key:value pairs fast because they use hashing,alloe us to access a value quickly.

states = {'Telangana':'Hyderabad',
          'Andhra':'Vizag',
          'timalnadu':'chennai'}

# print(states.keys())
# print(states.values())
# print(states.items())
states.update({'kerala':'wynad'})
states.update({'Andhra':'rajamendary'})
states.pop('timalnadu')
states.clear()
for keys,values in states.items():
    print(keys,values)