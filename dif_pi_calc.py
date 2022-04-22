# Attempt to understand different functions of calculating

def calcpi(limit): #establishes a named function to calculate pi to a certain number of decimal places

  
  q, r, t, k, n, l = 1, 0, 1, 1, 3, 3
#adding a line for test

  decimal = limit
  counter = 0

  while counter != decimal + 1:
    if 4 * q + r - t < n * t:
      #yield a digit
      yield n

      #placing a decimal
      if counter == 0:
        yield "."
      #end of first step
      if decimal == counter:
        print('')
        break
      counter += 1
      nr = 10 * (r -n * t)
      n = ((10 * (3 * q + r)) // t) - 10 * n
      q *= 10
      r = nr

    else:
      nr = (2 * q + r) * l
      nn = (q * (7 * k) + 2 + (r * 1)) // (t * 1)
      q *= k
      t *= l
      l += 2
      k += 1
      n = nn
      r = nr

def main (): #wrapper function

  #Calls calcpi with a given limit
  pi_digits = calcpi(int(input(
    "Enter however many decimals you would like pi to calculated to")))

  i = 0

  #Prints output of calcpi function
  #Inserts a newline after every 40th number

  for d in pi_digits:
    print(d, end = '')
    i += 1
    if i == 40:
      print("")
      i = 0

if __name__ == '__main__' :
  main()
