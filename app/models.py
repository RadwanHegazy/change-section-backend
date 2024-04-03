from django.db import models
from uuid import uuid4
from django.dispatch import receiver
from django.db.models.signals import post_save, post_delete
from django.core.cache import cache
from django.core.exceptions import ValidationError

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
    student_collage_id = models.BigIntegerField(unique=True)
    posted_at = models.DateTimeField(auto_now_add=True)
    telegram = models.URLField()
    whatsapp = models.URLField(null=True,blank=True)
    level = models.CharField(choices=LEVEL_CHOICES,max_length=1)

    class Meta:
        ordering = ('-posted_at',)

    def clean(self) -> None:

        if "web.telegram.org/k/#@" not in str(self.telegram) :
            raise ValidationError({
                'telegram':"invalid url for telegram"
            })
        
        if "wa.me" not in str(self.whatsapp):
            raise ValidationError({
                'whatsapp' : 'invalid url for whatsapp'
            })
        

        if len(str(self.student_collage_id)) != 10 :
            raise ValidationError({
                'student_collage_id' : 'invalid student collage id'
            })

    def __str__(self) -> str:
        return self.student_name



@receiver(post_save,sender=Post)
def CahcePostsOnCreate(created,instance,**kwargs) :
    if created :
        cache.delete('posts')



receiver(post_delete,sender=Post)
def CahcePostsOnDelete(instance,**kwargs) :
    cache.delete('posts')
