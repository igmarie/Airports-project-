def Airportlist():
    import csv
    dataline = ' '
    f = open('Airports.txt','r')
    for row in csv.reader(f):
        dataline= [row[0],row[1],row[2],row[3]]
        Airports.append(dataline)
    f.close()
    print(Airports)

def Menu()
    print('Please choose one of the following: ')
    print('[1] Input airport details')
    print('[2] Input flight details')
    print('[3] Input price')
    print('[4] Calculate profit')
    print('[Q] To Quit')
    choice = input()
    while choice !='Q':
        if choice == '1':
            print('Details for airport')
        elif choice == '2'
            print('Details for flight')
        elif choice == '2':
            print('Price')
        elif choice == '4':
            print('Calculating the profit')
        elif:
            ('please choose a option')
            
    
