def generate_parenthesis(n):
    '''
    Generate matched parenthesis with n number of open and closed brackets
    Example 
    1 -> ()
    2 -> (()), ()()
    3-> ((())), (()()), (())(), ()(()), ()()()
    '''
    result = []   # To keep track of final result
    generate_n_matched_paren_strings(n, n, "", result)
    return result

def generate_n_matched_paren_strings(l , r, s, result):
    if l == 0 and r == 0:   # If both zero then we got the final string
        result.append(s)
        return
    if l > 0:   # First go depth first since left parenthesis comes first
        generate_n_matched_paren_strings(l - 1, r, s + "(", result)
    if l < r:   # Only go right if left is less than right
        generate_n_matched_paren_strings(l, r - 1, s + ")", result)

if __name__ == '__main__':
    print(generate_parenthesis(3))