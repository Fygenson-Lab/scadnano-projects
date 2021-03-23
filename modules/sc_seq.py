def sequence(seq_name, start, end):
    """Given a sequence name and range, returns the sequence in that range"""
    if seq_name == 'm13':
        seq = m13_sequence(start, end)
    elif seq_name == 'p3024':
        seq = p3024_sequence(start, end)
    elif seq_name == 'p768':
        seq = p768_sequence(start, end)
    else:
        raise Exception("Error in sc_seq.sequence(), sequence {} has not been added to the sequence module".format(seq_name))
    return seq

def m13_sequence(start, end):
    """Given a range, returns the m13 sequence in that range"""
    index = 577
    m13 = 'AATGCTACTACTATTAGTAGAATTGATGCCACCTTTTCAGCTCGCGCCCCAAATGAAAATATAGCTAAACAGGTTATTGACCATTTGCGAAATGTATCTAATGGTCAAACTAAATCTACTCGTTCGCAGAATTGGGAATCAACTGTTATATGGAATGAAACTTCCAGACACCGTACTTTAGTTGCATATTTAAAACATGTTGAGCTACAGCATTATATTCAGCAATTAAGCTCTAAGCCATCCGCAAAAATGACCTCTTATCAAAAGGAGCAATTAAAGGTACTCTCTAATCCTGACCTGTTGGAGTTTGCTTCCGGTCGGTTCGCTTTGAAGCTCGAATTAAAACGCGATATTTGAAGTCTTTCGGGCTTCCTCTTAATCTTTTTGATGCAATCCGCTTTGCTTCTGACTATAATAGTCAGGGTAAAGACCTGATTTTTGATTTATGGTCATTCTCGTTTTCTGAACTGTTTAAAGCATTTGAGGGGGATTCAATGAATATTTATGACGATTCCGCAGTATTGGACGCTATCCAGTCTAAACATTTTACTATTACCCCCTCTGGCAAAACTTCTTTTGCAAAAGCCTCTCGCTATTTTGGTTTTTATCGTCGTCTGGTAAACGAGGGTTATGATAGTGTTGCTCTTACTATGCCTCGTAATTCCTTTTGGCGTTATGTATCTGCATTAGTTGAATGTGGTATTCCTAAATCTCAACTGATGAATCTTTCTACCTGTAATAATGTTGTTCCGTTAGTTCGTTTTATTAACGTAGATTTTTCTTCCCAACGTCCTGACTGGTATAATGAGCCAGTTCTTAAAATCGCATAAGGTAATTCACAATGATTAAAGTTGAAATTAAACCATCTCAAGCCCAATTTACTACTCGTTCTGGTGTTTCTCGTCAGGGCAAGCCTTATTCACTGAATGAGCAGCTTTGTTACGTTGATTTGGGTAATGAATATCCGGTTCTTGTCAAGATTACTCTTGATGAAGGTCAGCCAGCCTATGCGCCTGGTCTGTACACCGTTCATCTGTCCTCTTTCAAAGTTGGTCAGTTCGGTTCCCTTATGATTGACCGTCTGCGCCTCGTTCCGGCTAAGTAACATGGAGCAGGTCGCGGATTTCGACACAATTTATCAGGCGATGATACAAATCTCCGTTGTACTTTGTTTCGCGCTTGGTATAATCGCTGGGGGTCAAAGATGAGTGTTTTAGTGTATTCTTTTGCCTCTTTCGTTTTAGGTTGGTGCCTTCGTAGTGGCATTACGTATTTTACCCGTTTAATGGAAACTTCCTCATGAAAAAGTCTTTAGTCCTCAAAGCCTCTGTAGCCGTTGCTACCCTCGTTCCGATGCTGTCTTTCGCTGCTGAGGGTGACGATCCCGCAAAAGCGGCCTTTAACTCCCTGCAAGCCTCAGCGACCGAATATATCGGTTATGCGTGGGCGATGGTTGTTGTCATTGTCGGCGCAACTATCGGTATCAAGCTGTTTAAGAAATTCACCTCGAAAGCAAGCTGATAAACCGATACAATTAAAGGCTCCTTTTGGAGCCTTTTTTTTGGAGATTTTCAACGTGAAAAAATTATTATTCGCAATTCCTTTAGTTGTTCCTTTCTATTCTCACTCCGCTGAAACTGTTGAAAGTTGTTTAGCAAAATCCCATACAGAAAATTCATTTACTAACGTCTGGAAAGACGACAAAACTTTAGATCGTTACGCTAACTATGAGGGCTGTCTGTGGAATGCTACAGGCGTTGTAGTTTGTACTGGTGACGAAACTCAGTGTTACGGTACATGGGTTCCTATTGGGCTTGCTATCCCTGAAAATGAGGGTGGTGGCTCTGAGGGTGGCGGTTCTGAGGGTGGCGGTTCTGAGGGTGGCGGTACTAAACCTCCTGAGTACGGTGATACACCTATTCCGGGCTATACTTATATCAACCCTCTCGACGGCACTTATCCGCCTGGTACTGAGCAAAACCCCGCTAATCCTAATCCTTCTCTTGAGGAGTCTCAGCCTCTTAATACTTTCATGTTTCAGAATAATAGGTTCCGAAATAGGCAGGGGGCATTAACTGTTTATACGGGCACTGTTACTCAAGGCACTGACCCCGTTAAAACTTATTACCAGTACACTCCTGTATCATCAAAAGCCATGTATGACGCTTACTGGAACGGTAAATTCAGAGACTGCGCTTTCCATTCTGGCTTTAATGAGGATTTATTTGTTTGTGAATATCAAGGCCAATCGTCTGACCTGCCTCAACCTCCTGTCAATGCTGGCGGCGGCTCTGGTGGTGGTTCTGGTGGCGGCTCTGAGGGTGGTGGCTCTGAGGGTGGCGGTTCTGAGGGTGGCGGCTCTGAGGGAGGCGGTTCCGGTGGTGGCTCTGGTTCCGGTGATTTTGATTATGAAAAGATGGCAAACGCTAATAAGGGGGCTATGACCGAAAATGCCGATGAAAACGCGCTACAGTCTGACGCTAAAGGCAAACTTGATTCTGTCGCTACTGATTACGGTGCTGCTATCGATGGTTTCATTGGTGACGTTTCCGGCCTTGCTAATGGTAATGGTGCTACTGGTGATTTTGCTGGCTCTAATTCCCAAATGGCTCAAGTCGGTGACGGTGATAATTCACCTTTAATGAATAATTTCCGTCAATATTTACCTTCCCTCCCTCAATCGGTTGAATGTCGCCCTTTTGTCTTTGGCGCTGGTAAACCATATGAATTTTCTATTGATTGTGACAAAATAAACTTATTCCGTGGTGTCTTTGCGTTTCTTTTATATGTTGCCACCTTTATGTATGTATTTTCTACGTTTGCTAACATACTGCGTAATAAGGAGTCTTAATCATGCCAGTTCTTTTGGGTATTCCGTTATTATTGCGTTTCCTCGGTTTCCTTCTGGTAACTTTGTTCGGCTATCTGCTTACTTTTCTTAAAAAGGGCTTCGGTAAGATAGCTATTGCTATTTCATTGTTTCTTGCTCTTATTATTGGGCTTAACTCAATTCTTGTGGGTTATCTCTCTGATATTAGCGCTCAATTACCCTCTGACTTTGTTCAGGGTGTTCAGTTAATTCTCCCGTCTAATGCGCTTCCCTGTTTTTATGTTATTCTCTCTGTAAAGGCTGCTATTTTCATTTTTGACGTTAAACAAAAAATCGTTTCTTATTTGGATTGGGATAAATAATATGGCTGTTTATTTTGTAACTGGCAAATTAGGCTCTGGAAAGACGCTCGTTAGCGTTGGTAAGATTCAGGATAAAATTGTAGCTGGGTGCAAAATAGCAACTAATCTTGATTTAAGGCTTCAAAACCTCCCGCAAGTCGGGAGGTTCGCTAAAACGCCTCGCGTTCTTAGAATACCGGATAAGCCTTCTATATCTGATTTGCTTGCTATTGGGCGCGGTAATGATTCCTACGATGAAAATAAAAACGGCTTGCTTGTTCTCGATGAGTGCGGTACTTGGTTTAATACCCGTTCTTGGAATGATAAGGAAAGACAGCCGATTATTGATTGGTTTCTACATGCTCGTAAATTAGGATGGGATATTATTTTTCTTGTTCAGGACTTATCTATTGTTGATAAACAGGCGCGTTCTGCATTAGCTGAACATGTTGTTTATTGTCGTCGTCTGGACAGAATTACTTTACCTTTTGTCGGTACTTTATATTCTCTTATTACTGGCTCGAAAATGCCTCTGCCTAAATTACATGTTGGCGTTGTTAAATATGGCGATTCTCAATTAAGCCCTACTGTTGAGCGTTGGCTTTATACTGGTAAGAATTTGTATAACGCATATGATACTAAACAGGCTTTTTCTAGTAATTATGATTCCGGTGTTTATTCTTATTTAACGCCTTATTTATCACACGGTCGGTATTTCAAACCATTAAATTTAGGTCAGAAGATGAAATTAACTAAAATATATTTGAAAAAGTTTTCTCGCGTTCTTTGTCTTGCGATTGGATTTGCATCAGCATTTACATATAGTTATATAACCCAACCTAAGCCGGAGGTTAAAAAGGTAGTCTCTCAGACCTATGATTTTGATAAATTCACTATTGACTCTTCTCAGCGTCTTAATCTAAGCTATCGCTATGTTTTCAAGGATTCTAAGGGAAAATTAATTAATAGCGACGATTTACAGAAGCAAGGTTATTCACTCACATATATTGATTTATGTACTGTTTCCATTAAAAAAGGTAATTCAAATGAAATTGTTAAATGTAATTAATTTTGTTTTCTTGATGTTTGTTTCATCATCTTCTTTTGCTCAGGTAATTGAAATGAATAATTCGCCTCTGCGCGATTTTGTAACTTGGTATTCAAAGCAATCAGGCGAATCCGTTATTGTTTCTCCCGATGTAAAAGGTACTGTTACTGTATATTCATCTGACGTTAAACCTGAAAATCTACGCAATTTCTTTATTTCTGTTTTACGTGCAAATAATTTTGATATGGTAGGTTCTAACCCTTCCATTATTCAGAAGTATAATCCAAACAATCAGGATTATATTGATGAATTGCCATCATCTGATAATCAGGAATATGAGATAATTCCGCTCCTTCTGGTGGTTTCTTTGTTCCGCAAAATGATAATGTTACTCAAACTTTTAAAATTAATAACGTTCGGGCAAAGGATTTAATACGAGTTGTCGAATTGTTTGTAAAGTCTAATACTTCTAAATCCTCAAATGTATTATCTATTGACGGCTCTAATCTATTAGTTGTTAGTGCTCCTAAAGATATTTTAGATAACCTTCCTCAATTCCTTTCAACTGTTGATTTGCCAACTGACCAGATATTGATTGAGGGTTTGATATTTGAGGTTCAGCAAGGTGATGCTTTAGATTTTTCATTTGCTGCTGGCTCTCAGCGTGGCACTGTTGCAGGCGGTGTTAATACTGACCGCCTCACCTCTGTTTTATCTTCTGCTGGTGGTTCGTTCGGTATTTTTAATGGCGATGTTTTAGGGCTATCAGTTCGCGCATTAAAGACTAATAGCCATTCAAAAATATTGTCTGTGCCACGTATTCTTACGCTTTCAGGTCAGAAGGGTTCTATCTCTGTTGGCCAGAATGTCCCTTTTATTACTGGTCGTGTGACTGGTGAATCTGCCAATGTAAATAATCCATTTCAGACGATTGAGCGTCAAAATGTAGGTATTTCCATGAGCGTTTTTCCTGTTGCAATGGCTGGCGGTAATATTGTTCTGGATATTACCAGCAAGGCCGATAGTTTGAGTTCTTCTACTCAGGCAAGTGATGTTATTACTAATCAAAGAAGTATTGCTACAACGGTTAATTTGCGTGATGGACAGACTCTTTTACTCGGTGGCCTCACTGATTATAAAAACACTTCTCAGGATTCTGGCGTACCGTTCCTGTCTAAAATCCCTTTAATCGGCCTCCTGTTTAGCTCCCGCTCTGATTCTAACGAGGAAAGCACGTTATACGTGCTCGTCAAAGCAACCATAGTACGCGCCCTGTAGCGGCGCATTAAGCGCGGCGGGTGTGGTGGTTACGCGCAGCGTGACCGCTACACTTGCCAGCGCCCTAGCGCCCGCTCCTTTCGCTTTCTTCCCTTCCTTTCTCGCCACGTTCGCCGGCTTTCCCCGTCAAGCTCTAAATCGGGGGCTCCCTTTAGGGTTCCGATTTAGTGCTTTACGGCACCTCGACCCCAAAAAACTTGATTTGGGTGATGGTTCACGTAGTGGGCCATCGCCCTGATAGACGGTTTTTCGCCCTTTGACGTTGGAGTCCACGTTCTTTAATAGTGGACTCTTGTTCCAAACTGGAACAACACTCAACCCTATCTCGGGCTATTCTTTTGATTTATAAGGGATTTTGCCGATTTCGGAACCACCATCAAACAGGATTTTCGCCTGCTGGGGCAAACCAGCGTGGACCGCTTGCTGCAACTCTCTCAGGGCCAGGCGGTGAAGGGCAATCAGCTGTTGCCCGTCTCACTGGTGAAAAGAAAAACCACCCTGGCGCCCAATACGCAAACCGCCTCTCCCCGCGCGTTGGCCGATTCATTAATGCAGCTGGCACGACAGGTTTCCCGACTGGAAAGCGGGCAGTGAGCGCAACGCAATTAATGTGAGTTAGCTCACTCATTAGGCACCCCAGGCTTTACACTTTATGCTTCCGGCTCGTATGTTGTGTGGAATTGTGAGCGGATAACAATTTCACACAGGAAACAGCTATGACCATGATTACGAATTCGAGCTCGGTACCCGGGGATCCTCTAGAGTCGACCTGCAGGCATGCAAGCTTGGCACTGGCCGTCGTTTTACAACGTCGTGACTGGGAAAACCCTGGCGTTACCCAACTTAATCGCCTTGCAGCACATCCCCCTTTCGCCAGCTGGCGTAATAGCGAAGAGGCCCGCACCGATCGCCCTTCCCAACAGTTGCGCAGCCTGAATGGCGAATGGCGCTTTGCCTGGTTTCCGGCACCAGAAGCGGTGCCGGAAAGCTGGCTGGAGTGCGATCTTCCTGAGGCCGATACTGTCGTCGTCCCCTCAAACTGGCAGATGCACGGTTACGATGCGCCCATCTACACCAACGTGACCTATCCCATTACGGTCAATCCGCCGTTTGTTCCCACGGAGAATCCGACGGGTTGTTACTCGCTCACATTTAATGTTGATGAAAGCTGGCTACAGGAAGGCCAGACGCGAATTATTTTTGATGGCGTTCCTATTGGTTAAAAAATGAGCTGATTTAACAAAAATTTAATGCGAATTTTAACAAAATATTAACGTTTACAATTTAAATATTTGCTTATACAATCTTCCTGTTTTTGGGGCTTTTCTGATTATCAACCGGGGTACATATGATTGACATGCTAGTTTTACGATTACCGTTCATCGATTCTCTTGTTTGCTCCAGACTCTCAGGCAATGACCTGATAGCCTTTGTAGATCTCTCAAAAATAGCTACCCTCTCCGGCATTAATTTATCAGCTAGAACGGTTGAATATCATATTGATGGTGATTTGACTGTCTCCGGCCTTTCTCACCCTTTTGAATCTTTACCTACACATTACTCAGGCATTGCATTTAAAATATATGAGGGTTCTAAAAATTTTTATCCTTGCGTTGAAATAAAGGCTTCTCCCGCAAAAGTATTACAGGGTCATAATGTTTTTGGTACAACCGATTTAGCTTTATGCTCTGAGGCTTTATTGCTTAATTTTGCTAATTCTTTGCCTTGCCTGTATGATTTATTGGATGTT'
    
    if end == -1:
        start = index
        end = index - 1
        seq = m13[start:len(m13)] + m13[0:end]
    else:
        start += index
        end += index
        if end > len(m13):
            end = end - len(m13)
            seq = m13[start: len(m13)] + m13[0:end]
        else:
            seq = m13[start:end]
    return seq

