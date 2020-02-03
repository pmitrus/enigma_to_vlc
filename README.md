# enigma_to_vlc

script to download bouquet as vlc playlist

sorry I'm learning python so code is for sure not optimal but creates for me working vlc playlist :)


how to use?

update by ip address of your device

change userbouquet.dbe00.tv to userbouquet.dbe01.tv etc to iterate next bouquests

url = """http://192.168.0.11/web/getservices?sRef=1:7:1:0:0:0:0:0:0:0:FROM BOUQUET "userbouquet.dbe00.tv" ORDER BY bouquet"""

update place to write playlist

f= open("/home/pi/plajlista.xspf","w+")

save and run

no licence, have fun :)
