from src.utils import generate_id, StateEnum

class User():

    def __init__(self):
        self.id = generate_id()


class Server():

    def __init__(self, umax=2):
        self.umax = umax
        self.id = generate_id()
        self.users = []
        
    '''def is_full(self):
        return len(self.users) >= self.umax'''
        

class Handler():

    def __init__(self):
        self.servers = []
        self.allocations = []

    def handle_tick(self, new_users):
        for i in range(0, new_users):
            server = self._check_server_balance()
            user = User()
            server.users.append(user)
            self.allocations.append({'server_id': server.id, 'user_id': user.id})

        return self.allocations

    def _check_server_balance(self):
        available_servers = [ s for s in self.servers if not s.is_full() ]
        if len(available_servers) > 0:
            return available_servers[0]
        else:
            server = Server()
            self.servers.append(server)
            return server

    def _get_server(self, server_id):
        return self.servers.get(server_id, None)

    def _connect_client(self):
        return None    

    def _create_server(self):
        return None

    def _start_task(self):
        return None

    def _terminate_task(self):
        return None


