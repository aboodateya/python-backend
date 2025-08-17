def multiplier_generator(base):
    if base ==0:
        def inner(value):
            return value * value
    else:
        def inner(value):
            return value * base
        return inner
    if __name__=="__main":
        doubler =multiplier_generator(2)
        tripler =multiplier_generator(3)
        squarer =multiplier_generator(0)

        print("Doubler(5):",doubler(5))
        print("Tripler(4):",tripler(4))
        print("Squarer(6):",squarer(6))
        