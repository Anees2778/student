from django.db import models

class Student(models.Model):
    address_choice=[('l','Lucknow'),('p','Prayagraj'),('k','Kanpur'),]
    firstName=models.CharField(max_length=30)
    lastName=models.CharField(max_length=30)
    testScore=models.FloatField(null=False)
    age=models.IntegerField(null=True)
    address=models.CharField(max_length=30,choices=address_choice,null=True)
    weight=models.FloatField(null=True)
    
    def __str__(self):
        return self.firstName
    
