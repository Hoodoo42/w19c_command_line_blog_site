from http import client
from urllib import response
import dbcreds
import mariadb
import dbhelpers as db


def login():
    # function prompts user to enter username and password
   username = input('Username: ')
   password = input('Password: ')
#    connects to db and saves the results of user input used for paramaters of the db procedure
   cursor =  db.connect_db()
   results =  db.execute_statement(cursor, 'CALL get_username_and_password(?,?)', [username, password])
#    close db
   db.close_connection(cursor)
#    checks if results has gathered one row from db, if yes it returns the user id from that row
# if no rows were saved in results, return undefined/None
   if(len(results) == 1):
    return results[0][2]
   elif(len(results) == 0):
    return None 

  #(in this function I keep getting the Programming Error cursor doesnt have a result set)
# this function will allow a user to create a post by taking their previously returned user id as an argument.
def create_post(client_id):
#   prompt user to input a title and content for their new post
    title = input('Post Title: ')
    content = input('Post Content: ')
    # connect to db
    cursor =  db.connect_db()
    # save the results of user input used for paramaters of the db procedure
    results =  db.execute_statement(cursor, 'CALL create_post(?,?,?)', [client_id ,title, content])
    # close db
    db.close_connection(cursor)
    # return the reuslts of the saved user input matching the parameters of the db procedure
    return results


# this function allows user to see all posts created.
def get_posts():
    cursor =  db.connect_db()
    results =  db.execute_statement(cursor, 'CALL get_posts()')
    db.close_connection(cursor)
    for post in results:
        print(post)

   
def login_infinitely(client_id):
        login()
        while(True): 
            print('create a new post? Select 1')
            print('read all posts? Select 2')
            print('quit? Select 3')

            response = input('What would you like to do? ')

            if(response == '1'):
                create_post(client_id)
            elif(response == '2'):
                get_posts()
            elif(response == '3'):
                return        
           


client_id = login()
login_infinitely(client_id)

# ### client_id is equal to whatever the function returns


# create_post(client_id)
# get_posts()


    
