import re
def praclog (x):
   x = re.sub("(?<=:\d\d)\s","\n",x)
   y = re.findall(".*(?<=:\d\d)(?=\n)",x)
   for i in y:
      if i == "":
         y.remove(i)
   return y

t ="Epilogue- La La Land -EC (Hurwitz) 0:39 Bagatelle No. 1 0:12 Symphony No. 1 -CT (Brahms) 0:06 Ballad of Mesopotamia 0:06 Across the Stars 0:05 Battle of the Heroes 0:03 Der Erlkonig -VN (Ernst) 0:03 Daily Report 0:02 Candide -CL (Bernstein) 0:02 09 Clar 1--Candide 0:02 Tragic Overture -CO (Brahms) 0:02 Run Free -CT (Zimmer) 0:02 Katchaturian > Violin Concerto > D min... 0:02 Andante Festivo 0:01 Vitali Chaconne 0:01 503, Angels and Demons 0:01 Run Free 0:01 2 Serenades Op. 69 -VN (Sibelius) 0:01 Run Free 0:01"
tt = praclog(t)

z = [re.findall("(?<=\().*(?=\))",i) for i in tt]
z