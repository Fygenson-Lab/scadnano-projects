import random
import scadnano as sc
import sc_general

def random_hairpin_sequence():
    """Returns a random 22 bp hairpin sequence, with TT at the 3' end, and TTTT loop at the center"""
    bases = ['A', 'T', 'C', 'G']
    seq = ''
    oposite_side = []
    for _ in range(8):
        new_base = random.choice(bases)
        seq += new_base
        if new_base == 'A':
            oposite_side += 'T'
        elif new_base == 'T':
            oposite_side += 'A'
        elif new_base == 'C':
            oposite_side += 'G'
        else:
            oposite_side += 'C'
    seq += 'TTTT'   
    oposite_side.reverse()
    for base in oposite_side:
        seq += base
    seq += 'TT'

    return seq 

def non_random_hairpin_sequence(index):
    """Returns a non-random hairpin, with TT at the 3' end, and TTT loop in the center"""
    non_random_pins = [
        'GTGAGGCGTTTTCGCCTCACTT',
        'GGCTCCGCTTTTGCGGAGCCTT',
        'CTGGCTCGTTTTCGAGCCAGTT',
        'CGCTTGCGTTTTCGCAAGCGTT',
        'TGCGGTCGTTTTCGACCGCATT',
        'CTGCGTCGTTTTCGACGCAGTT',
        'CCGAGGCGTTTTCGCCTCGGTT',
        'GCCAGGACTTTTGTCCTGGCTT',
        'TCGGAGCGTTTTCGCTCCGATT',
        'GGTGGTCGTTTTCGACCACCTT',
        'GCCATCGCTTTTGCGATGGCTT',
        'CGTGGAGCTTTTGCTCCACGTT',
        'GTCCACCGTTTTCGGTGGACTT',
        'GTGGTCCGTTTTCGGACCACTT',
        'CTCGGCACTTTTGTGCCGAGTT',
        'CGGATCGCTTTTGCGATCCGTT',
        'CACCGCTGTTTTCAGCGGTGTT',
        'CGGAACCGTTTTCGGTTCCGTT',
        'CCGTGGCGTTTTCGCCACGGTT',
        'GTGCTGCGTTTTCGCAGCACTT',
        'ACGCTGGCTTTTGCCAGCGTTT',
        'CGACGGACTTTTGTCCGTCGTT',
        'GGCATCCGTTTTCGGATGCCTT',
        'GCTGACGCTTTTGCGTCAGCTT',
        'ACCAGCCGTTTTCGGCTGGTTT',
        'CGGAGGCGTTTTCGCCTCCGTT',
        'CTCGCTGCTTTTGCAGCGAGTT',
        'GCCAGTGCTTTTGCACTGGCTT',
        'CCGTCCGCTTTTGCGGACGGTT',
        'CGGATGGCTTTTGCCATCCGTT',
        'TCTGGTCGTTTTCGACCAGATT',
        'GGCACCTGTTTTCAGGTGCCTT',
        'CCTGCCTGTTTTCAGGCAGGTT',
        'CGGTGCCGTTTTCGGCACCGTT',
        'CTCGGTCGTTTTCGACCGAGTT',
        'CCGAGGACTTTTGTCCTCGGTT',
        'CGGCAGGCTTTTGCCTGCCGTT',
        'CGCTTGGCTTTTGCCAAGCGTT',
        'TGGCGAGCTTTTGCTCGCCATT',
        'CCACCTCGTTTTCGAGGTGGTT',
        'CTCTGGACTTTTGTCCAGAGTT',
        'CGAGGCACTTTTGTGCCTCGTT',
        'CTCCTGCGTTTTCGCAGGAGTT',
        'GTCAGGCGTTTTCGCCTGACTT',
        'CGTCCTGCTTTTGCAGGACGTT',
        'CGGACCTGTTTTCAGGTCCGTT',
        'CGAGGTCGTTTTCGACCTCGTT',
        'CAGGAGCGTTTTCGCTCCTGTT',
        'GCAGTCGCTTTTGCGACTGCTT',
        'GTCTGGCGTTTTCGCCAGACTT',
        'TGGCTGCGTTTTCGCAGCCATT',
        'AGTGCCTGTTTTCAGGCACTTT',
        'GTCGGTGCTTTTGCACCGACTT',
        'CGGTCGGCTTTTGCCGACCGTT',
        'GACCTGGCTTTTGCCAGGTCTT',
        'TCGGCTCGTTTTCGAGCCGATT',
        'CACAGGCGTTTTCGCCTGTGTT',
        'GTGGCAGCTTTTGCTGCCACTT',
        'ACCAGGCGTTTTCGCCTGGTTT',
        'GCTCGCTGTTTTCAGCGAGCTT',
        'CCTACCGCTTTTGCGGTAGGTT',
        'CTGGACGCTTTTGCGTCCAGTT',
        'GCTCGGACTTTTGTCCGAGCTT',
        'GCCGAGCGTTTTCGCTCGGCTT',
        'TCGGAGGCTTTTGCCTCCGATT',
        'CTGGTGGCTTTTGCCACCAGTT',
        'CCGCAGGCTTTTGCCTGCGGTT',
        'CACGACGCTTTTGCGTCGTGTT',
        'GTCGCTGCTTTTGCAGCGACTT',
        'CGGAGCACTTTTGTGCTCCGTT',
        'GCCTAGCGTTTTCGCTAGGCTT',
        'CGCTCGTGTTTTCACGAGCGTT'
    ]

    return non_random_pins[index]

def add_hairpins(design, hairpin_locations, hairpin_lattice):
    """Given the design, the hairpin lattice, and the hairpin locations, adds the hairpins to the hairpin lattice and crossovers to the seed"""
    seed_domain = range(len(hairpin_locations))
    hairpin_domain = range(len(hairpin_locations), len(hairpin_locations) + len(hairpin_lattice))
    #creates the hairpins, included the loopout crossover
    for i in range(len(hairpin_domain)):
        helix = hairpin_domain[i]
        for j in range(len(hairpin_locations[helix - len(seed_domain)])):
            left_offset = hairpin_locations[helix - len(seed_domain)][j]
            right_offset = left_offset + 8
            index = 6 * (i - 1) + j
            pin_seq = non_random_hairpin_sequence(index)
            staple = sc.Strand([sc.Domain(helix = helix, forward = True, start = left_offset, end = right_offset), sc.Loopout(length = 4), sc.Domain(helix = helix, forward = False, start = left_offset - 2, end = right_offset)], dna_sequence= pin_seq)
            design.add_strand(staple)

    #add nicks on staple strands to be able to connect the hairpins
    for helix in seed_domain:
        forward = sc_general.forward_strand(helix, 'staple')
        for nick in hairpin_locations[helix]:
            design.add_nick(helix = helix, offset = nick, forward = forward)

    #crossovers between the main helices and the hairpins
    crossovers = []
    for helix in seed_domain:
        helix2 = hairpin_domain[helix]
        forward = sc_general.forward_strand(helix, 'staple')
        for pin in hairpin_locations[helix]:
            if forward == True:
                forward_pin_offset = pin - 1
                reverse_pin_offset = pin
            else:
                forward_pin_offset = pin
                reverse_pin_offset = pin - 1
            crossovers.append(sc.Crossover(helix = helix, helix2 = helix2, offset = forward_pin_offset, offset2 = pin, forward = forward, forward2 = True, half = True))
            crossovers.append(sc.Crossover(helix = helix, helix2 = helix2, offset = reverse_pin_offset, offset2 = pin - 2, forward = forward, forward2 = False, half = True))

    design.add_crossovers(crossovers)

