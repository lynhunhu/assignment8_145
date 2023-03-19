
def copy(node_chain=N.node):
    
    if node_chain is None:
        return None
    
    else:
        #new_node = N.node(None)

        walker = node_chain
        new_node.set_data(walker.get_data())

        walker.set_data(walker.get_next())

        return new_node.set_next(copy(walker))
    

    


