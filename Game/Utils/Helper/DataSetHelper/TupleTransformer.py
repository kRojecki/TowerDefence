class TupleTransformer:

    @staticmethod
    def mutiply_tuple(data, mutiplier):
        return [s * mutiplier for s in data]

    @staticmethod
    def add_to_tuple(data, adding_value):
        return [s + adding_value for s in data]

    @staticmethod
    def add_tuples(tuple1, tuple2):
        if len(tuple1) != len(tuple2):
            raise Exception('Tuples have different sizes')

        i = 0
        tuple1 = list(tuple1)

        for e in tuple1:
            tuple1[i] += tuple2[i]
            i += 1

        return tuple(tuple1)

    @staticmethod
    def negate_tuple(tuple1):

        tuple_tmp = list(tuple1)

        i = 0
        for e in tuple_tmp:
            tuple_tmp[i] = -tuple_tmp[i]
            i += 1

        return tuple(tuple_tmp)
