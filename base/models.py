from django.db import models

class userToken(models.Model):
    token = models.CharField(max_length=1000)

    def __str__(self):
        return self.token

class NotificationImage(models.Model):
    image = models.ImageField(upload_to="image", null=True)
    
    def __str__(self):
        return self.image.url

    def save(self, *args, **kwargs):
        try:
            this = NotificationImage.objects.get(id=self.id)
            if this.image != self.image:
                this.image.delete()
        except:
            pass

        super(NotificationImage,self).save(*args,**kwargs)