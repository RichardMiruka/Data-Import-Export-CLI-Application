import click
import csv
from sqlalchemy.orm import sessionmaker
from .database import Session
from .models import Data
from .utils import merge_sort

class Importer:
    def __init__(self, file_path, sort):
        self.file_path = file_path
        self.sort = sort

    def run(self):
        data = []

        with open(self.file_path, 'r') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for row in csv_reader:
                data.append(row)

        if self.sort:
            column1_values = [row['column1'] for row in data]
            sorted_column1 = merge_sort(column1_values)
            for i, row in enumerate(data):
                row['column1'] = sorted_column1[i]

        session = Session()

        try:
            for row in data:
                entry = Data(column1=row['column1'], column2=row['column2'], column3=row['column3'])
                session.add(entry)

            session.commit()

            click.echo("Data import successful!")

        except Exception as e:
            session.rollback()
            click.echo(f"Data import failed: {str(e)}", err=True)

        finally:
            session.close()

class Exporter:
    def __init__(self, file_path):
        self.file_path = file_path

    def run(self):
        session = Session()

        try:
            data = session.query(Data).all()

            csv_data = []
            for entry in data:
                row = [entry.column1, entry.column2, entry.column3]
                csv_data.append(row)

            with open(self.file_path, 'w', newline='') as csv_file:
                csv_writer = csv.writer(csv_file)
                csv_writer.writerow(['column1', 'column2', 'column3'])
                csv_writer.writerows(csv_data)

            click.echo("Data export successful!")

        except Exception as e:
            click.echo(f"Data export failed: {str(e)}", err=True)

        finally:
            session.close()


@click.group()
def cli():
    """Data Import/Export CLI Application"""
    pass

