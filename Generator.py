# Ethan Busbee

from Dice import Dice

class Generator(object):

  def __init__(self):
    self._hand = Dice()
    self._hand.addDie(sides = 6, count = 4) # init to 4d6

  def __del__(self):
    pass

  def _rollBaseNumbers(self):
    return self._hand.roll(count = 6)

  def _generateScoreList(self):
    # roll 4d6 x 6
    rolls = self._rollBaseNumbers()

    # drop lowest from each set and sum remaining rolls into output
    output = []
    for rollset in rolls:
      rollset.remove(min(rollset))
      output.append(sum(rollset))

    return sorted(output, reverse = True)

  def generateScoreLists(self, count = 1):
    output = []
    for i in range(count):
      output.append(self._generateScoreList())
    return sorted(output, reverse = True)
