def planet_weight(weight, planet):
  if planet == 1:
    weight = weight * 0.91
  elif planet == 2:
    weight = weight * 0.38
  elif planet == 3:
    weight = weight * 2.34
  elif planet == 4:
    weight = weight * 1.06
  elif planet == 5:
    weight = weight * 0.92
  else:
    weight = weight * 1.19

  
  return "Your weight: " + str(round(weight, 2)) + " lbs."