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

    def summary(self):
        '''
        returns summary of a blog
        '''
        return self.body[:100]+"..."

    def pub_date_pretty(self):
        '''
        Customization of date as per a specified format
        '''
        return self.pub_date.strftime('%b %e %Y')

    def __str__(self):
        '''
        string repr of objects
        '''
        return self.title



# create a blog model

# add blog app to settings
# create a migration
# migrate
# add to admin