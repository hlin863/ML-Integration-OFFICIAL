from django import forms


class RepositorySelectionForm(forms.Form):
    repository_url = forms.URLField(
        label="Public GitHub repository URL",
        widget=forms.URLInput(
            attrs={
                "class": "form-control",
                "placeholder": "https://github.com/owner/project",
            }
        ),
    )
    branch = forms.CharField(
        label="Branch",
        initial="main",
        max_length=100,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "main",
            }
        ),
    )
    dataset_paths = forms.CharField(
        label="Dataset paths to watch",
        initial="data/**, *.csv",
        widget=forms.Textarea(
            attrs={
                "class": "form-control",
                "placeholder": "data/**, *.csv",
                "rows": 3,
            }
        ),
    )
    training_command = forms.CharField(
        label="Training/test command",
        initial="python train.py",
        max_length=500,
        widget=forms.TextInput(
            attrs={
                "class": "form-control",
                "placeholder": "python train.py",
            }
        ),
    )
    metric_threshold = forms.DecimalField(
        label="Minimum test metric",
        required=False,
        min_value=0,
        max_digits=8,
        decimal_places=3,
        widget=forms.NumberInput(
            attrs={
                "class": "form-control",
                "placeholder": "Optional",
                "step": "0.001",
            }
        ),
    )
