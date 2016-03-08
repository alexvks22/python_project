date  = input('Dwse thn hmeromhnia:')
month = raw_input("Dwse ton mhna se greeklish h se agglika:")
year = input('Dwse thn xronia:')
year_string = str(year)

#kathe minas ehei ton diko tou, monadiko, kwdiko
if month == 'December' or month =='december' or month=='dekemvrios' or month=='Dekemvrios' or month == "dekembrios" or month == "Dekembrios":
    month_code=6

if month == 'January' or month=='january' or month== 'ianouarios' or month == "Ianouarios":
    month_code=1

if month == 'February' or month=='february' or month== 'Fevrouarios' or month == "fevrouarios" or month == "febrouarios" or month == "Febrouarios" :
    month_code=4

if month == 'March' or month=='march' or month== 'martios' or month == "Martios":
    month_code=4

if month == 'April' or month=='april' or month== 'aprilios' or month == "Aprilios":
    month_code=0

if month == 'May' or month=='may' or month== 'maios' or month == "Maios":
    month_code=2

if month == 'June' or month=='june' or month== 'iounios' or month == "Iounios" :
    month_code=5

if month == 'July' or month=='july' or month== 'ioulios' or month == "Ioulios":
    month_code=0

if month == 'August' or month=='august' or month== 'aygoustos' or month == "Aygoustos":
    month_code=3

if month == 'September' or month=='september' or month== 'septemvrios' or month == "Septemvrios" or month == "septembrios" or month == "Septembrios":
    month_code=6

if month == 'October' or month=='october' or month== 'oktwvrios' or month == "Oktwvrios" or month == "oktwbrios" or month == "Oktwbrios":
    month_code=1

if month == 'November' or month=='november' or month== 'noemvrios' or month == "Noemvrios" or month == "noembrios" or month == "Noembrios":
    month_code=4



if year_string[:2] == '16': # analoga ta 2 prwta psifia, o kathe xronos antiproswpevetai apo ena kwdiko
    year_code = (6 + year%100 + (year%100)/4) % 7

elif year_string[:2]== '17':
    year_code = (4 + year%100 + (year%100)/4) % 7

elif year_string[:2]== '18':
    year_code = (2 + year%100 + (year%100)/4) % 7

elif year_string[:2]== '19':
    year_code = ( year%100 + (year%100)/4) % 7

elif year_string[:2]== '20':
   year_code = (6 + year%100 + (year%100)/4) % 7

elif year_string[:2]== '21':
    year_code = (4 + year%100 + (year%100)/4) % 7

elif year_string[:2]== '22':
    year_code = (2 + year%100 + (year%100)/4) % 7

else:
   year_code = (year%100 + (year%100)/4) % 7

day = (year_code+month_code+date) % 7

if year%4 == 0:  #ean to etos einai disekto
    day = day - 1
    if day == 0:
        print "Savvato"
    elif day == 1:
        print "Kyriaki"
    elif day == 2:
        print "Deytera"
    elif day == 3:
        print "Triti"
    elif day == 4:
        print "Tetarti"
    elif day == 5:
        print "Pempti"
    else:
        print "Paraskevi"
else:                   #gia tis ypoloipes xronologies, pou den einai disektes
    if day == 0:
        print "Savvato"
    elif day == 1:
        print "Kyriaki"
    elif day == 2:
        print "Deytera"
    elif day == 3:
        print "Triti"
    elif day == 4:
        print "Tetarti"
    elif day == 5:
        print "Pempti"
    else:
        print "Paraskevi"




