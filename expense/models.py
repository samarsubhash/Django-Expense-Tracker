from django.db import models

# Create your models here.
class expensedb(models.Model):

  CATEGORY_CHOICES = [
        ('FOOD', 'Food'),
        ('TRAVEL', 'Travel'),
        ('BILLS', 'Bills'),
        ('GYM', 'Gym'),
        ('ENTERTAINMENT', 'Entertainment'),
    ]
  title = models.CharField(max_length=100)
  amount = models.DecimalField(max_digits=10,decimal_places=2)
  category = models.CharField(max_length=20,choices=CATEGORY_CHOICES)

  def __str__(self):
    return self.title