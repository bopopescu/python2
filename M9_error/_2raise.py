try:
    num = int(input(" input score : "))
    if num<0 or num >100:
      raise ValueError
    else:
      print("score: ",num)
except ValueError:
    print("score:  100 >  score > 0 ")