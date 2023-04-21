from django.db import models
from django.contrib.postgres import fields as postgres_fields


# class BaseTest(models.Model):
#     # Fields
#     created = models.DateTimeField(auto_now_add=True, editable=False)
#     name = models.CharField(blank=False, max_length=255)
#     description = models.TextField(blank=True)
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         abstract = True
class Benchmark(models.Model):
    # Relationships
    # Fields
    name = models.CharField(blank=False, max_length=255)
    created = models.DateTimeField(auto_now_add=True, editable=False)

    def __str__(self):
        return self.name


class RepetitionTest(models.Model):
    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    name = models.CharField(blank=False, max_length=255)
    description = models.TextField(blank=True)
    target = models.IntegerField()
    benchmark = models.ForeignKey(Benchmark, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class BenchmarkResult(models.Model):
    # Relationships
    baseBenchmark = models.ForeignKey(Benchmark, on_delete=models.CASCADE)
    # Fields
    created = models.DateTimeField(auto_now_add=True, editable=False)
    comment = models.TextField(blank=True)


class RepetitionResult(models.Model):
    # Relationships
    benchmarkResult = models.ForeignKey(BenchmarkResult, on_delete=models.CASCADE)
    repetitions = models.IntegerField()
    test = models.ForeignKey(RepetitionTest, on_delete=models.CASCADE)

# class TestResult(models.Model):
#     # Relationships
#     benchmarkResult = models.ForeignKey(BenchmarkResult, on_delete=models.CASCADE)
#
#     # Fields
#     created = models.DateTimeField(auto_now_add=True, editable=False)


# class BooleanTest(BaseTest):
#     target = models.BooleanField()
#
#
# class BooleanResult(TestResult):
#     true = models.BooleanField()
#     test = models.ForeignKey(BooleanTest, on_delete=models.CASCADE)
#
#
# class QuizzTest(BaseTest):
#     target = models.IntegerField()
#     range = postgres_fields.IntegerRangeField()
#
#
# class QuizzResult(TestResult):
#     answer = models.IntegerField()
#     test = models.ForeignKey(QuizzTest, on_delete=models.CASCADE)
#
#
# class QuestionTest(BaseTest):
#     target = models.TextField()
#
#
# class QuestionResult(TestResult):
#     answer = models.TextField()
#     test = models.ForeignKey(QuestionTest, on_delete=models.CASCADE)
#
#
# class TimedTest(BaseTest):
#     target = models.TimeField()
#
#
# class TimedResult(TestResult):
#     time = models.TimeField()
#     test = models.ForeignKey(QuestionTest, on_delete=models.CASCADE)
