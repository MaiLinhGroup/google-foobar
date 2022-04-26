import fileinput

def solution(h, q):
    """Find the parent node of nodes in q
        in a perfect binary tree with height h.

    Args:
        h (int): height of the perfect binary tree with 1 <= h <= 30.
        q (list(int)): list of positive integers representing 
                        different flux converters, min length 1, 
                        max length 10000.
    Returns:
        p (list(int)): each element in p is the label of 
                        the converter that sits on top of 
                        the respective converter in q, 
                        or -1 if there is no such converter,
                        min length 1, max length 10000.
    """
    p = []
    for converter in q:
        if (converter == pow(2,h) - 1):
            p.append(-1)
        elif (right(converter)):
            p.append(converter + 1)
        else:
            node_h = height(converter)
            p.append(converter + pow(2,node_h))
    return p


def height(node):
    n = node + 1
    if ((n & (n-1) == 0) and n != 0):
        return n.bit_length() - 1

    i = node.bit_length() - 1
    x = pow(2,i) - 1
    return height(node-x)

def right(node):
    n = node + 1
    if ((n & (n-1) == 0) and n != 0): # left
        return False

    i = node.bit_length() - 1
    x = pow(2,i) - 1
    if (node == 2*x): # right
        return True

    return right(node-x)


if __name__ == '__main__':
    for line in fileinput.input():
        input = [int(s) for s in line.split(' ')]
        h = input[0]
        q = input[1:]
        print "solution(", h, ",", q, "): ", solution(h, q)