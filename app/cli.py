import click
import csv
from sqlalchemy.orm import sessionmaker
from app.database import Session, Data
from .models import Base, DataModel
from .utils import merge_sort

@click.group()
def cli():
    """Data Import/Export CLI Application"""
    pass

@cli.command()
@click.argument('file_path')
@click.option('--sort', '-s', is_flag=True, help='Sort the data before importing')
def import_data(file_path, sort):
    """
    Import data from a CSV file into the database
    
    Args:
        file_path (str): Path to the CSV file
        sort (bool): Flag to enable sorting of data before importing
    """
    data = []

    with open(file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append(row)

    if sort:
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

@cli.command()
@click.argument('file_path')
def export_data(file_path):
    """
    Export data from the database to a CSV file
    
    Args:
        file_path (str): Path to the CSV file for exporting the data
    """
    session = Session()

    try:
        data = session.query(Data).all()

        csv_data = []
        for entry in data:
            row = [entry.column1, entry.column2, entry.column3]
            csv_data.append(row)

        with open(file_path, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(['column1', 'column2', 'column3'])
            csv_writer.writerows(csv_data)

        click.echo("Data export successful!")

    except Exception as e:
        click.echo(f"Data export failed: {str(e)}", err=True)

    finally:
        session.close()

if __name__ == '__main__':
    cli()
