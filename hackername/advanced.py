#This is the work with the addons provided (mutiple inputs, something random instead of "zz@_")
import random
middle_things = ['@admin.', '^root_', 'potato']
remove_at = ['a', 'e', 'i', 'o', 'u']

def split(word):
    return [char for char in word]

class Hackername():
  """Creates the Hackername, has first and last name as additional properties"""
  def __init__(self, fn:str, ln:str):
    self.first_name = fn
    self.last_name = ln

    hackername = list()
    for l in split(fn):
      if l.lower() in remove_at:
        hackername.append(l)
        hackername.append(random.choice(middle_things))
        break
      hackername.append(l)

    hackername.append(split(ln)[0])
    self.hackername = ''.join(hackername)

fn = []
ln = []
hn = list()

while True:
  fn_i = str(input('First name: '))
  if not fn_i.lower() == 'x':
    fn.append(fn_i)
    ln_i = str(input('Last name: '))
    ln.append(ln_i)
  else:
    x = 0
    for item in fn:
      hn.append(Hackername(item, ln[x]).hackername)
      x = x+1
    break
    
print('Hackernames: ' + "\n".join(hn)) 
