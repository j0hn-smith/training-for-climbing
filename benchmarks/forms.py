from django.forms import ModelForm

from benchmarks.models import BenchmarkResult, RepetitionResult, Benchmark
from django import forms

class BenchmarkResultForm(ModelForm):
    class Meta:
        model = BenchmarkResult
        fields = "__all__"

class BenchmarkForm(ModelForm):
    class Meta:
        model = Benchmark
        fields = ["name"]

class TestResultForm(ModelForm):
    class Meta:
        model = RepetitionResult
        fields = ["repetitions"]


ResultFormSet = forms.modelformset_factory(
    RepetitionResult,
    fields=('repetitions', ),
)
