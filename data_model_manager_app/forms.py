from . import models
from django import forms
from django.forms import Textarea


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
        # min value is zero in form
        has_min_zero = [
            'size_on_disk',
            'number_of_images',
            'number_of_classes',
            'brisque',
            'brightness',
            'sharpness',
            'iqa_3',
            'iqa_4',
            'mean_width',
            'mean_height',
            'shape_2',
            'shape_3',
            'shape_4',
        ]
        # required fields in form
        required_fields = [
            'name',
            'data_category',
            'size_on_disk',
            'directory_of_data',
            'number_of_images',
            'number_of_classes',
        ]
        for name in self.fields.keys():
            # add * to required fields
            if name in required_fields:
                self.fields[name].label = self.fields[name].label + " *"
            # add min zero to number fields
            if name in has_min_zero:
                self.fields[name].widget.attrs['min'] = 0
                self.fields[name].widget.attrs.update({
                    'class': 'form-control',
                })
            # do not add to note fields
            elif name == 'note':
                pass
            # add a "form-control" class to each form input
            # for enabling bootstrap
            else:
                self.fields[name].widget.attrs.update({
                    'class': 'form-control',
                })
        # add place hoder to some input fields
        self.fields['best_result'].widget.attrs.update({
            'placeholder': "Metric: Accuracy",
        })
        self.fields['size_on_disk'].widget.attrs.update({
            'placeholder': "GB",
        })
        self.fields['directory_of_data'].widget.attrs.update({
            'placeholder': "Data on which pc?",
        })

    class Meta:
        # declare fields for add data form model
        model = models.Dataset
        fields = [
            'name',
            'data_category',
            'size_on_disk',
            'directory_of_data',
            'number_of_images',
            'number_of_classes',
            'brisque',
            'brightness',
            'sharpness',
            'iqa_3',
            'iqa_4',
            'mean_width',
            'mean_height',
            'shape_2',
            'shape_3',
            'shape_4',
            'analyzed',
            'best_result',
            'best_analyzed_model',
            'data_avatar',
            'note',
        ]
        widgets = {
            'note': Textarea(attrs={'cols': 57, 'rows': 3}),
        }


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
        # declare fields for data search form
        model = models.Dataset
        fields = [
            'name',
            'data_category',
            'directory_of_data',
            'analyzed',
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
        # declare fields for add new model form
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
        # declare fields for search model form
        model = models.AiModel
        fields = "__all__"


class AddModelTrainData(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(AddModelTrainData, self).__init__(*args, **kwargs)
        # add bootstrap
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control'
            })
        # set min max value for result fields
        self.fields['result'].widget.attrs['min'] = 0
        self.fields['result'].widget.attrs['max'] = 100

    class Meta:
        # declare fields for add record model trains data
        model = models.ModelTrainData
        fields = ['data', 'model', 'result']


class SearchModelTrainData(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(SearchModelTrainData, self).__init__(*args, **kwargs)
        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control'
            })
            self.fields[name].required = False
        self.fields['result'].widget.attrs['min'] = 0
        self.fields['result'].widget.attrs['max'] = 100
        self.fields['result'].widget.attrs.update({
            'placeholder': "Accuracy greater than",
        })

    class Meta:
        # declare fields for search record model trains data
        model = models.ModelTrainData
        fields = "__all__"
