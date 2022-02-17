import sys
sys.path.append('.../')
from modules import sc_general

def scaffold_crossovers(shape_outline, seam_locations):
    """Given the shape_outline and seam locations, returns the list of scaffold crossovers
    (all as half crossovers)"""
    crossovers = []
    for helix in range(len(shape_outline)):
        crossovers_on_line = []
        if helix + 1 == len(shape_outline):
            helix2 = 0
        else:
            helix2 = helix + 1

        outline, outline2 = shape_outline[helix], shape_outline[helix2]
        row_type, row_type2 = outline[0], outline2[0]
        lines, lines2 = outline[1], outline2[1]
    
        #full crossovers on the seam, odd helices
        seams = seam_locations[helix]
        seams2 = seam_locations[helix2]
        if seams != 'no seam' and seams2 != 'no seam':
            for i in range(len(seams)):
                offset, offset2 = seams[i], seams2[i]
                if offset != 'no seam' and offset2 != 'no seam':
                    if i % 2 == 0:
                        condition = (helix % 2 == 1)
                    else:
                        condition = (helix % 2 == 0)
                    if condition and helix != len(seam_locations):
                        crossovers_on_line.append((helix, helix2, offset, offset2))
                        crossovers_on_line.append((helix, helix2, offset - 1, offset2 - 1))

        #Set right hand side to even or odd based on num of seems
        if len(seams) % 2 == 1:
            right_side_condition = (helix % 2 == 0)
        else:
            right_side_condition = (helix % 2 == 1) and (helix2 != 0)
        
        #left and right outside crossobers, half crossovers, even helices
        if helix % 2 == 0:
            left_outside, left_outside2, right_outside, right_outside2 = lines[0][0], lines2[0][0], lines[-1][1] - 1, lines2[-1][1] - 1
            crossovers_on_line.append((helix, helix2, left_outside, left_outside2))
        if right_side_condition:
            crossovers_on_line.append((helix, helix2, right_outside, right_outside2))
        #inside crossobers, half crossovers, odd helices
        if helix % 2 == 1:
            if row_type == 0 and row_type < row_type2:
                left_inside, right_inside = seam_locations[helix] - 1, seam_locations[helix]
                left_inside2, right_inside2 = lines2[0][1] - 1, lines2[1][0]
                crossovers_on_line.append((helix, helix2, left_inside, left_inside2))
                crossovers_on_line.append((helix, helix2, right_inside, right_inside2))
            for i in range(row_type):
                if row_type < row_type2:
                    left_inside, right_inside = seam_locations[helix] - 1, seam_locations[helix]
                    left_inside2, right_inside2 = lines2[i][1] - 1, lines2[i + 1][0]
                elif row_type > row_type2:
                    left_inside2, right_inside2 = seam_locations[helix + 1] - 1, seam_locations[helix + 1]
                    left_inside, right_inside = lines[i][1] - 1, lines[i + 1][0]
                else:
                    left_inside, left_inside2, right_inside, right_inside2 = lines[i][1] - 1, lines2[i][1] - 1, lines[i + 1][0], lines2[i + 1][0]
                crossovers_on_line.append((helix, helix2, left_inside, left_inside2))
                crossovers_on_line.append((helix, helix2, right_inside, right_inside2))

        if crossovers_on_line == []:
            crossovers.append('no crossover')
        else:
            crossovers.append(crossovers_on_line)

    return crossovers

