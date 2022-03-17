# %%
import base64
from IPython.display import Image, display
import matplotlib.pyplot as plt

def mm(graph):
  graphbytes = graph.encode("ascii")
  base64_bytes = base64.b64encode(graphbytes)
  base64_string = base64_bytes.decode("ascii")
  display(Image(url="https://mermaid.ink/img/" + base64_string))

mm("""
graph LR;
    A--> B & C & D;
    B--> A & E;
    C--> A & E;
    D--> A & E;
    E--> B & C & D;
""")

# %%
g = """
graph TD;
   IV((IVRoom)) --> MI{MI} & 7C{7C} & EI & N
   R((Runner)) --> 7C & MI & EP & 3
   PD((PDesk)) --> 7P & EP & N
"""
mm(g)

# %%
g = """
%%{init: {'theme': 'dark'}%%
        graph TD
          A[fa:fa-tree Christmas] -.->| fa:fa-money Get money .| B(Go shopping)
          B -.-> C{fa:fa-cloud <br> Let me think...}
          C -.-> B
          B --> G[/fa:fa-gemini Another/]
          C ==>|One| D[fa:fa-laptop Laptop_ ]
          C -->|Two| E[fa:fa-mobile iPhone_ ]
          C -.->|Three| F(fa:fa-car Car_)
          subgraph "section"
            C
            D
            E
            F
            G
          end"""
mm(g)

# %%
%%HTML
<p>hjk
<a href="{% static 'fontawesomefree/css/all.min.css' %}" rel="stylesheet" type="text/css"></p>


# %%
g = """
graph TD;
  genwk --calcs--> genrow
"""
mm(g)
# %%
