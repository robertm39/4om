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

def get_mcs_product_from_macros(macros):
    """
    Return a macro space macro product from the given list of macros.
    
    Parameters:
        macros: The macro list to return a macro product made from.
    """
#        print('get_mcs_macro:')
#        print(product)
#        print('end get_mcs_macro')
#    return utils.paren([utils.paren([utils.paren(macros)])])
    return utils.paren([utils.paren([utils.paren(macros)])])

def get_mcs_macro(product, name):
        """
        Return a macro space macro from the given mcs product.
        
        Parameters:
            product: The mcs product to return a macro made from. With triple parens (one because it'll be unwrapped, to to end up in the result).
#        """
#        print('get_mcs_macro:')
#        print(product)
#        print('end get_mcs_macro')
        return utils.paren([utils.normal(name),
                            utils.paren([utils.normal(name)]),
                            utils.paren([product])])

def sort_macros(mcs_product, mcs_names, macros):
    #mcs always counts as the last macro
#    print('sorting')
#    print(mcs_product)
    name_indices = {}
    i = 0
    for mcs_name in mcs_names:
        name_indices[utils.parse(mcs_name)] = len(macros)+i
        i += 1
        
    for i in range(0, len(mcs_product.children[0].children[0].children)):
        node = mcs_product.children[0].children[0].children[i]
        if is_macro(node):
            name_indices[utils.get_name(node)] = i
    
    name_key = lambda macro: name_indices[utils.get_name(macro)] #Secondary sort
    length_key = lambda macro: -len(utils.get_form(macro)) #Primary sort
    
    macros.sort(key=name_key) #This works because of stable sorting
    macros.sort(key=length_key)