def linear_scaffold_crossovers(shape_outline, seam_locations):
    """Given the shape_outline and seam locations, returns the list of scaffold crossovers
    Linear scaffold refers to a scaffold that doesn't not have a center seem"""
    crossovers = []
    for helix in range(len(shape_outline) - 1):
        crossovers_on_line = []
        if helix + 1 == len(shape_outline):
            helix2 = 0
        else:
            helix2 = helix + 1

        outline, outline2 = shape_outline[helix], shape_outline[helix2]
        row_type, row_type2 = outline[0], outline2[0]
        lines, lines2 = outline[1], outline2[1]
        
        #left and right outside crossovers, half crossovers, even helices
        left_outside, left_outside2, right_outside, right_outside2 = lines[0][0], lines2[0][0], lines[-1][1] - 1, lines2[-1][1] - 1
        if helix % 2 == 1:
            crossovers_on_line.append((helix, helix2, left_outside, left_outside2))
        if helix % 2 == 0:
            crossovers_on_line.append((helix, helix2, right_outside, right_outside2))
        #inside crossovers, half crossovers, odd helices
        if helix % 2 == 1:
            if row_type == 0 and row_type < row_type2:
                left_inside, right_inside = seam_locations[helix] - 1, seam_locations[helix]
                left_inside2, right_inside2 = lines2[0][1] - 1, lines2[1][0]
                crossovers_on_line.append((helix, helix2, left_inside, left_inside2))
                crossovers_on_line.append((helix, helix2, right_inside, right_inside2))
            for i in range(row_type):
                if row_type < row_type2:
                    left_inside, right_inside = seam_locations[helix] - 1, seam_locations[helix]
                    left_inside2, right_inside2 = lines2[i][1] - 1, lines2[i + 1][0]
                elif row_type > row_type2:
                    left_inside2, right_inside2 = seam_locations[helix + 1] - 1, seam_locations[helix + 1]
                    left_inside, right_inside = lines[i][1] - 1, lines[i + 1][0]
                else:
                    left_inside, left_inside2, right_inside, right_inside2 = lines[i][1] - 1, lines2[i][1] - 1, lines[i + 1][0], lines2[i + 1][0]
                crossovers_on_line.append((helix, helix2, left_inside, left_inside2))
                crossovers_on_line.append((helix, helix2, right_inside, right_inside2))

        if crossovers_on_line == []:
            crossovers.append('no crossover')
        else:
            crossovers.append(crossovers_on_line)

    return crossovers

def staple_nick_s_shape_no_nick_on_seam(staple_domain, seam_locations, grid_type):
    """Given the shape outline, and the seam locations, returns a list of staple nicks for s shaped staples with no nicks at the pattern center"""
    nick_locations = []
    max_offset = sc_general.find_max(staple_domain)
    if grid_type == 'square':
        multiple = 8
    else:
        multiple = 7

    for helix in range(len(staple_domain)):
        nicks_on_line = []
        center = sc_general.find_pattern_center(seam_locations, helix, staple_domain)
        seam = seam_locations[helix][0]

        #Right Side of the seam
        for offset in range(center, max_offset, multiple):
            if helix % 2 == 1:
                if (offset - center - (3 * multiple)) % (4 * multiple) == 0 or offset == seam:
                    continue
            elif helix % 2 == 0:
                if (offset - center - multiple) % (4 * multiple) == 0 or offset == seam:
                    continue
            if sc_general.is_in_outline(staple_domain, helix, offset) and sc_general.is_in_outline(staple_domain, helix, offset + 1) and sc_general.is_in_outline(staple_domain, helix, offset - 1):
                nicks_on_line.append(offset)

        #Left side of seam
        for offset in range(center - multiple, 0, - multiple):
            if helix % 2 == 1:
                if (offset + center - (3 * multiple)) % (4 * multiple) == 0 or offset == seam:
                    continue
            elif helix % 2 == 0:
                if (offset + center - multiple) % (4 * multiple) == 0 or offset == seam:
                    continue
            if sc_general.is_in_outline(staple_domain, helix, offset) and sc_general.is_in_outline(staple_domain, helix, offset + 1) and sc_general.is_in_outline(staple_domain, helix, offset - 1):
                nicks_on_line.append(offset)
        
        if nicks_on_line == []:
            nick_locations.append('no nicks')
        else:
            nick_locations.append(nicks_on_line)

    return nick_locations

