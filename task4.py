#write a program to create a list of n integer values and do the following
 L1=['20','30','40','50','60']
 # a) add an item in to the list (using function)
 L1.append('70')
print(L1)
['20', '30', '40', '50', '60', '70']
 # b) delete(using function)
L1.remove('30')
print(L1)
['20', '40', '50', '60', '70']
 # c) store the largest number frrpm the list to a variable
 print(max(L1))
70
 # d) store the smallest number from the list to a variable
 print(min(L1))
20
 #create a tuple and point the reverse of the created tuple
 tuple = ('1','2','3','hello','3.14')
>>> reversedtuples = tuple[::-1]
 print(reversedtuples)
('3.14', 'hello', '3', '2', '1')
 #create a tuple and convert tuple into list
tuple = ('405','506','607','3.45','hello')
 list = list(tuple)
 print(type(list))
<class 'list'>
print(list)
['405', '506', '607', '3.45', 'hello']
