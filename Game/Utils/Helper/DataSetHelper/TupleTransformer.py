class TupleTransformer:

    @staticmethod
    def mutiplyTuple(data, mutiplier):
        return [s * mutiplier for s in data]

    @staticmethod
    def addToTuple(data, adding_value):
        return [s + adding_value for s in data]
