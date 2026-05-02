import unittest
from todo_list import add_task_logic, remove_task_logic


class TestTodoApp(unittest.TestCase):

    #Add single task
    def test_add_task(self):
        tasks = []
        add_task_logic(tasks, "Study Python")
        self.assertIn("Study Python", tasks)

    #Add multiple tasks
    def test_add_multiple_tasks(self):
        tasks = []
        add_task_logic(tasks, "Task 1")
        add_task_logic(tasks, "Task 2")
        self.assertEqual(len(tasks), 2)

    #Remove task
    def test_remove_task(self):
        tasks = ["Task 1", "Task 2"]
        removed = remove_task_logic(tasks, 0)
        self.assertEqual(removed, "Task 1")

    #Task actually removed
    def test_task_removed_from_list(self):
        tasks = ["Task 1", "Task 2"]
        remove_task_logic(tasks, 0)
        self.assertNotIn("Task 1", tasks)

    #Remove last task
    def test_remove_last_task(self):
        tasks = ["Only Task"]
        removed = remove_task_logic(tasks, 0)
        self.assertEqual(removed, "Only Task")
        self.assertEqual(len(tasks), 0)

    #Remove invalid index (too big)
    def test_remove_invalid_index_high(self):
        tasks = ["Task 1"]
        removed = remove_task_logic(tasks, 5)
        self.assertIsNone(removed)

    #Remove invalid index (negative)
    def test_remove_invalid_index_negative(self):
        tasks = ["Task 1"]
        removed = remove_task_logic(tasks, -1)
        self.assertIsNone(removed)

    #Tasks list not empty after add
    def test_not_empty_after_add(self):
        tasks = []
        add_task_logic(tasks, "New Task")
        self.assertTrue(tasks)

    #Tasks list shrinks after remove
    def test_list_size_decreases(self):
        tasks = ["Task 1", "Task 2"]
        remove_task_logic(tasks, 0)
        self.assertEqual(len(tasks), 1)

    #Add empty string task
    def test_add_empty_task(self):
        tasks = []
        add_task_logic(tasks, "")
        self.assertIn("", tasks)

    #Remove from empty list
    def test_remove_from_empty_list(self):
        tasks = []
        removed = remove_task_logic(tasks, 0)
        self.assertIsNone(removed)

    #Order maintained after add
    def test_task_order(self):
        tasks = []
        add_task_logic(tasks, "First")
        add_task_logic(tasks, "Second")
        self.assertEqual(tasks[0], "First")
        self.assertEqual(tasks[1], "Second")


if __name__ == "__main__":
    unittest.main()