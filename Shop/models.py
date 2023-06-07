from django.db import models

# Create your models here.
class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    category_type = models.CharField(max_length=50, null=True, blank=True)
    
    def __str__(self):
        return f"{self.category_type}"
    
class Food(models.Model):
    food_id = models.AutoField(primary_key=True)
    food_name = models.CharField(max_length=50, null=True, blank=True)
    food_age = models.TextField(max_length=50, null = True , blank=True)
    food_desc = models.TextField(max_length=500, null=True, blank=True)
    food_des = models.TextField(max_length=500, null=True, blank=True)
    food_review = models.TextField(max_length=1000, null=True, blank=True)
    food_price = models.DecimalField(max_digits=6, decimal_places=0, null=True, blank=True) 
    food_img = models.ImageField(upload_to='food/')
    food_category = models.ForeignKey(Category, on_delete=models.CASCADE,null=True, blank=True)
    
    
    def __str__(self):
        return f'{self.food_id} - {self.food_name}'
    
class Kategoria(models.Model):
    kategoria_id = models.AutoField(primary_key=True)
    kategoria_type = models.CharField(max_length=50, null=True, blank=True)
    kategoria_img = models.ImageField(upload_to='adopt/')

    def __str__(self):
        return f"{self.kategoria_type}"
    
class Adopt(models.Model):
    adopt_id = models.AutoField(primary_key=True)
    adopt_name = models.CharField(max_length=50, null=True, blank=True)
    adopt_desc = models.TextField(max_length=500, null=True, blank=True)
    adopt_img = models.ImageField(upload_to='adopt/')
    adopt_category = models.ForeignKey(Kategoria, on_delete=models.CASCADE,null=True, blank=True)
    
    
    def __str__(self):
        return f'{self.adopt_id} - {self.adopt_name}'
    
class Contact(models.Model):
    contact_emri = models.CharField(max_length=60, null=True, blank=True)
    contact_email = models.EmailField(null=True, blank=True)
    contact_comment = models.TextField(max_length=500, null=True, blank=True)
    
    def __str__(self):
        return f'{self.contact_emri} - {self.contact_email} - {self.contact_comment}'
    
class Subscriber(models.Model):
    name = models.CharField(max_length=255)
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f'{self.name} - {self.name}'
    



    

    
    
    


    
    
    