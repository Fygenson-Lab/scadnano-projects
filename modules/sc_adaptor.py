import sc_general
import scadnano as sc
import math
import sc_seq

def find_sticky_seq_ranges(sticky_offset, scaffold_start, hex_or_square):
    """Given the locations of the sticky ends, the scaffold starting point on the last helix, and the max_offset, retursn the seq offset for the sticky ends"""
    if hex_or_square == 'hex':
        multiple = 7
    elif hex_or_square == 'square':
        multiple = 8
    else:
        raise Exception("Error in check_valid_outline(), input for hex_or_square must be eihter 'hex' or 'square'")
    sequence_ranges = []
    offset0 = scaffold_start * 11 + sticky_offset
    sequence_ranges.append((offset0, offset0 + 4 * multiple))
    i = 1
    while i < 6:
        offset = scaffold_start * 12 + scaffold_start * 2 * i + (sticky_offset - scaffold_start)
        sequence_ranges.append((offset, offset + 4 * multiple))
        i += 1 

    return sequence_ranges      

def tile_adapt_seq(helix):
    tile_end_seq = [
        'GTCTGGCACGGAT',
        'CTTGGCTGGCATT',
        'CTGGTTGCTCGTG',
        'ACTCCGTGAGGTA',
        'GTCTGTGCCGAGC',
        'TGGCTCTGGCATT',
        'CTGGTTCGTCCGC',
        'ACGCTTCCAGGTA',
        'GTCTGTCCTGCGA',
        'GACGGTTGGCATT',
        'CTGGTTCAGGCTT',
        'CGACGCTGAGGTA',
    ]
    
    seq = tile_end_seq[helix]
    return seq

def center_adapt_seq():
    seq = ['GACCGCACTCACCACTGCTCG',
    'GCTCTGTCTCGCTACCTGCGT',
    'TCGTCGGATGGTGAGGTCCAC',
    'TGGCTACCGTCCTACGCTTCG',
    'GACCTTGGTGATGCTGGACTG',
    'CTCCAACGCAAGACCATGCCG',
    'ACCTCATCCTCGCTTTCGGTG',
    'GGAGATCGGTCACTGCCGTAG',
    'CTCACGAGGCACAACCACAGC',
    'GAAGTGCGAGTCCTGTGGAAC',
    'ACCACGAGACGCCATCGAGCG',
    'CCTGTCTGACTCGTAGCCTTG']
    
    return seq

def add_adaptor_crossovers(design):
    """Given a adaptor design, adds the crossovers"""
    crossovers = []
    croosover_locations = [16, 36, 37]
    for helix in range(1, 12, 2):
        if helix == 11:
            helix2 = 0
        else:
            helix2 = helix + 1
        forward = sc_general.forward_strand(helix, 'staple')
        forward2 = sc_general.forward_strand(helix2, 'staple')
        for offset in croosover_locations:
            crossovers.append(sc.Crossover(helix = helix, helix2 = helix2, offset = offset, offset2 = offset, forward = forward, forward2 = forward2, half = True))

    design.add_crossovers(crossovers)

def outside_adaptor_seq(sticky_seq):
    """Given the sequence of the sticky ends, returns the outside sequence of the adaptor"""
    outside_seqs = []
    staple_centers = center_adapt_seq()
    for helix in range(12):
        helix_to_strand = [5, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5]
        strand = helix_to_strand[helix]

        complete_seq = sticky_seq[strand]
        tile_seq = tile_adapt_seq(helix)

        if helix % 2 == 0:
            reversed_seed_end = complete_seq[16:32]
        elif helix %2 == 1:
            reversed_seed_end = complete_seq[0:16]

        seed_end = reversed_seed_end[::-1]
        tile_end = tile_seq[::-1]

        seed_to_adaptor = sc_general.find_seq_pairs(seed_end)
        staple_center = staple_centers[helix]
        
        scaffold_center = sc_general.find_seq_pairs(staple_center[::-1])
        #if helix % 2 == 1:
            #scaffold_center = scaffold_center[5:len(scaffold_center)]
        adaptor_to_tile = sc_general.find_seq_pairs(tile_end)

        if helix % 2 == 0:
            outside_seq = '{}{}{}'.format(seed_to_adaptor, scaffold_center, adaptor_to_tile)
        else:
            outside_seq = '{}{}{}'.format(adaptor_to_tile, scaffold_center, seed_to_adaptor)
        outside_seqs.append(outside_seq)
    
    return outside_seqs

    
    