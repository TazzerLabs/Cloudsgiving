import cassandra.cluster import Cluster
from cassandra.policies import DCAwareRoundRobinPolicy

def main():
    NodeIPFile = open("NodeExIP.txt")
    NodeIP = str(NodeIPFile.read())
    NodeIP = NodeIP.split()
    cluster = Cluster([NodeIP[0], NodeIP[1], NodeIP[2], load_balancing_policy=DCAwareRoundRobinPolicy, port=80)
    keyspace = "CREATE KEYSPACE IF NOT EXISTS minibank WITH REPLICATION = {'class': 'SimpleStrategy', 'replication_factor' : 3}"
    session = cluster.connect(keyspace)
    #This should be useless stuff
    #session.set_keyspace('users')
    #session.execute('USE users')
    
    
    #UUID takes a uuid.UUID datatype
    #Username, username, password takes a string
    #subscription, content takes a list
    session.execute('CREATE TABLE Users (userID UUID PRIMARY KEY, username text, email text, password text, content list, subscription list)')
    session.execute('INSERT INTO Users (userID, username, email, password, content, subscription)
                     VALUES(%s, %s, %s, %s, %s, %s)',
                     (uuid.uuid1(), username, email, password, contentL, subscriptionL)
                     )
    rows = session.execute("SELECT userID, username, email from users")
    for row in rows:
        print row[0], row[1], row[2]


main()
