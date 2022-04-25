def spam(divideBy):
    try:
        return 42/divideBy
    except:
        print("invalid argument")

print(spam(42))
print(spam(0))
