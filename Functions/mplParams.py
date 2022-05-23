from matplotlib import rcParams



BACKGROUND_D = "#1B1F28"
BACKGROUND_L = "#232732"
ORANGE =       "#DDAD79"
GREEN  =       "#B8CB9A"

PALETTE_DICT = {
   'Red'    :'tomato', 
   'Blue'   :'cornflowerblue', 
   'Purple' :'mediumpurple', 
   "Pink"   :'pink', 
   'Emperor':'orange', 
   'Berry'  :'orchid', 
   'Mint'   :'palegreen'
}

rcParams['axes.facecolor']    = BACKGROUND_L
rcParams['figure.facecolor']  = BACKGROUND_D
rcParams['axes.labelcolor']   = GREEN

rcParams['axes.titlecolor']   = 'white'
rcParams['axes.titleweight']  = "bold"
rcParams['axes.edgecolor']    = 'white'
rcParams['xtick.labelcolor']  = 'white'
rcParams['ytick.labelcolor']  = 'white'