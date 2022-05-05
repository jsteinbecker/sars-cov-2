from dataclasses import dataclass, field


@dataclass
class IdealBodyWeight:
    inches:int
    IBW:int = 0
    IBW_in_pounds:float = 0
    
    def __post_init__(self):
        self.IBW = (self.inches-60)*2.3 + 50
        self.IBW_in_pounds = self.IBW * 2.2
    def __repr__(self):
        return f'{str(self.IBW)} kg ({str(round(self.IBW_in_pounds,1))} lbs)'

@dataclass
class CrCl:
    age:int
    weight_kg_:int
    Serum_Creat:float

    def __post_init__ (self):
        self.FIELD = 'CREATINE CLEARANCE'
        self.CrCl = round(((140 - self.age) * self.weight_kg_ )/(72 * self.Serum_Creat),2)
        self.INFOSOURCE = "source: Cockroft-Gault Method"
        self.calcRefRange()
        
    def calcRefRange (self):
        #REF RANGE
        if self.CrCl < 30:
            self.REFRANGE = 'Severly Impaired Renal Function'
        if 30 <= self.CrCl < 60:
            self.REFRANGE = 'Impaired Renal Function'
        if 60 < self.CrCl <= 90:
            self.REFRANGE = 'Mildly Impaired Renal Function'
        if 90 < self.CrCl:
            self.REFRANGE = 'Normal Renal Function'
    def __repr__ (self):
        return f'{str(self.CrCl)} <CrCl>  {self.REFRANGE} ({self.age}yr, {self.weight_kg_}kg, {self.Serum_Creat}SCr)'
     
@dataclass
class Patient:
    name:str
    age:int
    height_in_:int
    weight_kg_:int
    SCr:float
    CrCl:CrCl = field(init=False)

    def __post_init__(self):
        self.CrCl = CrCl(self.age,self.weight_kg_,self.SCr)
        self.IBW = IdealBodyWeight(self.height_in_)
        self.ROOM = None
    def __assignRoom__(self,room):
        self.ROOM = room
    def __repr__(self):
        return f'{"-"*65}\n\n{self.name}:\n   {self.age}yr, {self.height_in_}in, {self.weight_kg_}kg, [IBW: {self.IBW.IBW}kg]\n   ({self.CrCl})\n{"-"*65}'
     

def makePatient(name,age,ht,kg,SCr):
    return Patient(name,age,ht,kg,SCr)