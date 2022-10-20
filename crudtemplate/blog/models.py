from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField( auto_now_add = True)

    class Meta:  
        db_table = "members_posts"