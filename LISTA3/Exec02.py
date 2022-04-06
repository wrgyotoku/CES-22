# decorador
def p_decorate(func):
    def wrapper(kind, *arguments, **keywords): 
        func(kind, *arguments, **keywords)
        print("That is a nice place indeed")
    return wrapper
# decorador aplicado na funcao places
@p_decorate
def places(kind, *arguments, **keywords):
    print ("Say a nice country:", kind)
    for arg in arguments:
        print (arg)
    print ("-" * 28)
    keys = sorted(keywords.keys())
    for kw in keys:
        print (kw, ":", keywords[kw])

places("Brazil", "A place that have a nice food",
    "and the people are happy",
    sport="Soccer",
    food="Barbecue",
    paradise="Paraty",
    drink="Caipirinha")