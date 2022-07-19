from django.db import models

class Transfer(models.Model):
    
    player_name = models.CharField(max_length=255)
    player_image = models.ImageField(upload_to="media/")
    from_team = models.CharField(max_length=255)
    to_team = models.CharField(max_length=255)
    info = models.TextField()
    transfer_date = models.DateTimeField()
    
    
    def __str__(self):
        return f"{self.player_name} from {self.from_team} to {self.to_team}"
    
