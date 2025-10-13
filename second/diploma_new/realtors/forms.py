from django.forms import ModelForm
from .models import Cottage
from django import forms

class CottageForm(ModelForm):
    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #
    #     for field in self.fields.values():
    #         field.widget.attrs.update({'class': 'input'})

    class Meta():
        model = Cottage
        fields = ['rlt', 'village', 'adress', 'land_area', 'house_area', 'floors', 'walls', 'bedrooms', 'web_site', 'price']
        labels = {
            'rlt': 'Риэлтор',
            'village': 'Поселок',
            'adress': 'Адрес',
            'land_area': 'Площадь участка (сот)',
            'house_area': 'Площадь дома',
            'floors': 'Этажность',
            'walls': 'Материал стен',
            'bedrooms': 'Количество спален',
            'web_site': 'веб-сайт',
            'price': 'Цена'
        }

        # widgets = {'rlt': forms.CheckboxSelectMultiple()}
