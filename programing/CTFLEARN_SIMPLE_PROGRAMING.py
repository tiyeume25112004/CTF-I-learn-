'''
the code must be
'''
# counter=0
# def check(line):
#         num1 = int(line.count('1'))
#         num0 = int(line.count('0'))
#         if((num0>0 and num0 % 3 == 0) or (num1 >0 and num1 % 2 ==0)):
#             return '1'
#         else:
#             return '0'
# with open('data.txt', 'r') as f:
#     for line in f:
#         counter+=int(check(line))
# print(counter)

'''
but the ctf says no, the bullshit code belike
'''
counter=0
def check(line):
        num1 = int(line.count('1'))
        num0 = int(line.count('0'))
        if(num0 % 3 == 0 or num1 % 2 ==0):
            return '1'
        else:
            return '0'
with open('data.txt', 'r') as f:
    for line in f:
        counter+=int(check(line))
print(counter)


        


        
