from django.db import models

# Create your models here.
CATEGORY_CHOICES=(
    ('CR','Curd'),
     ('ML','Milk'),
      ('LS','Lassi'),
       ('MS','Milkshake'),
       ('GH','Ghee'),
        ('PA','Paneer'),
        ('CH','Cheese'),
        ('IC','Ice cream'),
)

class Product(models.Model):
    title =models.CharField(max_length=100)
    selling_price=models.FloatField()
    discounted_price= models.FloatField()
    description = models.TextField()
    comopsition=models.TextField(default="")
    prodapp =models.TextField(default="")
    category=models.CharField(choices=CATEGORY_CHOICES, max_length=2)
    product_image = models.ImageField(upload_to='product/')
    def __str__(self):
        return self.title