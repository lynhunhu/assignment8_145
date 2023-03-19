#Name: Nhu Nhu Ly
#NSID: cvd326
#instructor's name: Eric Neufeld
#student number: 11333935
#course number: 27177
#lab section: Monday 1:30 - 2:50 - 28623

import node as N


def to_string(node_chain):

    if node_chain is None:
        return None
    
    elif node_chain.get_next() is None:
        return '[ {} | *-]'.format(node_chain.get_data())
    
    else:
        return '[ {} | *-]-->'.format(node_chain.get_data()) + to_string(node_chain.get_next())
    


def copy(node_chain):
    if node_chain is None:
        return None
    
    else:
        
        new_node = N.node(None)
        new_node.__next = node_chain.get_next()
        return new_node

def replace(node_chain, target, replacement):
    walker = node_chain

    if node_chain is None:
        return None
    
    if walker.get_data() == target:
        return node_chain(replacement, replace(walker.get_next(), target, replacement))
    
    return node_chain(walker.get_data(), replace(walker.get_next(),target,replacement))

#test

chain1 = N.node(1,N.node(1,N.node(9)))
chain1before = chain1
print("Chain1 before:")
status = ""
while not chain1before is None:
    if(chain1before.get_next() is None):
        status+="[{} | /]".format(chain1before.get_data())
    else:
        status+="[{} |*-]-->".format(chain1before.get_data())
    chain1before = chain1before.get_next()
print(status)
replace(chain1,1,10)
print("Chain1 after:")
status_after=""
while not chain1 is None:
    if(chain1.get_next() is None):
        status_after+="[{} | /]".format(chain1.get_data())
    else:
        status_after+="[{} |*-]-->".format(chain1.get_data())
    chain1 = chain1.get_next()
print(status_after)

    
    


