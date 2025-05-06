from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Tree(models.Model):
    name = models.CharField(max_length=255, default='NAME')
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)


class Node(models.Model):
    name = models.CharField(max_length=255, default='NAME_NODE')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    tree = models.ForeignKey(Tree,on_delete=models.CASCADE,related_name='node')
    id = models.AutoField(primary_key=True)
    
    def get_c(self):
        self.c = {}
        self.c[self.name] = {}
        for node in Node.objects.all():
            if node.parent == self:
                self.c[self.name].update(node.get_c())
        self.c[self.name].update({'id':self.id})

        return self.c