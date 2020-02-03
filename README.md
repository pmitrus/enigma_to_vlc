# enigma_to_vlc

script to download bouquet as vlc playlist

sorry I'm learning python so code is for sure not optimal but creates for me working vlc playlist :)


how to use?

a) update by ip address of your device in all lines where you see http://192.168.0.11

b) change userbouquet.dbe00.tv to userbouquet.dbe01.tv etc to iterate next bouquests

url = """http://192.168.0.11/web/getservices?sRef=1:7:1:0:0:0:0:0:0:0:FROM BOUQUET "userbouquet.dbe00.tv" ORDER BY bouquet"""

and 

 f.write("\t\t\t<location>http://192.168.0.11:8001/"+programy['e2servicereference']+"</location>\r\n")


update place to write playlist

f= open("/home/pi/plajlista.xspf","w+")

save and run

no licence, have fun :)
