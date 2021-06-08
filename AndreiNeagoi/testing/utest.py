def do_stuff(num):
    try:
        if num != None:
            return int(num)+5

        else:
            return 'please try again'
    except ValueError as err:
        return err
