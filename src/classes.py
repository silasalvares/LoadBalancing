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

    def __init__(self, ttask=4, umax=2):
        self.id = generate_id()
        self.ttask = ttask
        self.umax = umax
        self.users = []
    
    def connect_user(self, user):
        self.users.append(user)

    def process(self):
        user_list = copy.copy(self.users)
        for user in user_list:
            user.task_count += 1
            if (user.task_count >= self.ttask):
                self.users.remove(user)

    def is_full(self):
        return len(self.users) == self.umax

    def is_empty(self):
        return len(self.users) == 0

    def remove_user(self):
        return self.users.pop(0)

class Handler():

    def __init__(self, server_cost=Decimal(1), ttask=4, umax=2):
        self.servers = []
        self.allocations = []
        self.clock = 0
        self.server_cost = server_cost
        self.total_cost = Decimal(0)
        self.ttask = ttask
        self.umax = umax
        self.completed = False

    def handle_tick(self, new_users):
        if new_users is not None:
            for i in range(0, new_users):
                server = self._select_server()          
                user = User()
                server.connect_user(user)
                self.allocations.append({'server': server.id, 'user': user.id, 'ticks': 0})            
        
        self._process()
        self.completed = (len(self.servers) == 0 and new_users == None)

    def _process(self):
        servers = copy.copy(self.servers)
        self.total_cost += (self.server_cost * len(self.servers))
        print(','.join([str(len(s.users)) for s in self.servers]))
        for server in servers:
               
            server.process()
            if (len(server.users) == 0):
                self.servers.remove(server)
        
        self.clock += 1 

    def _select_server(self):
        available_servers = [s for s in self.servers if len(s.users) < s.umax]
        return available_servers[0] if len(available_servers) > 0 else self._create_new_server()

    def _create_new_server(self):
        server = Server(ttask=self.ttask, umax=self.umax)
        self.servers.append(server)
        return server

    def get_total_cost(self):
        return '$' + str(self.total_cost)