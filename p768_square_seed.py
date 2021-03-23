import sys
sys.path.append('c:/Users/Sarah/Documents/UCSB/Fygenson Lab/scadnano_projects/modules')
import sc_general
import sc_pattern
import sc_create
import sc_seeds
import sc_seq

def generate_shape_outline():
    """Generate a shape outline
    [(row_type, [(start, end), (start, end), ...]), ...]"""

    outline = []
    for _ in range(12):
        row_type = 0
        start = 0
        end = 64
        outline.append((row_type, [(start, end)]))

    return outline

def generate_staple_domain():
    """Generates the bounds for which the design has staple strands (in the same format as the shape_ouline"""
    domain = []
    for _ in range(12):
        row_type = 0
        start = 16
        end = 48
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

def generate_hairpin_lattice():
    """Generates the lattice, allong with its positions
    [(x_pos, y_pos), (x_pos, y_pos), ...]"""
    x_pos = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    y_pos = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    
    lattice = []
    for i in range(len(x_pos)):
        lattice.append((x_pos[i], y_pos[i]))

    return lattice

def seam_locations(outline):
    """Give a shape outline, returns the seam locations for each helix, in the form of a stacked list
    [[seam1, seam2, ...],[seam for helix 2], ...]"""
    
    seams = []
    for i in range(len(outline)):
        seams.append('no seam')

    return seams

def hairpin_locations(outline):
    """Generates a list of hairpin locations"""

    hairpins_shape = []
    for helix in range(len(outline)):
        hairpins_line = []
        if helix % 2 == 0:
            offsets = [3]
        else:
            offsets = [5]
        for i in offsets:
            hairpins_line.append(8 * i)
        hairpins_shape.append(hairpins_line)
    
    return hairpins_shape

if __name__ == '__main__':
    #main seed outline
    grid_type = 'square'
    main_seed = generate_shape_outline()
    sc_general.check_valid_outline(main_seed, grid_type)

    #both the main lattice and the hairpin lattice
    main_lattice = generate_main_lattice()
    hairpin_lattice = generate_hairpin_lattice()
    complete_lattice = main_lattice + hairpin_lattice

    #seam and hairpin locations
    seams = seam_locations(main_seed)
    hairpins = hairpin_locations(main_seed)
    staple_ouline = generate_staple_domain()

    #staple nick locations
    staple_nicks = sc_pattern.linear_staple_nick_s_shape(staple_ouline, seams, grid_type)

    #crossover locations
    scaffold_crossovers = sc_pattern.linear_scaffold_crossovers(main_seed, seams)
    staple_crossovers = sc_pattern.linear_staple_crossovers_s_shape_loop_around(staple_ouline, seams, grid_type)

    #scaffold
    design = sc_create.create_helices(main_seed, complete_lattice, grid_type)
    sc_create.add_precursor_scaffolds(design, main_seed)
    sc_create.add_scaffold_nicks(design, seams)
    sc_create.add_crossovers(design, scaffold_crossovers, 'scaffold')
    design.strands[0].set_scaffold()

    #staples
    sc_create.add_precursor_staples(design, staple_ouline)
    sc_create.add_staple_nicks(design, staple_nicks)
    sc_create.add_crossovers(design, staple_crossovers, 'staple')

    #assign scaffold sequence
    sca_seq = sc_seq.sequence('p768', 0, 768)
    design.assign_dna(design.strands[0], sequence = sca_seq)

    #hairpins
    sc_seeds.add_hairpins(design, hairpins, hairpin_lattice)
    design.write_scadnano_file()