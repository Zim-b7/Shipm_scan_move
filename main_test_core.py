#import mysql
print ("Welcome to shipment flow application\nk - to start scan\nq - to quit application")
starter = input ()
while starter != 'k' and starter != 'q':
    print("Only k or q are available, try again")
    starter = input()
while starter == 'k':
    print("First scan shipment and then zone_from -> zone_to:")
    shipm = input()
    shipm = int(shipm)
    while shipm < 804000000000000:
        print ("Incorrect shipment value try again:")
        shipm = input()
        shipm = int(shipm)
    else: print ("You are ready to scan zone_from:")
    zone_from = input()
    while zone_from == '' or ' ' in zone_from or zone_from == '0':
        print ("zone_from can't be empty/contain spaces, check it and try again")
        zone_from = input()
    else: print ("You are ready to scan zone_to:")
    zone_to = input()
    while zone_to == '' or ' ' in zone_to or zone_to == '0':
        print ("zone_to can't be empty/contain spaces, check it and try again:")
        zone_to = input()
    else: print ("You have finished input\nShipment:%s\nMoving: %s -> %s" % (shipm,zone_from,zone_to))
    print ("Another scan?\nk - go on\nq - quit")
    starter = input()
    while starter != 'k' and starter!= 'q':
        print ("Only k or q are available, try again")
        starter = input()
#cnx = mysql.connect(user='root', password='',
#                                host='192.168.200.10',
#                                database='asd')
#x = cnx.cursor()
#x.execute("SELECT * FROM SSCConTrip")
#cnx.close()