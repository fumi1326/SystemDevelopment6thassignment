class TaskManager:
    """タスク管理を行うクラス。"""
    def __init__(self):
        self.tasks = []

    def add_task(self, title: str):
        """タスクを追加する。"""
        if not title:
            raise ValueError("Title cannot be empty")
        self.tasks.append({"title": title, "completed": False})
        return True

    def get_tasks(self):
        """全タスクを取得する。"""
        return self.tasks