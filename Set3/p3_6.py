tree = {'value': 13,
        'children': [{'value': 7, 'children': []},
                     {'value': 8,
                      'children': [{'value': 99, 'children': []},
                                   {'value': 16,
                                    'children': [{'value': 77, 'children': []}]},
                                   {'value': 42, 'children': []}]}]}

def tree_max(tree):
    # base case
    if len(tree['children']) == 0:
        return tree['value']
    else:
        highest_now = tree['value']
        for child in tree['children']:
            highest_child = binary_tree_max(child)
            if(highest_child > highest_now):
                highest_now = highest_child
        
    return highest_now

def binary_tree_max(tree):
    return tree_max(tree)

print(tree_max(tree))