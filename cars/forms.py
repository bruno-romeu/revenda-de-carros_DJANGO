from django import forms
from cars.models import Car

#class que tem na hierarquia o ModelForm já conversa automaticamente com os modelos já criados que são informados.
class CarModelForm(forms.ModelForm):
    class Meta:
        #escolher o modelo já criado que deseja anexar.
        model = Car
        #selecionando quais "chaves" do modelo vamos usar para salvar.
        fields = '__all__'

        #validação de dados
    def clean_value(self):
        #capturar o valor que o usuário informou para fazer a validação de dados.
        value = self.cleaned_data.get('value')
        if value < 20000:
            self.add_error('value', 'Valor mínimo do carro deve ser de R$20.000,00')
        return value
    
    def clean_factory_year(self):
        factory_year = self.cleaned_data.get('factory_year')
        if factory_year < 1975:
            self.add_error('factory_year', 'Não é possível cadastrar carros fabricados antes de 1975.')
        return factory_year