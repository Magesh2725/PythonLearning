def isANumber():
    while True:
        try:
            result = int(input('Enter your number of choice'))
        except:
            print('Thats not a number!')
        else:
            break
        finally:
            print('I am a finaly statement')




isANumber()

