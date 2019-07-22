import pytest
from src.classes import Server, User

@pytest.fixture
def server():
    return Server()

def test_when_server_created_then_default_vars_are_set(server):
    assert isinstance(server.id, str)
    assert server.umax > 0
    assert len(server.users) == 0
    
def test_when_connect_user_then_user_list_is_updated(server):
    server.connect_user('user')
    assert len(server.users) == 1

def test_when_process_then_all_users_tasks_are_incremented(server):
    server.connect_user(User())
    before = [ {'id': u.id, 'task_count': u.task_count} for u in server.users]
    assert len(before) > 0
    server.process()
    after = [ {'id': u.id, 'task_count': u.task_count} for u in server.users]
    assert len(after) > 0
    for a in after:
        b_item = next((b for b in before if b['id'] == a['id']))
        assert a['task_count'] == b_item['task_count'] + 1

def test_when_process_reaches_ttask_then_user_is_disconnected(server):
    user = User()
    server.connect_user(user)
    assert user in server.users
    for p in range(0,4):
        server.process()
    assert user not in server.users 

    