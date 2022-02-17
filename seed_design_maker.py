import sys, os, pandas
sys.path.append('.../')
from modules import sc_general
from modules import sc_pattern
from modules import sc_create
from modules import sequences

#This script assumes a 12 helix seed, with no empty regions, and a linear S shaped scaffold, on a square lattice (8 bp multiples)

design_name = input('Design name: ')

sequence_name = input('Scaffold sequence name (make sure sequence is in seq.json): ')

seed_legnth = None
while type(seed_legnth) != int:
    try:
        seed_legnth = int(input('Desired Seed Legnth (in bp, must be divisible by 16): '))
        if seed_legnth % 16 != 0:
            seed_legnth = None
            print('Seed legnth must be a multiple of 16')
    except:
        print('Please input an integer for the seed legnth')

sidedness = None
while type(sidedness) != int:
    try:
        sidedness = int(input('Is this a one-sided or two-sided seed?(1 or 2): '))
        if not(sidedness == 1 or sidedness == 2):
            sidedness = None
            print('Please input sided-ness as "1" or "2"')
    except:
        print('Please input sided-ness as "1" or "2"')

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

gen_short_hp_seq = None
while type(gen_short_hp_seq) != bool:
    a = input('Do you want to export staple sequences with short hairpins? (y/n): ')
    if a == 'y':
        gen_short_hp_seq = True
    elif a == 'n': 
        gen_short_hp_seq = False
    else:
        print('Please input either "y" or "n"')

if gen_short_hp_seq:
    short_hp_seq = sequences.generate_hairpin_stp(design)

    df = pandas.DataFrame(data = short_hp_seq, index = ['Sequences'])
    df = (df.T)
    df.to_excel('{} staple sequences.xlsx')