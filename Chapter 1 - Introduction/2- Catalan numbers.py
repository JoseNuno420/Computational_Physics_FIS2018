def Catalan_sequence_maxval(maxval):
    """Return Catalan Sequence until you pass the maxval barrier.
    
    :param maxval: int/float max value you want in your sequence.
    :return: str with the requested Catalan sequence.
    
    Sequence definition:
        C_0 = 1
        C_{n+1} = (4*n + 2)/(n + 2) * C_n
    """
    C_n1 = 1
    string = str(C_n1) + "\n"
    n = 1
    
    while C_n1 < maxval:
        C_n1 *= (4*n + 2)/(n + 2)
        string = string + str(C_n1) + "\n"
        n += 1
    return string
