
from rdkit import Chem
from rdkit.Chem.rdmolfiles import MolFromSmiles
from rdkit.Chem import Draw

col = {
   "nicodozole" : "COC(=O)NC1=NC2=CC=C(C(=O)C3=CC=CS3)C=C2N1",
   "benzene" : "c1ccccc1",
   "glycine" : "NCC(=O)O",
   "tyrosine" : "NC(c1ccc(O)cc1)C(=O)O",
   "alanine" : "NC(C)C(=O)O",
   "GWA" : "NCC(=O)ONC(c1ccc(O)cc1)C(=O)ONC(C)C(=O)O"
}


def molv (mol_name:str):
   n = MolFromSmiles(col[mol_name])
   Draw.MolToImage(n).show()

molv("nicodozole")