from Core.Resolver.Upgrade.GrowthFunctions.Abstract.GrowthFunction import GrowthFunction


class ExponentialIncrement(GrowthFunction):

    _base = 2

    def __init__(self, base=2):
        self._base = base

    def calculate_growth(self, value, level):
        return (level ** self._base) + value
