reedset = []
class oboeReed:
   def __init__(self, color, staple, length):
      self.color = color
      self.staple = staple
      self.ilength = length
      self.len = length
      self.clips = []
      reedset.append(self)

   def clip(self,amt):
      if amt < 5:
         amount = amt
      if amt > 5:
         amount = self.len - amt
      self.clips.append(amount)
      self.len = self.len - amount

a = oboeReed("red","bE",72)
a.clips
a.clip(69.1)
a.len

reedset[0].len