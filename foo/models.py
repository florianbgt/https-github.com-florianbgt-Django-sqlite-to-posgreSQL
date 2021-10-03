from django.db import models
from django.contrib.auth import get_user_model

class Foo(models.Model):
    foo = models.CharField(max_length=50)
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    
    def __str__(self):
        return f"{self.pk}-{self.foo}"