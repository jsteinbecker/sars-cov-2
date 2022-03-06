import re

def markdownTable_to_CSV (text):
   """
   -------------------------
   Markdown Table -> CSV
   -------------------------
   in: STRING
   reqires:
      - Start     `<TABLE>`
      - Separator     `|`
      - End line     `***`

   >>> out: STRING, .csv format
   -------------------------
   """
   
   #-- Extract Table from Other Text
   re_pattern = '(?<=\<TABLE\>)[\w\W]*(?=\*\*\*)'
   tables = re.findall (re_pattern, text )

   #-- Delete the " -----|------|------ " Row
   re_pattern = '\n-+\|-+(?=\n)'
   converted = re.sub(re_pattern,"",tables[0])
   converted
   #-- Remove Leading Newline
   converted_v2 = re.sub('^\n',"",converted)
   #-- Replace | with ,
   converted_v3 = re.sub('\|',',',converted_v2)
   return converted_v3


ex_text = """
blah blah blah

<TABLE>
Phone | Techician
-----|----------
1147 | Runner
2013 | IV-Room
6833 | Carousel
2010 | Med-Rec
***

Blah blah blah """

print (markdownTable_to_CSV (ex_text) )