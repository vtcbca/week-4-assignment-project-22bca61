import sqlite3
import datetime
con=sqlite3.connect("contact_management_system.db")
cur = con.cursor()
cur.execute("""create table if not exists contact
               ( c_id int primary key,
                 f_name text,
                 l_name text,
                 contact number,
                 email text,
                 city text
                 check ( email like '%_@_%._%')
                );""")
#<sqlite3.Cursor at 0x16e6e53fcc0>
cur.execute("""create table if not exists details_log
                (
                    f_name text,
                    l_name text,
                    new_contact number,
                    old_contact number,
                    datetime text,
                    operation text     
                )""")
#<sqlite3.Cursor at 0x16e6e53fcc0>
cur.execute("""create trigger if not exists insertdata
               after insert on contact
               begin
                   insert into details_log
                   values(new.f_name,new.l_name,new.contact,'NULL',datetime('now'),'insert');
               end;
                   """)
#<sqlite3.Cursor at 0x16e6e53fcc0>
cur.execute("""create trigger if not exists deletedata
               after delete on contact
               begin
                   insert into details_log
                   values(old.f_name,old.l_name,'NULL',old.contact,datetime('now'),'delete');
               end;
                   """)
#<sqlite3.Cursor at 0x16e6e53fcc0>
cur.execute("""create trigger if not exists updatedata
               after update on contact
               begin
                   insert into details_log
                   values(new.f_name,new.l_name,new.contact,old.contact,datetime('now'),'update');
               end;
                   """)
#<sqlite3.Cursor at 0x16e6e53fcc0>
def insertrecord():
    cur=con.cursor()
    c_id=int(input("Enter contact id:"))
    f_name=input("Enter the first name:")
    l_name=input("Enter the last name:")
    contact=int(input("Enter the contact number:"))
    email=input("Enter the email:")
    city=input("Enter the city:")
    l=[cid,f_name,l_name,contact,email,city]
    cur.execute("insert into contact values(?,?,?,?,?,?);",l)
    print("Sucessfully row insert.");
    con.commit()
def updateContacts():
    cur=con.cursor()
    name_search=input("\n\nEnter their First name: ")
    new_contact=input("Enter New Contact No :")
    cur.execute(f"update CONTACT set contact='{new_contact}' where f_name='{name_search}'")
    print("Contact updated successfully.\n")
    con.commit()
def deleteContacts():
    cur=con.cursor()
    name_search=input("\n\nEnter their First Name: ")
    cur.execute(f"delete from CONTACT where f_name='{name_search}'")
    print("Contact deleted successfully.\n")
    con.commit()
def searchContacts():
    cur=con.cursor()
    name_search=input("\n\nEnter their First Name: ")
    cur.execute(f"select * from CONTACT where f_name='{name_search}'")
    records=cur.fetchall()
    for rows in records:
        print('{}\t{}\t{}\t{}\t{}'.format(rows[0],rows[1],rows[2],rows[3],rows[4]))      
    con.commit()
choice=1
while choice!=0:
    print('\n----------------------------------------------------------')
    print('1- Insert contacts')
    print('2- Update contacts')
    print('3- Delete contacts')
    print('4- Search contacts')
    print('0- Exit the program')
    choice=int(input('\nEnter your choice: '))
    if choice==1:
        insertrecord()      
    elif choice==2:
        updateContacts()    
    elif choice==3:
        deleteContacts()   
    elif choice==4:
         searchContacts() 
