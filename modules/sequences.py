import json

def generate_hairpin_stp(design, short = 'n'):
    '''Given completed design object (with named stp), generates staple sequences with hairpins inserted'''
    with open('modules/seq.json') as file:
        seqs = json.load(file)
    if short == 'n':
        hairpin_seq = seqs['hairpins']
    else:
        hairpin_seq = seqs['short hairpins']

    hairpins = {}
    i = 0
    for strand in design.strands:
        if not strand.is_scaffold:
            hairpin = strand.dna_sequence[0:16] + hairpin_seq[i] + strand.dna_sequence[16:32] #5 prime of stp + random hairpin + 3 prime of stp
            if short == 'n':
                hairpins['{}_hairpin'.format(strand.name)] = hairpin
            else:
                hairpins['{}_short_hairpin'.format(strand.name)] = hairpin
            i += 1

    return hairpins

def generate_stem_stp(design):
    '''Given completed design object (with named stp), generates staple sequences with stems inserted
    This assumes no more than 12 stp on a seed'''
    with open('modules/seq.json') as file:
        seqs = json.load(file)
    stem_seqs = seqs['3 prime stems']

    stems = {}
    for strand in design.strands:
        if not strand.is_scaffold:
            stem = strand.dna_sequence[16:32] + stem_seqs['h{}'.format(strand.name[3])] #3 prime end of the stp + the stem sequence, looked up using the helix number in the stp name
            stems['{}_stem'.format(strand.name)] = stem

    return stems

def generate_sticky_stp(design):
    '''Given completed design object (with named stp), generates staple sequences with 5' sticky ends inserted
    This assumes no more than 12 stp on a seed'''
    with open('modules/seq.json') as file:
        seqs = json.load(file)
    sticky_stem_seqs = seqs['stem of 5 prime sticky ends']
    sticky_seqs = seqs['5 prime sticky end']

    stickys = {}
    for strand in design.strands:
        if not strand.is_scaffold:
            sticky = sticky_seqs['h{}'.format(strand.name[3])] + sticky_stem_seqs['h{}'.format(strand.name[3])] + strand.dna_sequence[0:16] #sticky end + stem + 5' end of stp
            stickys['{}_stem'.format(strand.name)] = sticky

    return stickys