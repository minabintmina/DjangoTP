from django.db import models
from datetime import date

class Produit(models.Model):
    TYPE_CHOICES=[('fr','Frais'),('cs','Conserve'),('em','emballé')]
    libelle=models.CharField(max_length=255)
    description=models.TextField()
    prix=models.DecimalField(max_digits=10,decimal_places=3,default=0.000)
    type=models.CharField(max_length=2,choices=TYPE_CHOICES,default='em')
    Img=models.ImageField(blank=True)
    catégorie=models.ForeignKey('Categorie', on_delete=models.CASCADE,null=True)
    Fournisseur=models.ForeignKey('Fournisseur',on_delete=models.CASCADE,null=True)
    
    def __str__(self):
        return self.libelle+" "+self.description+" "+str(self.prix)


class Categorie(models.Model):
    TYPE_CHOICES=[('Al','Alimentaire'), ('Mb','Meuble'),('Sn','Sanitaire'), ('Vs','Vaisselle'),('Vt','Vêtement'),('Jx','Jouets'),('Lg','Linge de Maison'),('Bj','Bijoux'),('Dc','Décor')]
    name=models.CharField(max_length=50,choices=TYPE_CHOICES,default='Al')
    def __str__(self):
        return self.name


class Fournisseur(models.Model):
    nom=models.CharField(max_length=100)
    adresse=models.TextField()
    email=models.EmailField()
    telephone=models.CharField(max_length=8)


class ProduitNC(Produit):
    Duree_garantie=models.CharField(max_length=100)

class Commande(models.Model):
    dateCde=models.DateField(null=True,default=date.today)
    totalCde=models.DecimalField(max_digits=10,decimal_places=3)
    Produit=models.ManyToManyField('Produit')

# Create your models here.
