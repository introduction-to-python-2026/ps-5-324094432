from fractions import Fraction

def split_before_uppercases(molecule_formula):
    """Splits a molecular formula into parts before each uppercase letter."""
    if not molecule_formula:
        return []
    start = 0
    end = 1
    split_formula = []
    while end < len(molecule_formula):
        if molecule_formula[end].isupper():
            split_formula.append(molecule_formula[start:end])
            start = end
        end += 1
    split_formula.append(molecule_formula[start:end])
    return split_formula

def split_at_digit(atom_string):
    """Splits a string like 'H2' into ('H', 2). If no digit, returns 1."""
    digit_index = 1
    for ch in atom_string[1:]:
        if ch.isdigit():
            break
        digit_index += 1
    if digit_index == len(atom_string):
        return atom_string, 1
    prefix = atom_string[:digit_index]
    number = int(atom_string[digit_index:])
    return prefix, number

def count_atoms_in_molecule(molecule_formula):
    """Returns a dictionary with atom counts in a molecular formula."""
    atom_dict = {}
    for atom_part in split_before_uppercases(molecule_formula):
        atom_name, atom_count = split_at_digit(atom_part)
        # accumulate instead of overwrite
        atom_dict[atom_name] = atom_dict.get(atom_name, 0) + atom_count
    return atom_dict

def parse_chemical_reaction(reaction_equation):
    """
    Parses a chemical reaction into reactants and products lists.
    Example: 'H2 + O2 -> H2O' → (['H2', 'O2'], ['H2O'])
    """
    reaction_equation = reaction_equation.replace(" ", "")
    reactants, products = reaction_equation.split("->")
    return reactants.split("+"), products.split("+")

def count_atoms_in_reaction(molecules_list):
    """
    Returns a list of dictionaries, each containing atom counts for a molecule.
    Example: ['H2', 'O2'] → [{'H': 2}, {'O': 2}]
    """
    return [count_atoms_in_molecule(molecule) for molecule in molecules_list]
