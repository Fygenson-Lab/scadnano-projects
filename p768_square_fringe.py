import sys
sys.path.append('c:/Users/Sarah/Documents/UCSB/Fygenson Lab/scadnano_projects/modules')
import sc_general
import sc_pattern
import sc_create
import sc_seeds
import sc_adaptor
import sc_seq
import sc_fringe

def generate_staple_outline():
    domain = []
    for _ in range(12):
        row_type = 0
        start = 0
        end = 16
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
    staple_domain = generate_staple_outline()
    lattice_domain = staple_domain

    scaffold_start = 112

    fringe_ranges = sc_fringe.find_fringe_seq_ranges(160, 112, grid_type, 'right')

    fringe_seq = sc_fringe.get_fridge_seqs(fringe_ranges, 'p3024', 'right')

    design = sc_create.create_helices(lattice_domain, lattice, grid_type)

    sc_fringe.add_fringe(design, fringe_seq, 'right')

    design.write_scadnano_file()

    