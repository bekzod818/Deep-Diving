from django.db import models


class TaskStatus(models.IntegerChoices):
    TODO = 1
    IN_PROGRESS = 2
    COMPLETED = 3


class Task(models.Model):
    name = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=TaskStatus.choices)

    def __str__(self):
        return self.name


class InProgressTask(Task):
    class Meta:
        proxy = True

    class Manager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status=TaskStatus.IN_PROGRESS)

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.status = TaskStatus.IN_PROGRESS
        super().save(*args, **kwargs)

    objects = Manager()


class ToDoTask(Task):
    class Meta:
        proxy = True
        ordering = ("-created_at",)

    class Manager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status=TaskStatus.TODO)

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.status = TaskStatus.TODO
        super().save(*args, **kwargs)

    objects = Manager()


class CompletedTask(Task):
    class Meta:
        proxy = True
        ordering = ("-created_at",)

    class Manager(models.Manager):
        def get_queryset(self):
            return super().get_queryset().filter(status=TaskStatus.COMPLETED)

    def save(self, *args, **kwargs):
        if self._state.adding:
            self.status = TaskStatus.COMPLETED
        super().save(*args, **kwargs)

    objects = Manager()
