def tour():

    print('Welcome to Lotus Travels\n\nPlease choose your favorite trip\n\n1. Singapore Rs.30000 for 3D/2N\n2. New York Rs.50000 for 3D/2N')
    print('3. Delhi Rs.20000 7D/6N ')
    c=int(input('Your Choice:'))
    if c==1:
        n=int(input('How many people:'))
        exp = n*30000
        gst=(18.0/100)*exp
        print('Total Expense including GST of 18% will be Rs.',exp+gst)
    elif c==2:
        n = int(input('How many people:'))
        exp = n * 50000
        gst = (18.0/100) * exp
        print('Total Expense including GST of 18% will be Rs.', exp + gst)
    elif c==3:
        n = int(input('How many people:'))
        exp = n * 20000
        gst = (18.0/100) * exp
        print('Total Expense including GST of 18% will be Rs.', exp + gst)
    else:
        print('Wrong option')
tour()
tour()

