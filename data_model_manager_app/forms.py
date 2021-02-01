from . import models
from django import forms


class DataCategoryForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DataCategoryForm, self).__init__(*args, **kwargs)
        # add a "form-control" class to each form input
        # for enabling bootstrap
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })

    class Meta:
        model = models.DataCategory
        fields = "__all__"


class DataForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DataForm, self).__init__(*args, **kwargs)
        has_min_zero = [
            'size_on_disk',
            'number_of_images',
            'number_of_classes',
            'iqa_0',
            'iqa_1',
            'iqa_2',
            'iqa_3',
            'iqa_4',
            'shape_0',
            'shape_1',
            'shape_2',
            'shape_3',
            'shape_4',
        ]
        for name in self.fields.keys():
            if name in has_min_zero:
                self.fields[name].widget.attrs['min'] = 0
                self.fields[name].widget.attrs.update({
                    'class': 'form-control',
                })
            else:
                self.fields[name].widget.attrs.update({
                    'class': 'form-control',
                })

    class Meta:
        model = models.Data
        fields = [
            'name',
            'data_category',
            'size_on_disk',
            'directory_of_data',
            'number_of_images',
            'number_of_classes',
            'iqa_0',
            'iqa_1',
            'iqa_2',
            'iqa_3',
            'iqa_4',
            'shape_0',
            'shape_1',
            'shape_2',
            'shape_3',
            'shape_4',
            'analyzed',
            'best_result',
            'best_analyzed_model',
            'data_avatar',
        ]


class DataFilterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DataFilterForm, self).__init__(*args, **kwargs)
        # add a "form-control" class to each form input
        # for enabling bootstrap
        for name in self.fields.keys():
            self.fields[name].required = False
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })

    class Meta:
        model = models.Data
        fields = [
            'name',
            'data_category',
            'size_on_disk',
            'directory_of_data',
            'number_of_images',
            'number_of_classes',
            'analyzed',
            'best_result',
            'best_analyzed_model',
            'data_owner',
        ]


class AiModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AiModelForm, self).__init__(*args, **kwargs)
        # add a "form-control" class to each form input
        # for enabling bootstrap
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })

    class Meta:
        model = models.AiModel
        fields = ["model_name",]


class SearchAiModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SearchAiModelForm, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control'
            })
            self.fields[name].required = False

    class Meta:
        model = models.AiModel
        fields = "__all__"


class SearchModelTrainData(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SearchModelTrainData, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control'
            })
            self.fields[name].required = False

    class Meta:
        model = models.ModelTrainData
        fields = "__all__"


class AddModelTrainData(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddModelTrainData, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control'
            })

    class Meta:
        model = models.ModelTrainData
        fields = "__all__"