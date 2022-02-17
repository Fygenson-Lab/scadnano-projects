These modules make use of a list structure referred to a as a shape outline.
Shape outlines have the following format:
    [helix 0 tuple, helix 1 tuple, . . .]
    helix n tuple = (row type, [(start, end), (start, end), . . .])
        where row type = the number gaps in the helix
        aka if a helix has one open game then row type = 0 and the associated list only has one start end tuple.

        if a row has one gap then the helix tuple would look like this
        (1, [(start, end), (start, end)])

It also uses lattice domains.
A lattice domain has the structure (x_positions, y_positions) where x_positions and y_positions are both a list of coordinates.

To form a design, first make this shape outline object.
If the staples do not span the entire scaffold, then make a second shape outline object for the staple domain (or hairpin domain etc...).
Then make the lattice domain for the shape (and the hairpin lattice etc . . .)

Then use the functions in the sc.pattern module to find all the nick and crossover locations.

Finally use the sc.create functions to create the initial design, precursor scaffold, scaffold nicks, scaffold crossovers, precursor staples, staple nicks, and staple crossovers.

The seed_design_maker is provided as an example, and as a shortcut to make any size seed.