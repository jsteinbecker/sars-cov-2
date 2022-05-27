import re
import datetime
import markdown 




def iconMD_to_HTML   (body:str ,format_="md"):
   """ FUNCTION REPLACING [MD] ICONS --> [HTML] REPRS
   -----------------------------------------------------------
   
   Finds:
   >>> icon[cloud]
                        -->   <i class="fas fa-cloud"></i>
   """
   if format_ == "md":
      body = markdown.markdown(body,extensions=['tables'])
   else:
      pass
   
   search = re.findall("(icon\[(.*?)\])",body)
   for tupl in search:
      replacement = '<i class="fas fa-' + tupl[1].lower() + '"></i>'
      body = body.replace(tupl[0],replacement)
   
   return body
   
a= """

# Josh Steinbecker icon[user] 

## icon[vampire] Bat Coronaviruses

Bat icon[virus] coronaviruses can be dangerous.

Josh | Steinbecker
----- | -------------
icon[clown] | CLown 
icon[math] | Math 
icon[dog] | Dog 
icon[user] | User

"""

def writeFile (a):
   TIMESTAMP = str(datetime.datetime.now().isoformat())[0:16]
   content  = """<!DOCTYPE html>
<html>
<head>
<title>Font Awesome Icons</title>

<meta name="viewport" content="width=device-width, initial-scale=1">

<script src="https://kit.fontawesome.com/6f5ec410dd.js" crossorigin="anonymous"></script>

<style>
   * { 
         background-color:  #111144;
         font-family:         "Jetbrains Mono";
      }
</style>

</head>


<body>
"""
   content += iconMD_to_HTML(a)
   content += "\n</body>\n</html>"
   f = open("content" + TIMESTAMP + ".html","x")
   f.write(content)
   f.close()

writeFile(a)

table = """Josh | Steinbecker
-----|-------------
icon[clown] | CLown 
icon[math] | Math 
icon[dog] | Dog 
icon[user] | User """

writeFile(table)