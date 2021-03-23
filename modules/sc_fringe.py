import sc_general
import sc_seq
import scadnano as sc

def find_fringe_seq_ranges(fringe_offset, scaffold_start, hex_or_square, left_right):
    """Given the locations of the fringe ends, the scaffold starting point on the last helix, and the max_offset, returns the seq offset for the sticky ends"""
    if hex_or_square == 'hex':
        multiple = 7
    elif hex_or_square == 'square':
        multiple = 8
    else:
        raise Exception("Error in check_valid_outline(), input for hex_or_square must be eihter 'hex' or 'square'")
    sequence_ranges = []
    if left_right == 'left':
        offset0 = scaffold_start * 11 + fringe_offset
        sequence_ranges.append((offset0, offset0 + 2 * multiple))
        offset1 = offset0 - 2 * multiple
        sequence_ranges.append((offset1, offset1 + 2 * multiple))
        i = 1
        while i < 6:
            offset_even = offset0 - 2 * scaffold_start * i
            sequence_ranges.append((offset_even, offset_even + 2 * multiple))
            offset_odd = offset_even - 2 * multiple
            sequence_ranges.append((offset_odd, offset_odd + 2 * multiple))
            i += 1
    elif left_right == 'right':
        fringe_offset -= scaffold_start
        print(fringe_offset)
        offset0 = 12 * scaffold_start + fringe_offset
        sequence_ranges.append((offset0, offset0 + 2 * multiple))
        offset1 = offset0 + 2 * scaffold_start - 2 * multiple
        sequence_ranges.append((offset1, offset1 + 2 * multiple))
        i = 1
        while i < 6:
            offset_even = offset0 + i * 2 * scaffold_start
            sequence_ranges.append((offset_even, offset_even + 2 * multiple))
            offset_odd = offset_even + 2 * scaffold_start - 2 * multiple
            sequence_ranges.append((offset_odd, offset_odd + 2 * multiple))
            i += 1
    print(sequence_ranges)
    return sequence_ranges 

def get_fridge_seqs(fringe_ranges, seq_name, left_right):
    """Given the fringe range offset, and the name of the sequence of the scaffold, returns the sequence of the fringes"""
    seqs = []
    if left_right == 'left':
        for helix in range(1, 12, 2):
            if helix == 11:
                helix2 = 0
            else:
                helix2 = helix + 1
            
            range1, range2 = fringe_ranges[helix], fringe_ranges[helix2]
            sca_seq1, sca_seq2 = sc_seq.sequence(seq_name, range1[0], range1[1]), sc_seq.sequence(seq_name, range2[0], range2[1])
            seq1, seq2 = sc_general.find_seq_pairs(sca_seq2[::-1]), sc_general.find_seq_pairs(sca_seq1[::-1])
            seq = seq2 + seq1
            seqs.append(seq)
    elif left_right == 'right':
        for helix in range(0, 12, 2):
            helix2 = helix + 1

            range1, range2 = fringe_ranges[helix], fringe_ranges[helix2]
            sca_seq1, sca_seq2 = sc_seq.sequence(seq_name, range1[0], range1[1]), sc_seq.sequence(seq_name, range2[0], range2[1])
            print(sca_seq1, sca_seq2)
            seq1, seq2 = sc_general.find_seq_pairs(sca_seq1[::-1]), sc_general.find_seq_pairs(sca_seq2[::-1])
            #print(seq1, seq2)
            seq = seq2 + seq1
            seqs.append(seq)
    print(seqs)
    return seqs

def add_fringe(design, fringe_seqs, left_right):
    """Given the design, and fringe sequence, adds the fringe to the design"""
    fringe_num = len(fringe_seqs)
    if left_right == 'left':
        helix_st = 1
    else:
        helix_st = 0

    for i in range(fringe_num):
        print(helix_st)
        if helix_st == 11:
            helix2 = 0 
        else:
            helix2 = helix_st + 1

        forward = sc_general.forward_strand(helix_st, 'staple')
        forward2 = sc_general.forward_strand(helix2, 'staple')

        if forward:
            helix = helix_st
        else:
            helix, helix2 = helix2, helix_st
            forward, forward2 = forward2, forward

        staple = sc.Strand([sc.Domain(helix = helix, forward = forward, start = 0, end = 16), sc.Domain(helix = helix2, forward = forward2, start = 0, end = 16)], dna_sequence= fringe_seqs[i])
        design.add_strand(staple)

        helix_st += 2
