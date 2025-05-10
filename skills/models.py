from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Tree(models.Model):
    name = models.CharField(max_length=255, default='NAME')
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    root_node = models.OneToOneField('Node', on_delete=models.CASCADE, null=True,related_name='parent_tree')
    structure = models.JSONField(default=dict)
    skill_points = models.PositiveIntegerField(default = 5)
    def get_structure(self):
        return self.root_node.get_c()




class Node(models.Model):
    name = models.CharField(max_length=255, default='NAME_NODE')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    tree = models.ForeignKey(Tree,on_delete=models.CASCADE,related_name='node')
    id = models.AutoField(primary_key=True)
    root_node = models.BooleanField(default=False)
    activated = models.BooleanField(default=False)
    def get_c(self):
        self.c = {"name":"","children":[],"id":0}
        self.c["name"] = self.name
        for node in Node.objects.all():
            if node.parent == self:
                self.c["children"].append(node.get_c())
        self.c['id'] = self.id
        self.c['activated'] = self.activated
        self.c['root_node'] = self.root_node

        return self.c