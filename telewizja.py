import traceback
import urllib3
import xmltodict

def getxml():
    #update by ip address of your device
    #change userbouquet.dbe00.tv to userbouquet.dbe01.tv etc to iterate next bouquests
    url = """http://192.168.0.11/web/getservices?sRef=1:7:1:0:0:0:0:0:0:0:FROM BOUQUET "userbouquet.dbe00.tv" ORDER BY bouquet"""

    http = urllib3.PoolManager()

    response = http.request('GET', url)
    try:
        data = xmltodict.parse(response.data)
    except:
        print("Failed to parse xml from response (%s)" % traceback.format_exc())
    return data


doc = getxml()
#update place to write playlist
f= open("/home/pi/plajlista.xspf","w+")

f.write("""<?xml version="1.0" encoding="UTF-8"?>\r\n""")
f.write("""<playlist xmlns="http://xspf.org/ns/0/" xmlns:vlc="http://www.videolan.org/vlc/playlist/ns/0/" version="1">\r\n""")
f.write("""\t<title>Lista odtwarzania</title>\r\n""")
f.write("""\t<trackList>\r\n""")

i=0

for programy in doc['e2servicelist']['e2service']:
    f.write("""\t\t<track>\r\n""")
    f.write("\t\t\t<location>http://192.168.0.11:8001/"+programy['e2servicereference']+"</location>\r\n")
    f.write("\t\t\t<title>"+programy['e2servicename']+"</title>\r\n")
    f.write("""\t\t\t<extension application="http://www.videolan.org/vlc/playlist/0">\r\n""")
    f.write("\t\t\t\t<vlc:id>"+str(i)+"</vlc:id>\r\n")
    f.write('\t\t\t</extension>\r\n')
    f.write("""\t\t</track>\r\n""")
    i=i+1

f.write("""\t</trackList>\r\n""")

f.write("""\t<extension application="http://www.videolan.org/vlc/playlist/0">\r\n""")

i=0

for programy in doc['e2servicelist']['e2service']:
    f.write('\t\t<vlc:item tid="'+str(i)+'"/>\r\n')
    i=i+1

f.write("""\t</extension>\r\n""")
f.write("""</playlist>\r\n""")
f.close()