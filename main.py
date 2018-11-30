import cassandra.cluster import Cluster
  
def main():
    cluster = Cluster()
    NodeIPFile = open("NodeExIP.txt")
    NodeIP = str(NodeIPFile.read())
    NodeIP = NodeIP.split()
    cluster = Cluster([NodeIP[0], NodeIP[1], NodeIP[2], load_balancing_policy=DCAwareRoundRobinPolicy, port=2880)
main()
