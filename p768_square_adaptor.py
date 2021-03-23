import sys
sys.path.append('c:/Users/Sarah/Documents/UCSB/Fygenson Lab/scadnano_projects/modules')
import sc_general
import sc_pattern
import sc_create
import sc_seeds
import sc_adaptor
import sc_seq

def generate_shape_outline():
    domain = []
    for _ in range(12):
        row_type = 0
        start = 0
        end = 45
        domain.append((row_type, [(start, end)]))

    return domain

def generate_staple_outline():
    domain = []
    for _ in range(12):
        row_type = 0
        start = 16
        end = 50
        domain.append((row_type, [(start, end)]))

    return domain

def generate_lattice_outline():
    domain = []
    for _ in range(12):
        row_type = 0
        start = 0
        end = 50
        domain.append((row_type, [(start, end)]))

    return domain

def generate_main_lattice():
    """Generates the lattice, allong with its positions
    [(x_pos, y_pos), (x_pos, y_pos), ...]"""
    x_pos = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    y_pos = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    
    lattice = []
    for i in range(len(x_pos)):
        lattice.append((x_pos[i], y_pos[i]))

    return lattice

if __name__ == '__main__':
    grid_type = 'square'
    lattice = generate_main_lattice()
    scaffold_domain = generate_shape_outline()
    staple_domain = generate_staple_outline()
    lattice_domain = generate_lattice_outline()

    scaffold_start = 112

    sticky_ranges = sc_adaptor.find_sticky_seq_ranges(208, 112, grid_type)
    sticky_seq = []

    for i in sticky_ranges:
        start, end = i[0], i[1]
        seed_end = sc_seq.p3024_sequence(start, end)
        sticky_seq.append(seed_end)
    
    staple_seq = []
    center_seq = sc_adaptor.center_adapt_seq()
    for helix in range(len(center_seq)):
        seq = center_seq[helix]
        if helix % 2 == 1:
            seq = seq + sc_adaptor.tile_adapt_seq(helix)
        else:
            seq = sc_adaptor.tile_adapt_seq(helix) + seq
        staple_seq.append(seq)

    #scaffold
    design = sc_create.create_helices(lattice_domain, lattice, grid_type)
    not_fixed_scaf_seq = sc_adaptor.outside_adaptor_seq(sticky_seq)
    scaf_seq = []
    for helix in range(len(not_fixed_scaf_seq)):
        seq = not_fixed_scaf_seq[helix]
        if helix % 2 == 1:
            seq = seq[5:]
        scaf_seq.append(seq)
    sc_create.add_precursor_scaffolds(design, scaffold_domain, dna_seq = scaf_seq)

    #staples
    sc_create.add_precursor_staples(design, staple_domain, dna_seq = staple_seq)
    for helix in range(1,12,2):
        forward = sc_general.forward_strand(helix, 'staple')
        design.add_nick(helix = helix, offset = 24, forward = forward)
    for helix in range(12):
        forward = sc_general.forward_strand(helix, 'staple')
        design.add_nick(helix = helix, offset = 37, forward = forward)

    sc_adaptor.add_adaptor_crossovers(design)



    design.write_scadnano_file()

    