import scadnano as sc
import sys
sys.path.append('.../')
from modules import sc_general

def create_helices(shape_outline, lattice, hex_or_square) -> sc.Design:
    """Given the outline, complete lattice, and if the lattice is hex or square, creates the base helices without any strands"""
    if hex_or_square == 'hex':
        grid_type = sc.hexagonal
    elif hex_or_square == 'square':
        grid_type = sc.square
    else:
        raise Exception("Error in create_helices(), input for hex_or_square must be eihter 'hex' or 'square'")

    max_offset = sc_general.find_max(shape_outline)
    size = len(lattice)
    helices = []
    for i in range(size):
        position = lattice[i]
        helices.append(sc.Helix(max_offset = max_offset, grid_position = position))
    design = sc.Design(helices = helices, strands = [], grid = grid_type)

    return design

def add_precursor_scaffolds(design: sc.Design, shape_outline, label = None, dna_seq = None):
    """Adds the precursor scaffold to the design"""
    for helix in range(len(shape_outline)):
        if dna_seq == None:
            seq = None
        else:
            seq = dna_seq[helix]
        forward = sc_general.forward_strand(helix, 'scaffold')
        one_line_outline = shape_outline[helix]
        for i in range(one_line_outline[0] + 1):
            lines = one_line_outline[1]
            line = lines[i]
            start = line[0]
            end = line[1]
            scaffold = sc.Strand([sc.Domain(helix = helix, forward = forward, start = start, end = end, label = label)], dna_sequence = seq, name = 'scaffold')
            design.add_strand(scaffold)

def add_scaffold_nicks(design: sc.Design, seam_locations):
    """Adds nicks to the precursor scaffold"""
    for helix in range(len(seam_locations)):
        if seam_locations[helix] == 'no seam':
            continue
        else:
            nick_offsets = seam_locations[helix]
            for nick_offset in nick_offsets:
                if nick_offset != 'no seam':
                    forward = sc_general.forward_strand(helix, 'scaffold')
                    design.add_nick(helix = helix, offset = nick_offset, forward = forward)

def add_crossovers(design: sc.Design, crossover_list, scaffold_or_staple):
    """Adds crossovers"""
    crossovers = []

    for helix in range(len(crossover_list)):
        if crossover_list[helix] == 'no crossover':
            continue
        else:
            for crossover in crossover_list[helix]:
                helix2 = crossover[1]
                offset = crossover[2]
                offset2 = crossover[3]
                forward = sc_general.forward_strand(helix, scaffold_or_staple)
                forward2 = sc_general.forward_strand(helix2, scaffold_or_staple)
                crossovers.append(sc.Crossover(helix = helix, helix2 = helix2, offset = offset, offset2 = offset2, forward = forward, forward2 = forward2, half = True))
    
    design.add_crossovers(crossovers)

def add_precursor_staples(design: sc.Design, staple_domain, label = None, dna_seq = None):
    """Add precursor staples to the design"""
    for helix in range(len(staple_domain)):
        if dna_seq == None:
            seq = None
        else:
            seq = dna_seq[helix]
        forward = sc_general.forward_strand(helix, 'staple')
        outline = staple_domain[helix]
        for i in range(outline[0] + 1):
            lines = outline[1]
            line = lines[i]
            start = line[0]
            end = line[1]
            staples = sc.Strand([sc.Domain(helix = helix, forward = forward, start = start, end = end, label = label)], dna_sequence = seq)
            design.add_strand(staples)

def add_staple_nicks(design: sc.Design, nick_locations):
    """Adds nicks ot the precursor staple strands"""
    for helix in range(len(nick_locations)):
        forward = sc_general.forward_strand(helix, 'staple')
        for nick in nick_locations[helix]:
            design.add_nick(helix = helix, offset = nick, forward = forward)