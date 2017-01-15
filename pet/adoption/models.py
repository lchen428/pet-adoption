from django.db import models


class Owner(models.Model):
    name = models.CharField(max_length=255)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()

    def __unicode__(self):
        return self.name

class Ad(models.Model):
    TYPE_OF_PET_CHOICES = (
        ('CAT', 'cat'),
        ('DOG', 'dog'),
        ('FISH', 'fish'),
        ('BIRD', 'bird'),
    )

    GENDER_CHOICES = (
        ('N', 'Not Applicable'),
        ('F', 'Female'),
        ('M', 'Male'),
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    type_of_pet = models.CharField(
        max_length=50,
        choices=TYPE_OF_PET_CHOICES
    )
    birth_date = models.DateField()
    neutered = models.BooleanField(default=False)
    gender = models.CharField(
        max_length=1,
        choices=GENDER_CHOICES,
        default='Not Applicable'
    )
    owner_id = models.ForeignKey(Owner, related_name='ads', on_delete=models.CASCADE)

    def __unicode__(self):
        return self.title
