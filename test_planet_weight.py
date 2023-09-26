import planet_weight

def test_planet_weight():
  assert planet_weight.planet_weight(185, 1) == 'Your weight: 168.35 lbs.'
  assert planet_weight.planet_weight(168, 2) == 'Your weight: 63.84 lbs.'
  assert planet_weight.planet_weight(146, 3) == 'Your weight: 341.64 lbs.'
  assert planet_weight.planet_weight(180, 4) == 'Your weight: 190.8 lbs.'
  assert planet_weight.planet_weight(160, 5) == 'Your weight: 147.2 lbs.'
  assert planet_weight.planet_weight(150, 6) == 'Your weight: 178.5 lbs.'
  