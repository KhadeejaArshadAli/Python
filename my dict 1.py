def createDictionary ():
    '''Return a tiny dictionary'''
    spanish = dict ()
    spanish ['hello'] = 'hola'
    spanish ['yes'] = 'si'
    spanish ['one'] = 'uno'
    spanish ['two'] = 'dos'
    spanish ['three'] = 'tres'
    spanish ['red'] = 'rojo'
    return spanish

def main ():
    dictionary = createDictionary ()
    print (dictionary['two'])
    print (dictionary ['one'])

main ()


