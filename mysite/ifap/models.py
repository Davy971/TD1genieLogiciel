from django.db import models

class Classe(models.Model):
     type_classe=  models.CharField(max_length=200)
     def __str__(self):
        return self.type_classe

class Ordre(models.Model):
     type_ordre=  models.CharField(max_length=200)
     def __str__(self):
        return self.type_ordre


class Famille(models.Model):
     type_famille=  models.CharField(max_length=200)
     def __str__(self):
        return self.type_famille

class NomScientifique(models.Model):
     type_nomscientifique=  models.CharField(max_length=200)
     def __str__(self):
        return self.type_nomscientifique

class Animal(models.Model):
      classe=  models.ForeignKey(Classe, on_delete=models.CASCADE)
      ordre=  models.ForeignKey(Ordre, on_delete=models.CASCADE)
      famille=  models.ForeignKey(Famille, on_delete=models.CASCADE)
      nomscientifique=  models.ForeignKey(NomScientifique, on_delete=models.CASCADE)


