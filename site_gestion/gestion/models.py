from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.core.validators import MaxValueValidator, MinValueValidator

# Mémo:  Pour bien initialiser la clef étrangère Article.category j'ai dans le shell fait les commandes : from gestion.models import Category | Category.objects.create(name='uncategorized') | python manage.py make migrations | python manage.py migrate
class Category(models.Model):
    name=models.CharField(max_length=150)

    def __str__(self) -> str:
        return self.name


class Article(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    title=models.CharField(max_length=50)
    description=models.TextField()
    image=models.ImageField(upload_to='media',null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    prix = models.DecimalField(max_digits=10, decimal_places=2)
    quantité=models.IntegerField(default=0,null=False,validators=[MinValueValidator(0)])

    def __str__(self):
        return self.title
    
    def get_absolute_url(self):
        return reverse("my-articles")
    
class Achat(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    panier=models.ForeignKey("Panier", on_delete=models.CASCADE,null=True)
    article=models.ForeignKey(Article,on_delete=models.CASCADE)
    quantité_achat=models.IntegerField(default=1)
    acheté=models.BooleanField(default=False)

    def __str__(self):
        chaine=self.article.title+" "+ "("+str(self.quantité_achat)+")"
        return chaine
    
class Panier(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    achats = models.ManyToManyField(Achat, related_name='paniers')
    acheté_p=models.BooleanField(default=False)
    date_achat=models.DateTimeField(blank=True,null=True)

    def __str__(self):
        return self.user.username