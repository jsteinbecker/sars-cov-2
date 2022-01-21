
nicodozole = "COC(=O)NC1=NC2=CC=C(C(=O)C3=CC=CS3)C=C2N1"

from rdkit import Chem
from rdkit.Chem.rdmolfiles import MolFromSmiles
from rdkit.Chem import Draw

n = MolFromSmiles(nicodozole)
type(n)
Draw.MolsToImage(n)
