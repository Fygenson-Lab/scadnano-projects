import sys, os, pandas
sys.path.append('.../')
from modules import sc_general
from modules import sc_pattern
from modules import sc_create
from modules import sequences

#This script assumes a 12 helix seed, with no empty regions, and a linear S shaped scaffold, on a square lattice (8 bp multiples)

design_name = input('Design name: ')

sequence_name = input('Scaffold sequence name (make sure sequence is in seq.json): ')

seed_legnth = int(sc_general.smart_input('Desired Seed Length (in bp, must be divisible by 16): ', 
    try_tests = [lambda string : int(string)],
    test_fail_mes = ['Please input seed legnth as an integer.'],
    conditions = [lambda seed_legnth : seed_legnth % 16 == 0],
    condition_fail_mes = ['Seed length must be a multiple of 16.']))

sidedness = sc_general.smart_input('Is this a one-sided or two-sided seed? (1 or 2): ',
    conditions = [lambda sidedness : sidedness == 1 or sidedness == 2],
    condition_fail_mes = ['Please input sidedness as "1" or "2"'])

print('Generating seed design file...')

lattice = [] #helice lattice to place strands on
for i in range(12): lattice.append((0, i))

outline = [] #outline object for the scaffold
for _ in range(12): outline.append((0, [(0, seed_legnth)])) 
sc_general.check_valid_outline(outline, 'square')

staple_outline = [] #outline object for the staples
for _ in range(12): staple_outline.append((0, [(16 * (sidedness - 1), seed_legnth - 16)]))

seems = [] #seam locations, none for the s-shaped seed
for _ in range(12): seems.append('no seam')

#find the staple nick and crossover locations, and scaffold sequence
staple_nicks = sc_pattern.seed_nick_locations(staple_outline, outline, seems, 'square')
scaffold_crossovers = sc_pattern.linear_scaffold_crossovers(outline, seems)
staple_crossovers = sc_pattern.seed_crossever_locations(staple_outline, outline, seems, 'square')
sca_seq = sc_general.sequence(sequence_name, 0, seed_legnth * 12)

design = sc_create.create_helices(outline, lattice, 'square') #create scadnano design object with helices
sc_create.add_precursor_scaffolds(design, outline) #add scaffold
sc_create.add_scaffold_nicks(design, seems) #add scaffold nicks
sc_create.add_crossovers(design, scaffold_crossovers, 'scaffold') #add scaffold crossovers
design.strands[0].set_scaffold() #set this strand as the scaffolds
sc_create.add_precursor_staples(design, staple_outline) #add staple strands
sc_create.add_staple_nicks(design, staple_nicks) #add staple nicks
sc_create.add_crossovers(design, staple_crossovers, 'staple') #add staple crossovers
design.assign_dna(design.strands[0], sequence = sca_seq) #assign scaffold sequence
sc_general.name_staples(design) #rename the staple strands

design.write_scadnano_file() #create scadnano file
os.rename('seed_design_maker.sc', '{}.sc'.format(design_name)) #rename file to the design name

print('Scadnano design file generated.')

gen_short_hp_seq = sc_general.smart_input('Do you want to export staple sequences with short hairpins? (y/n): ',
    conditions = [lambda y_n : y_n == 'y' or y_n == 'n'],
    condition_fail_mes = ['Please input either "y" or "n"'])

if gen_short_hp_seq == 'y':
    short_hp_seq = sequences.generate_hairpin_stp(design)

    df = pandas.DataFrame(data = short_hp_seq, index = ['Sequences'])
    df = (df.T)
    df.to_excel('{} staple sequences.xlsx')