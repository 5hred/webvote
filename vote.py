import sqlite3 as sq3
import jason
from sq3 import Error
"""create the database and interact with it"""
#make the database and connection
def make_db(database):
    try:
        #connection object
        connection = sq3.connect(database)
        #get the dict from sqlite query
        connection.row_factory = lambda c, r: dict(zip(col[0] for col in\
        c.description], r))
        #return result
        return connection
    except Error as e:
        print(e)
#create a table for the vote
def make_table(conn):
    sql = '''
        CREATE TABLE IF NOT EXISTS choice (
            id integer PRIMARY KEY,
            name varchar(255) NOT NULL,
            votes integer NOT NULL Default 0
        );
        '''
    conn.execute(sql)
#create a ballet point to vote on
def make_ballet_item(conn, ballet):
    sql = ''' INSERT INTO ballet(name)
                VALUES(?) '''
    conn.execute(sql, ballet)
#create a vote for the ballet point
def set_vote(conn, ballet):
    sql = ''' UPDATE ballet
                set vote = vote+1
                WHERE name = ?
        '''
    conn.execute(sql, ballet)
#remove a vote for the ballet point
def pop_vote(conn, ballet):
    sql = ''' UPDATE ballet
                set vote = vote-1
                WHERE name = ?
            '''
    conn.execute(sql, ballet)
#get the results from the votes
def get_votes(conn,name):
    sql = '''
            SELECT * FROM ballet
        '''
    conn.execute(sql)
    rows = conn.fetchall()
    rows.append({'name' : name})
    return jason.dump(rows)
#create an object for each person
class Person:
    def __init__(voter, name, vote):
        voter.name = name
        voter.vote = vote
        registered = FALSE
        castvote = ""
    #check to see if they can vote
    def check_registered():
    #cast one vote
    def cast_vote(vote):
        if voted
        pop_vote(conn, )
        set_vote(conn, vote)
#create a class for each vote
class Ballet:
    def __init__(ballet, name, args):
        ballet.name = name
        ballet.items = args
        voted = FALSE
        vote = NULL
        database = "./votedatabase.db"
        conn = make_db(ballet.name)
    def build_ballet(args):
        for x in args : make_table(conn, x)
#not using it as stand alone no need for main()
def main():
if __name__ == '__main__':
    print("Run as a module")
else:
    print("Ruing as a module")
