class TupleTransformer:

    @staticmethod
    def mutiplyTuple(data, mutiplier):
        for element, key in data:
            data[key] = element * mutiplier;
        return data

    @staticmethod
    def addToTuple(data, adding_value):
        for element, key in data:
            data[key] = element + adding_value;
        return data
