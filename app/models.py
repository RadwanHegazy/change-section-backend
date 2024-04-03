from django.db import models
from uuid import uuid4



LEVEL_CHOICES = (
    ('1','1'),
    ('2','2'),
    ('3','3'),
    ('4','4'),
)

class Post (models.Model) :
    id = models.UUIDField(primary_key=True,db_index=True,editable=False,default=uuid4)
    student_name = models.CharField(max_length=255)
    from_section = models.PositiveIntegerField()
    to_section = models.PositiveIntegerField()
    student_collage_id = models.BigIntegerField()
    posted_at = models.DateTimeField(auto_now_add=True)
    telegram = models.URLField()
    whatsapp = models.URLField(null=True,blank=True)
    level = models.CharField(choices=LEVEL_CHOICES,max_length=1)


    def __str__(self) -> str:
        return self.student_name
