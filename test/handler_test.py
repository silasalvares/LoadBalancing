import pytest
from src.handler import Handler
from src.utils import StateEnum

@pytest.fixture
def handler():
    return Handler()

def test_when_handler_created_server_list_is_empty(handler):
    assert len(handler.servers) == 0

def test_when_tick_with_no_users_then_no_server_created(handler):
    server_count =  len(handler.servers)
    handler.handle_tick(0)
    assert len(handler.servers) == server_count

def test_when_tick_with_users_then_servers_are_created(handler):
    handler.handle_tick(1)
    assert len(handler.servers) > 0

def test_when_tick_then_users_are_allocated(handler):
    allocations = handler.handle_tick(2)
    assert len(allocations) > 0
    for allocation in allocations:
        assert allocation.get('server_id', None) is not None

def test_when_server_full_then_new_server_is_created(handler):
    handler.handle_tick(3)
    assert len(handler.servers) == 2
    handler.handle_tick(4)
    assert len(handler.servers) == 4
    handler.handle_tick(2)
    assert len(handler.servers) == 5

def test_when_user_allocated_then_task_is_started(handler):
    assert handler.



    