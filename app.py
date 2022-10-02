import dbcreds
import mariadb
import dbhelpers as db


def login():
   username = input('Username: ')
   password = input('Password: ')
   cursor =  db.connect_db()
   results =  db.execute_statement(cursor, 'CALL get_username_and_password(?,?)', [username, password])
   db.close_connection(cursor)
   if(len(results) == 1):
    return results[0][2]
   elif(len(results) == 0):
    return None 

def create_post(client_id):
    #in this function I keep getting the Programming Error cursor doesnt have a result set 
    title = input('Post Title: ')
    content = input('Post Content: ')
    cursor =  db.connect_db()
    results =  db.execute_statement(cursor, 'CALL create_post(?,?,?)', [client_id ,title, content])
    db.close_connection(cursor)
    return results

def get_posts():
    cursor =  db.connect_db()
    results =  db.execute_statement(cursor, 'CALL get_posts()')
    db.close_connection(cursor)
    for post in results:
        print(post)
   

def application():
   username = input('Username: ')
   password = input('Password: ')
   cursor =  db.connect_db()
   results =  db.execute_statement(cursor, 'CALL get_username_and_password(?,?)', [username, password])
   db.close_connection(cursor)
   print('Create new post: 1')
   print('View all posts:2')
   print('Quit: 3')
   client_id = login()
   user_selection = input('Please choose an option: ')
   if(user_selection == '1'):
        create_post(client_id)
   elif(user_selection == '2'):
        get_posts()
   elif(user_selection == '3'):
        return results   
   



# client_id is equal to whatever the function returns

application()
# create_post(client_id)
# get_posts()


    
