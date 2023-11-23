# # dictionary = A changeable unordered collection of unique key:value pairs fast because they use hashing,alloe us to access a value quickly.

# states = {'Telangana':'Hyderabad',
#           'Andhra':'Vizag',
#           'timalnadu':'chennai'}

# # print(states.keys())
# # print(states.values())
# # print(states.items())
# states.update({'kerala':'wynad'})
# states.update({'Andhra':'rajamendary'})
# states.pop('timalnadu')
# states.clear()
# for keys,values in states.items():
#     print(keys,values)


n = 7
ar = [1,2,1,2,1,3,2]

pair_socks = {}
for socks in ar:
    if socks in pair_socks:
        pair_socks[socks] +=1
    else:
        pair_socks[socks] =1



total_pairs = 0

for count in pair_socks.values():
    total_pairs += count // 2


print(total_pairs)