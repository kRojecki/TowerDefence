class ClassProvider:

    @staticmethod
    def provide_class(class_type):
        parts = class_type.split('.')
        module = ".".join(parts[:-1])
        m = __import__(module)
        for comp in parts[1:]:
            m = getattr(m, comp)
        return m
