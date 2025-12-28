import pytest
from src.task_manager import TaskManager

def test_add_task():
    tm = TaskManager()
    assert tm.add_task("Test Task") is True
    assert len(tm.get_tasks()) == 1

def test_add_task_error():
    tm = TaskManager()
    with pytest.raises(ValueError):
        tm.add_task("")