def linear_staple_nick_s_shape(staple_domain, seam_locations, grid_type):
    """Given the shape outline, and the seam locations, returns a list of staple nicks for s shaped staples with no nicks at the pattern center"""
    nick_locations = []
    max_offset = sc_general.find_max(staple_domain)
    if grid_type == 'square':
        multiple = 8
    else:
        multiple = 7

    for helix in range(len(staple_domain)):
        nicks_on_line = []
        center = sc_general.find_pattern_center(seam_locations, helix, staple_domain)

        #Right Side of the seam
        for offset in range(center, max_offset, multiple):
            if helix % 2 == 0:
                if (offset - center - (3 * multiple)) % (4 * multiple) == 0:
                    continue
            elif helix % 2 == 1:
                if (offset - center - multiple) % (4 * multiple) == 0:
                    continue
            if sc_general.is_in_outline(staple_domain, helix, offset) and sc_general.is_in_outline(staple_domain, helix, offset + 1) and sc_general.is_in_outline(staple_domain, helix, offset - 1):
                nicks_on_line.append(offset)

        #Left side of seam
        for offset in range(center - multiple, 0, - multiple):
            if helix % 2 == 0:
                if (offset + center - (3 * multiple)) % (4 * multiple) == 0:
                    continue
            elif helix % 2 == 1:
                if (offset + center - multiple) % (4 * multiple) == 0:
                    continue
            if sc_general.is_in_outline(staple_domain, helix, offset) and sc_general.is_in_outline(staple_domain, helix, offset + 1) and sc_general.is_in_outline(staple_domain, helix, offset - 1):
                nicks_on_line.append(offset)
        
        if nicks_on_line == []:
            nick_locations.append('no nicks')
        else:
            nick_locations.append(nicks_on_line)

    return nick_locations

def linear_staple_nick_s_shape_scaffold_center(staple_domain, scaffold_domain, seam_locations, grid_type):
    """Given the shape outline, and the seam locations, returns a list of staple nicks for s shaped staples with no nicks at the pattern center (pattern center defined by scaffold center)"""
    nick_locations = []
    max_offset = sc_general.find_max(staple_domain)
    if grid_type == 'square':
        multiple = 8
    else:
        multiple = 7

    for helix in range(len(staple_domain)):
        nicks_on_line = []
        center = sc_general.find_pattern_center(seam_locations, helix, scaffold_domain)

        #Right Side of the seam
        for offset in range(center, max_offset, multiple):
            if helix % 2 == 0:
                if (offset - center - (3 * multiple)) % (4 * multiple) == 0:
                    continue
            elif helix % 2 == 1:
                if (offset - center - multiple) % (4 * multiple) == 0:
                    continue
            if sc_general.is_in_outline(staple_domain, helix, offset) and sc_general.is_in_outline(staple_domain, helix, offset + 1) and sc_general.is_in_outline(staple_domain, helix, offset - 1):
                nicks_on_line.append(offset)

        #Left side of seam
        for offset in range(center - multiple, 0, - multiple):
            if helix % 2 == 0:
                if (offset + center - (3 * multiple)) % (4 * multiple) == 0:
                    continue
            elif helix % 2 == 1:
                if (offset + center - multiple) % (4 * multiple) == 0:
                    continue
            if sc_general.is_in_outline(staple_domain, helix, offset) and sc_general.is_in_outline(staple_domain, helix, offset + 1) and sc_general.is_in_outline(staple_domain, helix, offset - 1):
                nicks_on_line.append(offset)
        for nick in nicks_on_line:
            print(type(nick))
        if nicks_on_line == []:
            nick_locations.append('no nicks')
        else:
            nick_locations.append(nicks_on_line)

    return nick_locations

def staple_crossovers_s_shape_loop_around_no_seam(staple_domain, seam_locations, grid_type):
    """Given the shape outline and seam location, returns a list of staple crossover locations for s shape staples which loop around to form a circluar shape"""
    crossovers = []
    if grid_type == 'square':
        multiple = 8
    else:
        multiple = 7
    for helix in range(len(staple_domain)):
        if helix + 1 == len(staple_domain):
            helix2 = 0
        else:
            helix2 = helix + 1
        crossovers_on_line = []
        center = sc_general.find_pattern_center(seam_locations, helix, staple_domain)
        max_offset = sc_general.find_max(staple_domain) + 1
        if seam_locations[helix] == 'no seam':
            seams = []
        else:
            seams = seam_locations[helix]
        if seam_locations[helix2] == 'no seam':
            seams2 = []
        else:
            seams2 = seam_locations[helix2]

        if helix % 2 == 0:
            right_side_offsets = list(range(center, max_offset, (4 * multiple)))
            left_side_offsets = list(range(center - (4 * multiple), 0, -(4 * multiple)))
        elif helix % 2 == 1:
            right_side_offsets = list(range(center + (2 * multiple), max_offset, (4 * multiple)))
            left_side_offsets = list(range(center - (2 * multiple), 0, -(4 * multiple)))  

        possible_offsets = left_side_offsets + right_side_offsets

        for i in possible_offsets:
            if sc_general.is_in_outline(staple_domain, helix, i) and sc_general.is_in_outline(staple_domain, helix2, i) and not(i in seams) and not(i in seams2):
                crossovers_on_line.append((helix, helix2, i, i))
            if sc_general.is_in_outline(staple_domain, helix, i - 1) and sc_general.is_in_outline(staple_domain, helix2, i - 1) and not(i in seams) and not(i in seams2):
                crossovers_on_line.append((helix, helix2, i - 1, i - 1))
            else:
                continue
        
        crossovers.append(crossovers_on_line)
    
    return crossovers

