from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.keyboard import VkKeyboard, VkKeyboardColor
import vk_api
from datetime import datetime
from datetime import date
import random
import time
import pytz
import datetime
import calendar
import time
import mysql.connector
import os
vk_session = vk_api.VkApi( token= os.environ.get('BOT_TOKEN') )
session_api = vk_session.get_api()
longpoll = VkLongPoll(vk_session)
def sqlQuery( query, number ):
   ps = os.environ.get('PASSWORD')
   conn = mysql.connector.connect( host = 'sql2.freemysqlhosting.net', user = 'sql2297188', password = str(ps), database = 'sql2297188' )
   cursor = conn.cursor()
   cursor.execute(query)
   if number == 1:
       result = cursor.fetchall()
       return result
   if number == 2:
       conn.commit()
       cursor.close()
       conn.close()
#vk_session.method('board.addTopic', {'group_id': '177844818', 'title': 'Testik', 'text': 'aaaaaaaaaaaaaaa', 'from_group':'1'})
def timez():
    x = str( datetime.datetime.now(pytz.timezone("Europe/Moscow")) )
    return int( x[11:13]), int( x[14:16]), int( x[17:19])
def mounth():
    x = str( datetime.datetime.now(pytz.timezone("Europe/Moscow")) )
    return int( x[5:7] )
def chislo():
    x = str( datetime.datetime.now(pytz.timezone("Europe/Moscow")) )
    return int( x[8:10] )
    #return 5
def hoursMinutes():
    now = str( datetime.datetime.now(pytz.timezone("Europe/Moscow")) )
    res = now[11:16]
    return int( res[0:2] ) * 60 + int( res[3:5] )
def diskussion():
    if mounth() < 10:
        mounthd = '0' + str( mounth() )
    else:
        mounthd = str( mounth() )
    if mounth() - 1 < 10:
        lastmounthd = '0' + str( mounth() - 1 )
    else:
        lastmounthd = str( mounth() - 1 )
    if chislo() >= 8:
        mas = [0]*7
        for i in range( chislo() - 7, chislo() ):
            if i < 10:
                mas[i] = '0' + str( i ) + '.' + str( mounthd )
            else:
                mas[i] = str( i ) + '.' + str( mounthd )
    else:
        x = calendar.monthrange( 2019, mounth() - 1 )[1]
        mas = []
        for i in range( x + chislo() - 7 , x + 1 ):
            mas.append( str( i ) + '.' + str( lastmounthd ) )
        for i in range( 1, chislo() ):
            mas.append( '0' + str( i ) + '.' + str( mounthd ) )
    return mas
def tostring( string ):
    tmp = ''
    for i in range(0, len(string) - 1 ):
        if string[i]!=' ' or string[i+1] != ' ':
            tmp = tmp + string[i]
    if string[len(string) - 1] != ' ':
        tmp = tmp + string[len(string) - 1]
    return tmp
while True:
    x,y,z= timez()
    if x  == 0 and y == 0 and z == 0:
        if date( 2019, mounth(), chislo() ).isoweekday() == 1:
            result = sqlQuery( 'select * from everyData', 1 )
            i = 0
            string = ''
            while True:
                try:
                    tmpnick = tostring( str( result[i][0] ) )
                    onlik = 0
                    mas = diskussion()
                    print( mas[6] )
                    for j in range( 6, -1, -1 ):
                        try:
                            tmpOnlik = tostring( str( sqlQuery( "select `" + str( mas[j] ) + "` from everyData where nick ='" + str( tmpnick ) + "'", 1 )[0][0] ) )
                        except Exception:
                            tmpOnlik = 'None'
                        if tmpOnlik != 'None':
                            onlik = onlik + int( tmpOnlik )
                        print( tmpOnlik )
                    onlik = str( onlik//60 ) + ' hours, ' + str( onlik%60 ) + ' minutes'
                    string = string + str( tmpnick ) + ' - ' + str( onlik ) + '\n'
                    i = i + 1
                except Exception:
                    break
            vk_session.method('board.addTopic', {'group_id': '177844818', 'title': 'Онлайн ['+str(mas[0]) + ' - ' + str(mas[6] ) + ']', 'text': str( string ), 'from_group':'1'})
    time.sleep(1)

                    
                             
                            
                            

                        
