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
        hackername.append('zz@_')
        break
      hackername.append(l)

    hackername.append(split(ln)[0])
    self.hackername = ''.join(hackername)

fn = str(input('First name: '))
ln = str(input('Last name: '))

print(f'Hackername: {Hackername(fn, ln).hackername}') 
