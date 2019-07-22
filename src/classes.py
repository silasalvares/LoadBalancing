import copy
from decimal import Decimal
from src.utils import generate_id

class User():

    def __init__(self):
        self.id = generate_id()
        self.task_count = 0

    def __eq__(self, other):
        return self.id == other.id

class Server():

    def __init__(self, umax=2):
        self.id = generate_id()
        self.umax = umax
        self.users = []
    
    def connect_user(self, user):
        self.users.append(user)

    def process(self):
        user_list = copy.copy(self.users)
        for user in user_list:
            user.task_count += 1
            if (user.task_count >= 4):
                self.users.remove(user)
            
class Handler():

    def __init__(self, server_cost=Decimal(1), umax=2):
        self.servers = []
        self.allocations = []
        self.clock = 0
        self.server_cost = server_cost
        self.total_cost = Decimal(0)
        self.umax = umax

    def handle_tick(self, new_users):
        for i in range(0, new_users):
            server = self._select_server()          
            user = User()
            server.connect_user(user)
            self.allocations.append({'server': server.id, 'user': user.id})            
        
        self._process()

    def _process(self):
        servers = copy.copy(self.servers)
        for server in servers:
            server.process()
            self.total_cost += self.server_cost
            if (len(server.users) == 0):
                self.servers.remove(server)

        self._realocate()    
        self.clock += 1 

    def _realocate(self):
        servers = copy.copy(self.servers)
        underused_servers = [
            s for s in servers
            if len(s.users) < self.umax
        ]
        for server in servers:
            underused_servers = [
                s for s in 
            ]
      

    def _select_server(self):
        available_servers = [s for s in self.servers if len(s.users) < s.umax]
        return available_servers[0] if len(available_servers) > 0 else self._create_new_server()

    def _create_new_server(self):
        server = Server(umax=self.umax)
        self.servers.append(server)
        return server

    