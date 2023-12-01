def f(*args, **kwargs):
    print("Positional:", args)
    print("Named:", kwargs)


f(100, 50, 25, 5, name="Alex")