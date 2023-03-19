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

        walker = node_chain
        new_node.set_data(walker.get_data())

        walker.set_data(walker.get_next())

        return new_node.set_next(copy(walker))
    
# def replace(node_chain, target, replacement):
#     walker = node_chain

#     if node_chain is None:
#         return None
    
#     if walker.get_data() == target:
#         return node_chain(replacement, replace(walker.get_next(), target, replacement))
    
#     return node_chain(walker.get_data(), replace(walker.get_next(),target,replacement))

#test
## vòng lặp
## 1
## newnode(1,copy(...))
#copy(N.node(2))


chain= N.node(1,N.node(2))

result = copy(chain)
expected = N.node(1,N.node(2))

if result == expected:
    print(True)

    
    


