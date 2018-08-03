from django.db import models
import json
#https://codeburst.io/create-a-django-api-in-under-20-minutes-2a082a60f6f3
# Create your models here.

class User(models.Model):
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=200)
    subscriptions = models.CharField(max_length=5000, default='{"Subscriptions" :[]}')
    created_at = models.DateTimeField(auto_now_add=True)

    def add_subscription(self,subscription):
        arr = json.loads(self.subscriptions)
        arr['Subscriptions'].append(subscription)
        self.subscriptions = json.dumps(arr)
        self.save()
        
    
    def __str__(self):
        return self.username + "\n    " +str(self.subscriptions)

    def get_subscriptions(self):
        return json.loads(self.subscriptions)['Subscriptions']#python array
