from Core.Resolver.Upgrade.GrowthFunctions.Abstract.GrowthFunction import GrowthFunction


class LinearIncrement(GrowthFunction):

    _step = 1

    def __init__(self, step=1):
        self._step = step

    def calculate_growth(self, value, level):
        return value + self._step
