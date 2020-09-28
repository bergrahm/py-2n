def raise_to(exp):
    def raise_to_exp(x):
        return pow(x, exp)
    return raise_to_exp

def main(x):
    square = raise_to(x)
    square(x)

if __name__ == "__main__":
    import sys
    print(sys.argv[1])
    main((sys.argv[1]))