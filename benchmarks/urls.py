from django.contrib import admin
from django.urls import path

from benchmarks.views import BenchmarkListView, BenchmarkDetailView, BenchmarkResultListView, BenchmarkCreateView, BenchmarkDeleteView

from benchmarks.views import show_benchmark_results, create_benchmark_result

urlpatterns = [
    path("", BenchmarkListView.as_view()),
    path("create/", BenchmarkCreateView.as_view(), name="create_benchmark"),
    path("<pk>/", BenchmarkDetailView.as_view(), name="detail"),
    path("<pk>/plot/", show_benchmark_results, name="plot"),
    path("<pk>/delete/", show_benchmark_results, name="delete"),
    path("<pk>/", BenchmarkDeleteView.as_view(), name="detail"),

    path("<pk>/create/", create_benchmark_result, name="create"),
    path("<pk>/results/", BenchmarkResultListView.as_view(), name="results"),
]
