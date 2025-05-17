from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Tree(models.Model):

    def __str__(self):
        return self.name
    
    name = models.CharField(max_length=45, default='NAME')
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    root_node = models.OneToOneField('Node', on_delete=models.CASCADE, null=True,related_name='parent_tree')
    structure = models.JSONField(default=dict)
    exp = models.PositiveBigIntegerField(default = 0)
    skill_points = models.PositiveBigIntegerField(default = 0)


    def get_structure(self):
        return self.root_node.get_c()




class Node(models.Model):
    name = models.CharField(max_length=45, default='NAME_NODE')
    parent = models.ForeignKey('self', on_delete=models.CASCADE, null=True, blank=True, related_name='children')
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    tree = models.ForeignKey(Tree,on_delete=models.CASCADE,related_name='node')
    id = models.AutoField(primary_key=True)
    root_node = models.BooleanField(default=False)
    activated = models.BooleanField(default=False)
    time_required = models.PositiveBigIntegerField(default = 5)
    difficulty = models.PositiveSmallIntegerField(default=1)
    skill_points_required = models.PositiveBigIntegerField(default=60)
    def save(self, *args, **kwargs):
        self.skill_points_required = self.time_required * self.difficulty
        return super().save(*args, **kwargs)
    
    def get_c(self):
        self.c = {"name":"","id":0,"children":[]}
        self.c["name"] = self.name
        self.c['id'] = self.id
        for node in Node.objects.all():
            if node.parent == self:
                self.c["children"].append(node.get_c())
        self.c['activated'] = self.activated
        self.c['root_node'] = self.root_node
        self.c['skill_points_required'] = self.skill_points_required

        return self.c