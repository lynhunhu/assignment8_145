#Name: Nhu Nhu Ly
#NSID: cvd326
#instructor's name: Eric Neufeld
#student number: 11333935
#course number: 27177
#lab section: Monday 1:30 - 2:50 - 28623

import a8q3 as Q3
import node as N

##Testing to_string(node_chain)

#Empty chain

case1 = "Testing an empty chain --- to_string(node_chain)"
expected1 = None
chain1 = None
result1 = Q3.to_string(chain1)

if result1 == expected1:
    print("There is nothing inputted, please retry.")
    print("{} --- Expected {} and obtained {} --- Successfully\n".format(case1,expected1,result1))

else:
    print("{} --- Error in function...".format(case1))


#Test a chain with one node

case2 = "Testing a chain with one node --- to_string(node_chain)"
chain2 = N.node(89)
expected2 = '[ 89 | *-]'
result2 = Q3.to_string(chain2)

if result2 == expected2:
    print("{} --- Expected {} and obtained {} --- Successfully\n".format(case2,expected2,result2))

else:
    print("{} --- Error in function...".format(case2))

#Test a chain with several nodes
case3 = "Testing a chain with several nodes --- to_string(node_chain)"
chain3 = N.node(89,N.node(22))
expected3 = '[ 89 | *-]-->[ 22 | *-]'
result3 = Q3.to_string(chain3)

if result3 == expected3:
    print("{} --- Expected {} and obtained {} --- Successfully\n".format(case3,expected3,result3))

else:
    print("{} --- Error in function...".format(case3))
#***********

case4 = "Testing a chain with several nodes --- to_string(node_chain)"
chain4 = N.node(89,N.node(22,N.node(24,N.node(90,N.node(38,N.node(102))))))
expected4 = '[ 89 | *-]-->[ 22 | *-]-->[ 24 | *-]-->[ 90 | *-]-->[ 38 | *-]-->[ 102 | *-]'
result4 = Q3.to_string(chain4)

if result4 == expected4:
    print("{} --- Expected {} and obtained {} --- Successfully\n".format(case4,expected4,result4))

else:
    print("{} --- Error in function...".format(case4))

###########################
#Testing copy(node_chain)
print("**************************")
#An empty chain
case5 = 'Testing an empty chain --- copy(node_chain)'
chain5 = None
expected5 = None
result5 = Q3.copy(chain5)

if result5 == expected5:
    print("{} --- Expected {} and obtained {} --- Successfully\n".format(case5, expected5,result5))

else:
    print("Error in function...")

#A chain with one node
case6 = 'Testing a chain with one node --- copy(node_chain)'
chain6 = N.node(23)
expected6 = N.node(23)
result6 = Q3.copy(chain6)

if result6.get_data() == expected6.get_data():
    print('{} --- expected {} and obtained {} --- Successfully\n'.format(case6, result6.get_data(), expected6.get_data()))

else:
    print("{} --- Error in function...".format(case6))

#A chain with several nodes

case7 = 'Testing a chain with several nodes --- copy(node_chain)'
chain7 = N.node(23,N.node(90,N.node(34,N.node(45))))
result7 = Q3.copy(chain7)

while result7 is not None:
    if result7.get_data() == chain7.get_data():
        print("{} --- Node expected {} and obtained {} --- Successfully\n".format(case7, result7.get_data(), chain7.get_data()))
        result7 = result7.get_next()
        chain7 = chain7.get_next()

    else:
        print('A node turned out unexpectedly... Please retry')
        result7 = result7.get_next()
        chain7 = chain7.get_next()

print('********************')

############
#Testing replace(node_chain, target, replacement)

#An empty chain
case8 = 'Tesing an empty chain -- replace(node_chain, target, replacement)'
chain8 = None
expected8 = None
result8 = Q3.replace(chain8, 8,10)

if result8 == expected8:
    print("{} --- Expected {} and obtained {} --- Successfully\n".format(case8, expected8,result8))
    
else:
    print("{} --- Error in function".format(case8))

#A chain with no replacement

case9 = 'Testing a chain with no replacement -- replace(node_chain, target, replacement)'
chain9 = N.node(23,N.node(22))
result9 = Q3.replace(chain9, None, None)

while result9 is not None:
    if result9.get_data() == chain9.get_data():
        print("{} --- Node expected {} and obtained {} --- Successfully\n".format(case9, result9.get_data(), chain9.get_data()))
        result9 = result9.get_next()
        chain9 = chain9.get_next()

    else:
        print("{} --- Error in function...".format(case9))
        result9 = result9.get_next()
        chain9 = chain9.get_next()

#A chain with several replacements
case10 = 'Testing a chain with several replacements -- replace(node_chain, target, replacement)'
chain10 = N.node(23,N.node(22,N.node(23,N.node(9,N.node(23,N.node(65))))))
expected10 = N.node(0,N.node(22,N.node(0,N.node(9,N.node(0,N.node(65))))))
result10 = Q3.replace(chain10, 23, 0)

while result10 is not None:
    if result10.get_data() == expected10.get_data():
        print("{} --- Node expected {} and obtained {} --- Successfully\n".format(case10, result10.get_data(), expected10.get_data()))
        result10 = result10.get_next()
        expected10 = expected10.get_next()

    else:
        print("{} --- Error in function...\n".format(case10))
        expected10 = expected10.get_next()
        expected10 = expected10.get_next()

