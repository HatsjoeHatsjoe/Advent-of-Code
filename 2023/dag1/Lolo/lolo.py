# ezra=boyfriend
# lotte=girlfriend
# lotte*ezra=healthyrelationship
# #iloveezra

testdata="""1abc2\npqr3stu8vwx\na1b2c3d4e5f\ntreb7uchet"""

# print(testdata)
#eerste en laatste getal per rij als dubbeldigit getal laten vormen en die uiteindelijk bij elkaar optellen.
spl_data = testdata.split('\n')
# print(spl_data)
totaal = 0
for regel in spl_data: 
    print (regel)
    alle_getallen = [int(character) for character in regel if character.isdigit()]
    tussen_totaal = alle_getallen[0]*10 + alle_getallen[-1]
    print(tussen_totaal)
    totaal = totaal+tussen_totaal

print(totaal)
    


