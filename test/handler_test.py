import pytest
import itertools
from decimal import Decimal
from src.classes import Handler

@pytest.fixture
def handler():
   return Handler()

def test_when_handler_created_then_variables_are_initialized(handler):
   assert len(handler.servers) == 0
   assert handler.total_cost == 0

def test_when_new_user_and_no_servers_then_server_is_created(handler):
   handler.handle_tick(1)
   assert len(handler.servers) == 1
   handler.handle_tick(1)
   assert len(handler.servers) == 1

def test_when_tick_with_no_users_then_no_server_is_created(handler):
   handler.handle_tick(0)
   assert len(handler.servers) == 0

def test_when_tick_then_all_users_are_allocated(handler):
   handler.handle_tick(4)
   assert len(handler.allocations) == 4
   for allocation in handler.allocations:
        assert isinstance(allocation.get('server', None), str)

def test_when_all_servers_full_then_new_server_is_created(handler):
   handler.handle_tick(2)    
   assert len(handler.servers) == 1
   handler.handle_tick(1)    
   assert len(handler.servers) == 2
   
def test_when_tick_then_clock_is_incremented(handler):
   handler.handle_tick(1)
   assert handler.clock == 1
   handler.handle_tick(1)
   assert handler.clock == 2
   handler.handle_tick(1)
   assert handler.clock == 3

def test_when_all_tasks_completed_then_no_users_left(handler):
   handler.handle_tick(2) #U1, U2 added
   users = [server.users for server in handler.servers]
   assert len(list(itertools.chain.from_iterable(users))) == 2
   handler.handle_tick(1) #U3 added
   users = [server.users for server in handler.servers]
   assert len(list(itertools.chain.from_iterable(users))) == 3
   handler.handle_tick(0) 
   handler.handle_tick(0) #U1, U2 disconnected 
   users = [server.users for server in handler.servers]
   assert len(list(itertools.chain.from_iterable(users))) == 1
   handler.handle_tick(0) #U3 disconnected
   users = [server.users for server in handler.servers]
   assert len(list(itertools.chain.from_iterable(users))) == 0
   
def test_when_server_empty_then_terminate_it(handler):
   assert len(handler.servers) == 0
   handler.handle_tick(2) #U1, U2 added
   assert len(handler.servers) == 1
   handler.handle_tick(0) 
   handler.handle_tick(0) 
   handler.handle_tick(0) #Server terminated
   assert len(handler.servers) == 0

def test_when_tick_then_cost_is_updated(handler):
   handler.handle_tick(2) #Server 1 started
   handler.handle_tick(1) #Server 2 started
   handler.handle_tick(0)
   handler.handle_tick(0) #Server 1 terminated
   handler.handle_tick(0) #Server 2 terminated
   assert handler.total_cost == Decimal(8)
   


