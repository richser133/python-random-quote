import random

def first():
  print("Keep it logically awesome.")

  f = open("quotes.txt")
  quotes = f.readlines()
  last = len(quotes) - 1
  rdn = random.randint(0, last)
  f.close()

  print(quotes[rnd])

if __name__== "__main__":
  first()
