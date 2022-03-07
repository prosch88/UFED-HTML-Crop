import os
import string
import sys

print("\nUFED HTML Report Crop - © Christian Peter - 2020\n")

try:
    try:
        with open("Report.html", encoding="utf8", errors='ignore') as f:
            text = f.read()
            fn = "Report"

    except:
        with open("Bericht.html", encoding="utf8", errors='ignore') as f:
            text = f.read()
            fn = "Bericht"

    finally:

        c1 = text.replace('<div class="padding2_8','<split>') 
        c2 = c1.replace('ytes)</span><br /></div></div></span></div></div></div></td>','<split>')
        new = c2.split('<split>')

        i=0
        for e in new:
            if e[0] == ' ':
                del new[i]
            i = i+1
        newhtml = ''.join(new)

        file = open(""+ fn +"-kurz.html", "w")
        file.write(f"{newhtml}")
        file.close
        print("***|||***    "+ fn +".html gefunden.     ***|||***\n")
        print("***|||***  Ausgabe: "+ fn +"-kurz.html   ***|||***\n")


except:
    print("Datei: \"Report.html\" oder \"Bericht.html\" nicht gefunden. \nBitte verschieben sie das Programm in den HTML-Report Ordner.")