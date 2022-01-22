
nicodozole = "COC(=O)NC1=NC2=CC=C(C(=O)C3=CC=CS3)C=C2N1"
benzene = "c1ccccc1"

from rdkit import Chem
from rdkit.Chem.rdmolfiles import MolFromSmiles
from rdkit.Chem import Draw

n = Chem.MolFromSmiles(benzene)
Chem.Draw.MolsToImage(n)
