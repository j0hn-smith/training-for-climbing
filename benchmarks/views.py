import datetime
import random

from django.views.generic import ListView, DetailView, TemplateView, CreateView, View
from benchmarks.models import Benchmark, BenchmarkResult, RepetitionResult, RepetitionTest
from benchmarks.forms import BenchmarkResultForm, TestResultForm, BenchmarkForm
from django.forms import modelform_factory
from django.shortcuts import render, redirect

TIMES_EXERCISED = 7


# Create your views here.
class BenchmarkListView(ListView):
    model = Benchmark


class BenchmarkResultListView(ListView):
    model = BenchmarkResult


class BenchmarkDetailView(DetailView):
    model = Benchmark

class BenchmarkDeleteView(View):
    pass



class BenchmarkCreateView(View):
    form_class = BenchmarkForm
    template_name = "benchmarks/benchmark_form.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        return render(request, self.template_name, {"form": form})

    def create_test_object(self, foo, post_dict, form):
        number = foo[0][-1]
        test = RepetitionTest(name=post_dict.get(foo[0]),
                              description=post_dict.get("descriptionInput_"+str(number)),
                              target=post_dict.get("repetitionInput_"+str(number)),
                              benchmark=form
                              )
        test.save()

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        form = form.save()
        filtered_list = filter(lambda x: "nameInput" in x[0], request.POST.lists())
        for foo in filtered_list:
            self.create_test_object(foo, request.POST, form)
        return render(request, self.template_name, {"form": form})

def create_benchmark_result(request, pk):
    form_list = create_result_forms(pk)
    print(form_list)
    if request.method == "POST":
        form = BenchmarkResultForm(request.POST, request.FILES)
        for foo in form_list.values():
            if form.is_valid():
                form.save()
                return redirect('results', pk=pk)
                # do something.
    else:
        form = BenchmarkResultForm()
    return render(request, "benchmarks/benchmark_result_create.html", {"form": form, 'form_list': form_list})


def create_random_list():
    list_of_numbers = []
    for _ in range(TIMES_EXERCISED):
        list_of_numbers.append(random.randrange(0, 37))
    return list_of_numbers


def show_benchmark_results(request, pk):
    exercises = ['Liegestuetze', 'Dips', 'Klimmzuege', 'Lunchs', 'Squads']
    data_dict = {}
    times = []
    for i in range(TIMES_EXERCISED):
        times.append(datetime.datetime.now() + datetime.timedelta(days=-i))
    for foo in exercises:
        data_dict[foo] = create_random_list()

    return render(request, "benchmarks/benchmark_results_plot.html", {"data_dict": data_dict, "times": times})


def create_result_forms(pk):
    form_list = {}
    tests = Benchmark.objects.get(pk=pk).tests.all()
    for test in tests:
        result = RepetitionResult()
        result.test = test
        form_list[test.name] = TestResultForm(instance=result)
    return form_list
