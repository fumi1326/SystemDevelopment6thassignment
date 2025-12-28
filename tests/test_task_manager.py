import pytest
from src.task_manager import TaskManager

def test_add_task():
    """タスク追加をテスト。"""
    tm = TaskManager()
    result = tm.add_task("Complete Report")
    assert len(tm.get_tasks()) == 1
    assert "Complete Report" in tm.get_tasks()[0]

def test_add_empty_task():
    """空のタスク追加時にエラーが発生するかをテスト。"""
    tm = TaskManager()
    with pytest.raises(ValueError):
        tm.add_task("")

def test_get_tasks_initially_empty():
    """初期状態でリストが空であることをテスト。"""
    tm = TaskManager()
    assert tm.get_tasks() == []