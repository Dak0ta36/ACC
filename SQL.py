import pyodbc

connection_to_db = pyodbc.connect(r'Driver={SQL Server};Server=DESKTOP-2323D7I\SQLEXPRESS;Database=NIR;Trusted_Connection=yes;')
cursor = connection_to_db.cursor()

patients=['Igor','Dmitry','Anna','Peter','Vladimir']
diagnosis=['illnes','flu','headache','cold','deafness']
def fill():
    for i in range(len(patients)):
        mydict = {'Name': patients[i], 'Diagnosis': diagnosis[i]}

        columns = ', '.join( str(x).replace('/', '_')  for x in mydict.keys())
        values = ', '.join("'" + str(x).replace('/', '_') + "'" for x in mydict.values())
        sql = "insert into %s ( %s ) values ( %s );" % ('NIRTABLE', columns, values)
        print(sql)

        cursor.execute(sql)
        cursor.commit()

fill()
connection_to_db.close()

