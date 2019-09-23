from django.db import models


# Create your models here.
# title
# publication date
# body
# image
class Blog(models.Model):
    image = models.ImageField(upload_to='images/')
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()



# create a blog model

# add blog app to settings
# create a migration
# migrate
# add to admin