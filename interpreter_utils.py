# -*- coding: utf-8 -*-
"""
Created on Mon Dec 24 10:46:23 2018

@author: rober
"""

import utils
from node import NodeType

NORMAL, CAPTURE, PAREN, SQUARE, CURLY, = NodeType.NORMAL, NodeType.CAPTURE, NodeType.PAREN, NodeType.SQUARE, NodeType.CURLY

def is_macro(node):
    """
    Return whether node is a macro.
    
    Parameters:
        nodes: The node to check for being a macro.
    """
    if node.node_type is PAREN:
        if len(node.children) == 3:
            name, form, product = node.children
            return name.node_type in [NORMAL, CAPTURE] and form.node_type is PAREN and product.node_type is PAREN
        else:
            return False
    else:
        return False

def get_parsed(line):
        """
        Return the line, parsed into a 4om expression.
        
        Parameters:
            line: The line to parse.
        """
        tokens = utils.tokenize(line)
        result = [utils.parse(token) for token in tokens]
        return result

def get_mcs_macro(product):
        """
        Return a macro space macro from the given mcs product.
        
        Parameters:
            product: The mcs product to return a macro made from.
        """
        return utils.bracket(PAREN, children=[utils.normal('mcs'),
                                              utils.bracket(PAREN, [utils.normal('mcs')]),
                                              utils.bracket(PAREN, #Do need both unwraps
                                                            [utils.bracket(PAREN, 
                                                                           [product])])])

def sort_macros(mcs_product, macros):
    #mcs always counts as the last macro
    name_indices = {utils.parse('mcs'):len(macros)}
        
    for i in range(0, len(mcs_product.children[0].children)):
        node = mcs_product.children[0].children[i]
        if is_macro(node):
            name_indices[utils.get_name(node)] = i
    
    name_key = lambda macro: name_indices[utils.get_name(macro)] #Secondary sort
    length_key = lambda macro: -len(utils.get_form(macro)) #Primary sort
    
    macros.sort(key=name_key) #This works because of stable sorting
    macros.sort(key=length_key)