def p3024_sequence(start, end):
    """Given a range, returns the p3024 sequence in that range"""
    index = 0
    p3024 = 'AATAGTGGACTCTTGTTCCAAACTGGAACAACACTCAACCCTATCTCGGGCTATTCTTTTGATTTATAAGGGATTTTGCCGATTTCGGGGTACCTACGAAGAGTTCCAGCAGGGATTCCAAGAAATGGCCAATGAAGATTGGATCACCTTTCGCACTAAGACCTACTTGTTTGAGGAGTTTCTGATGAATTGGCACGACCGCCTCAGGAAAGTGGAGGAGCATTCTGTGATGACTGTCAAGCTCCAATCTGAGGTGGACAAATATAAGATTGTTATCCCTATCCTGAAGTACGTCCGCGGAGAACACCTGTCACCCGATCACTGGCTGGATCTGTTCCGCTTGCTGGGTCTGCCTCGCGGCACATCTCTGGAGAAACTGCTGTTCGGTGACCTGCTGAGAGTTGCCGATACCATCGTGGCCAAGGCTGCTGACCTGAAAGATCTGAACTCACGCGCCCAGGGTGAAGTGACCATCCGCGAAGCACTCAGGGAACTGGATTTGTGGGGCGTGGGTGCTGTGTTCACACTGATCGACTATGAGGACTCCCAGAGCCGCACCATGAAGCTGATCAAGGATTGGAAGGACATCGTCAACCAGGTGGGCGACAATAGATGCCTCCTGCAGTCCTTGAAGGACTCACCATACTATAAAGGCTTTGAAGACAAGGTCAGCATCTGGGAAAGGAAACTCGCCGAACTGGACGAATATTTGCAGAACCTCAACCATATTCAGAGAAAGTGGGTTTACCTCGAACCAATCTTTGGTCGCGGAGCCCTGCCCAAAGAGCAGACCAGATTCAACAGGGTGGATGAAGATTTCCGCAGCATCATGACAGATATCAAGAAGGACAATCGCGTCACAACCTTGACTACCCACGCAGGCATTCGCAACTCACTGCTGACCATCCTGGACCAATTGCAGAGATGCCAGCGCAGCCTCAACGAGTTCCTGGAGGAGAAGCGCAGCGCCTTCCCTCGCTTCTACTTCATCGGAGACGATGACCTGCTGGAGATCTTGGGCCAGTCAACCAATCCATCCGTGATTCAGTCTCACCTCAAGAAGCTGTTTGCTGGTATCAACTCTGTCTGTTTCGATGAGAAGTCTAAGCACATTACTGCAATGAAGTCCTTGGAGGGAGAAGTTGTGCCATTCAAGAATAAGGTGCCCTTGTCCAATAACGTCGAAACCTGGCTGAACGATCTGGCCCTGGAGATGAAGAAGACCCTGGAGCAGCTGCTGAAGGAGTGCGTGACAACCGGACGCAGCTCTCAGGGAGCTGTGGACCCTTCTCTGTTCCCATCACAGATCCTGTGCTTGGCCGAACAGATCAAGTTTACCGAAGATGTGGAGAACGCAATTAAAGATCACTCCCTGCACCAGATTGAGACACAGCTGGTGAACAAATTGGAGCAGTATACTAACATCGACACATCTTCCGAGGACCCAGGTAACACAGAGTCCGGTATTCTGGAGCTGAAACTGAAAGCACTGATTCTCGACATTATCCATAACATCGACGTGGTCAAGCAGCTGAACCAAATCCAAGTGCACACCACCGAAGATTGGGCCTGGAAGAAGCAGTTGAGGTTCTACATGAAGTCCGACCACACCTGTTGCGTTCAGATGGTTGACAGCGAGTTCCAGTACACCTATGAGTACCAAGGAAATGCCAGCAAGCTCGTTTACACTCCACTCACTGACAAGTGTTACCTCACCTTGACACAGGCTATGAAGATGGGCCTGGGAGGCAACCCATACGGTCCAGCTGGCACTGGTAAGACAGAGAGCGTTAAGGCACTCGGAGGTCTGCTGGGCAGGCAGGTCCTCGTGTTCAACTGTGATGAAGGAATCGACGTTAAGTCCATGGGAAGAATCTTTGTTGGCCTCGTTAAGTGTGGAGCTTGGGGTTGCTTCGACGAGTTCAACAGGCTGGAGGAATCTGTGCTGAGCGCCGTCTCTATGCAGATCCAGACCATCCAGGACGCATTGAAGAACCACAGGACCGTCTGCGAGCTGTTGGGTAAGGAAGTGGAGGTGAACTCCAACTCCGGAATCTTCATCACAATGAATCCCGCAGGTAAAGGATATGGAGGAAGACAGAAACTCCCAGACAACCTGAAGCAGCTGTTCCGCCCAGTGGCTATGTCCCATCCAGACAATGAGCTGATCGCCGAAGTCATCCTCTATTCCGAGGGATTCAAAGATGCTAAAGTTCTCTCCAGAAAGCTCGTGGCCATCTTCAATCTGTCAAGAGAACTCCTGACACCTCAGCAGCATTACGACTGGGGTCTGAGAGCCCTCAAGACCGTCCTGAGAGGTTCAGGAAATCTCCTCAGGCAGCTGAACAAGAGCGGTACAACACAGAATGCAAATGAGAGCCACATTGTCGTCCAGGCTCTGAGGCTGAATACCATGTCAAAGTTCACATTCACAGACTGCACAAGATTTGACGCTCTGATTAAAGATGTGTTCCCTGGTATTGAACTCAAAGAAGTGGAGTATGACGAGCTGAGCGCCGCTTTGAAGCAGGTGTTTGAGGAGGCTAACTATGAGATTATCCCTAATCAGATCAAGAAAGCATTGGAACTGTATGAACAGCTGTGTCAGAGGATGGGAGTGGTGATTGTGGGCCCATCAGGCGCAGGTAAGAGCACTCTCTGGAGAATGCTGAGAGCAGCACTGTGCAAGACTGGAAAGGTGGTGAAGCAATACACCATGAATCCCGGATCCACGCGCCCTGTAGCGGCGCATTAAGCGCGGCGGGTGTGGTGGTTACGCGCAGCGTGACCGCTACACTTGCCAGCGCCCTAGCGCCCGCTCCTTTCGCTTTCTTCCCTTCCTTTCTCGCCACGTTCGCCGGCTTTCCCCGTCAAGCTCTAAATCGGGGGCTCCCTTTAGGGTTCCGATTTAGTGCTTTACGGCACCTCGACCCCAAAAAACTTGATTTGGGTGATGGTTCACGTAGTGGGCCATCGCCCTGATAGACGGTTTTTCGCCCTTTGACGTTGGAGTCCACGTTCTTT'
    seq = p3024[start:end]

    if end == -1:
        start = index
        end = index - 1
        seq = p3024[start:len(p3024)] + p3024[0:end]
    else:
        start += index
        end += index
        if end > len(p3024):
            end = end - len(p3024)
            seq = p3024[start: len(p3024)] + p3024[0:end]
        else:
            seq = p3024[start:end]

    return seq

