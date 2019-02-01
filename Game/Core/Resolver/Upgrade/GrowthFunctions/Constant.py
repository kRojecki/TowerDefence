from Core.Resolver.Upgrade.GrowthFunctions.Abstract.GrowthFunction import GrowthFunction


class Constant(GrowthFunction):

    def calculate_growth(self, value, level):
        return value
