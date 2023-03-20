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
        return N.node(node_chain.get_data(), copy(node_chain.get_next()))
      
        
def replace(node_chain, target, replacement):

    if node_chain is None:
        return None   
    
    if node_chain.get_data() == target:
        return N.node(replacement, replace(node_chain.get_next(), target, replacement))
    
    return  N.node(node_chain.get_data(), replace(node_chain.get_next(),target,replacement))