def p768_sequence(start, end):
    """Given a range, returns the p768 sequence in that range"""
    index = 0
    p768 = 'GCTGGTGAACAAATTGGAGCAGTATACTAACATCGACACATCTTCCGAGGACCCAGGTAACACAGAGTCCGGTATTCTGGAGCTGAAACTGAAAGCACTGATTCTCGACATTTCCGACCACACCTGTTGCGTTCAGATGGTTGACAGCGAGTTCCAGTACACCTATGAGTACCAAGGAAATGCCAGCAAGCTCGTTTACACTCCACTCACTGACAAGTGTTACCTCACCTTGACACAGGCCCTCGTGTTCAACTGTGATGAAGGAATCGACGTTAAGTCCATGGGAAGAATCTTTGTTGGCCTCGTTAAGTGTGGAGCTTGGGGTTGCTTCGACGAGTTCAACAGGCTGGAGGAATCTGTGCTGAGCGCCGGAATCTTCATCACAATGAATCCCGCAGGTAAAGGATATGGAGGAAGACAGAAACTCCCAGACAACCTGAAGCAGCTGTTCCGCCCAGTGGCTATGTCCCATCCAGACAATGAGCTGATCGCCGAACAGCATTACGACTGGGGTCTGAGAGCCCTCAAGACCGTCCTGAGAGGTTCAGGAAATCTCCTCAGGCAGCTGAACAAGAGCGGTACAACACAGAATGCAAATGAGAGCCACATTGTCGTCCAGGCTCTGGAGTATGACGAGCTGAGCGCCGCTTTGAAGCAGGTGTTTGAGGAGGCTAACTATGAGATTATCCCTAATCAGATCAAGAAAGCATTGGAACTGTATGAACAGCTGTGTCAGAGGATGGGAGTGGTGAATCCCGGATCCACGCG'
    seq = p768[start:end]

    if end == -1:
        start = index
        end = index - 1
        seq = p768[start:len(p768)] + p768[0:end]
    else:
        start += index
        end += index
        if end > len(p768):
            end = end - len(p768)
            seq = p768[start: len(p768)] + p768[0:end]
        else:
            seq = p768[start:end]

    return seq