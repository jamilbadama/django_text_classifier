import csv
from io import StringIO
from .models import TrainingSet


def handle_uploaded_file(f, classifier_name):
    csv_file = StringIO(f.read().decode())
    corpus_reader = csv.DictReader(csv_file, fieldnames=['body', 'target'])
    for row in corpus_reader:
        training_data = TrainingSet(body=row['body'], target=row['target'],
                                    classifier=classifier_name)
        training_data.save()


def open_file(path, classifier_name):
    with open(path, 'r') as f:
        handle_uploaded_file(f, classifier_name)
