# Ethan Busbee

from random import randint
import traceback

class Die(object):

  def __init__(self, sides = 6):
    if sides < 2: raise Exception("Not enough sides! (Minimum 2)")
    self.sides = sides

  def roll(self):
    return randint(1, self.sides)

class Dice(object):

  def __init__(self):
    self._dice = []

  def addDie(self, sides = 6, count = 1):
    try:
      die = Die(sides = sides)
      for run in range(count):
        self._dice.append(die)
    except:
      print str(traceback.format_exc())
      print "\nAlso this means your die wasn't added."

  def roll(self, count = 1):
    results = []
    for run in range(count):
      result = []
      for die in self._dice:
        result.append(die.roll())
      results.append(result)
    return results