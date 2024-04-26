from django.db import models
from django.urls import reverse

class Toy(models.Model):
    name = models.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('toys_detail', kwargs={'pk': self.id})

class Finch(models.Model):
    breed = models.CharField(max_length=100)
    toys = models.ManyToManyField(Toy)

    def __str__(self):
        return self.breed
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'finch_id':self.id}) #details is the name of the path. 
    
class Feeding(models.Model):
    MEALS = (
        ('B', 'Breakfast'),
        ('L', 'Lunch'),
        ('D', 'Dinner')
    )
    date = models.DateField('feeding date')
    meal = models.CharField(max_length=1, choices=MEALS, default = 'B')
    finch = models.ForeignKey(Finch, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.get_meal_display()} on {self.date}'
    
    class Meta:
        ordering = ('-date',)