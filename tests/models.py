import pytest
from app.models import Task

class TestTaskCreation:
    def test_valid_title_creates_task(self):
        task = Task(title="Test Task")
        assert task.title == "Test Task"
        assert task.done is False
    def test_title_is_stripped_of_whitespace(self):
        pass
    def test_empty_title_raises_value_error(self):
        pass
    def test_title_over_200_chars_raises_value_error(self):
        pass

class TestTaskCompletion:
    def test_complete_sets_done_to_true(self):
        pass
    def test_to_dict_contains_all_keys(self):
        pass

Tomek 16:08
from datetime import datetime

class Task:
    def __init__(self, title: str, description: str = ""):
        if not title or not title.strip():
            raise ValueError("Tytuł zadania nie może być pusty")
        if len(title) > 200:
            raise ValueError("Tytuł nie może przekraczać 200 znaków")
        self.title = title.strip()
        self.description = description
        self.done = False
        self.created_at = datetime.utcnow()

    def complete(self):
        self.done = True

    def to_dict(self) -> dict:
        return {
            "title": self.title,
            "description": self.description,
            "done": self.done,
            "created_at": self.created_at.isoformat(),
        }