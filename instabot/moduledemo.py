

name = "Whatever"

def sumAny(*args):
    sum = 0
    for num in args:
      sum = sum + num
      print(sum)
      return sum









a = 4+5

locals dict = locals()
print('locals for Demo:',locals())
print('Globals for Demo:',globals())


if __name__ =='__main__':
    print("Running file as script")
    print("Calling sumAny with 1,2,3 as arguments")
    sumAny(1,2,3)



