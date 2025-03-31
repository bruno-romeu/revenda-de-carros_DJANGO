from django.db import models




class Brand(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Car(models.Model):
    #Criando os padrões para inserir no banco de dados.
    id = models.AutoField(primary_key=True)
    model = models.CharField(max_length=200)
    brand = models.ForeignKey(Brand, on_delete=models.PROTECT, related_name='car_brand')
    factory_year = models.IntegerField(blank=True, null=True)
    model_year = models.IntegerField(blank=True, null=True)
    plate = models.CharField(blank=True, null=True, max_length=20)
    value = models.FloatField(blank=True, null=True)
    photo = models.ImageField(upload_to='cars/', blank=True, null=True)
    bio = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.model
    
class CarInventory(models.Model):
    cars_count = models.IntegerField()
    cars_value = models.FloatField()
    #datetimefield é uma propriedade que faz com que o armazenamento de dados guarde a data e o horário da ação, com horas, minutos e segundos.
    created_at = models.DateTimeField(auto_now_add=True)
    #auto_now_add=True faz com que seja armazenado automaticamento a data atual da ação.

    class Meta:
        ordering = ['-created_at']
    #alteração feita para a ordenação do inventário ser decrescente, da última alteração até a primeira.

    def __str__(self):
        return f'{self.cars_count} - {self.cars_value}'
    