def linear_staple_crossovers_s_shape_loop_around(staple_domain, seam_locations, grid_type):
    """Given the shape outline and seam location, returns a list of staple crossover locations for s shape staples which loop around to form a circluar shape"""
    crossovers = []
    if grid_type == 'square':
        multiple = 8
    else:
        multiple = 7
    for helix in range(len(staple_domain)):
        if helix + 1 == len(staple_domain):
            helix2 = 0
        else:
            helix2 = helix + 1
        crossovers_on_line = []
        center = sc_general.find_pattern_center(seam_locations, helix, staple_domain)
        max_offset = sc_general.find_max(staple_domain) + 1

        if helix % 2 == 1:
            right_side_offsets = list(range(center, max_offset, (4 * multiple)))
            left_side_offsets = list(range(center - (4 * multiple), 0, -(4 * multiple)))
        elif helix % 2 == 0:
            right_side_offsets = list(range(center + (2 * multiple), max_offset, (4 * multiple)))
            left_side_offsets = list(range(center - (2 * multiple), 0, -(4 * multiple)))  

        possible_offsets = left_side_offsets + right_side_offsets

        for i in possible_offsets:
            if sc_general.is_in_outline(staple_domain, helix, i) and sc_general.is_in_outline(staple_domain, helix2, i):
                crossovers_on_line.append((helix, helix2, i, i))
            if sc_general.is_in_outline(staple_domain, helix, i - 1) and sc_general.is_in_outline(staple_domain, helix2, i - 1):
                crossovers_on_line.append((helix, helix2, i - 1, i - 1))
            else:
                continue
        crossovers.append(crossovers_on_line)
    
    return crossovers

def linear_staple_crossovers_s_shape_loop_around_scaffold_center(staple_domain, scaffold_domain, seam_locations, grid_type):
    """Given the shape outline and seam location, returns a list of staple crossover locations for s shape staples which loop around to form a circluar shape, using the scaffold to define pattern center"""
    crossovers = []
    if grid_type == 'square':
        multiple = 8
    else:
        multiple = 7
    for helix in range(len(staple_domain)):
        if helix + 1 == len(staple_domain):
            helix2 = 0
        else:
            helix2 = helix + 1
        crossovers_on_line = []
        center = sc_general.find_pattern_center(seam_locations, helix, scaffold_domain)
        max_offset = sc_general.find_max(staple_domain) + 1

        if helix % 2 == 1:
            right_side_offsets = list(range(center, max_offset, (4 * multiple)))
            left_side_offsets = list(range(center - (4 * multiple), -1, -(4 * multiple)))
        elif helix % 2 == 0:
            right_side_offsets = list(range(center + (2 * multiple), max_offset, (4 * multiple)))
            left_side_offsets = list(range(center - (2 * multiple), -1, -(4 * multiple)))  

        possible_offsets = left_side_offsets + right_side_offsets

        for i in possible_offsets:
            if sc_general.is_in_outline(staple_domain, helix, i) and sc_general.is_in_outline(staple_domain, helix2, i):
                crossovers_on_line.append((helix, helix2, i, i))
            if sc_general.is_in_outline(staple_domain, helix, i - 1) and sc_general.is_in_outline(staple_domain, helix2, i - 1):
                crossovers_on_line.append((helix, helix2, i - 1, i - 1))
            else:
                continue

        crossovers.append(crossovers_on_line)
    
    return crossovers