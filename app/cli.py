import click
import csv
from .database import Session, Data

@click.group()
def cli():
    """Data Import/Export CLI Application"""
    pass

@cli.command()
@click.argument('file_path')
def import_data(file_path):
    """Import data from a CSV file into the database"""
    # How to Read the CSV file and extract data
    data = []

    with open(file_path, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        for row in csv_reader:
            data.append(row)

    # Create a session
    session = Session()

    try:
        # Iterate over the data and insert into the database
        for row in data:
            entry = Data(column1=row['column1'], column2=row['column2'], column3=row['column3'])
            session.add(entry)

        # Commit the changes
        session.commit()

        click.echo("Data import successful!")

    except Exception as e:
        # Rollback the transaction in case of an error
        session.rollback()

        click.echo(f"Data import failed: {str(e)}", err=True)

    finally:
        # Close the session
        session.close()

@cli.command()
@click.argument('file_path')
def export_data(file_path):
    """Export data from the database to a CSV file"""
    # Create a session
    session = Session()

    try:
        # Retrieve data from the database
        data = session.query(Data).all()

        # Convert data to a format suitable for CSV export
        csv_data = []
        for entry in data:
            row = [entry.column1, entry.column2, entry.column3]
            csv_data.append(row)

        # Write the data to a CSV file
        with open(file_path, 'w', newline='') as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(['column1', 'column2', 'column3'])  # Write the header row
            csv_writer.writerows(csv_data)

        click.echo("Data export successful!")

    except Exception as e:
        click.echo(f"Data export failed: {str(e)}", err=True)

    finally:
        # Close the session
        session.close()

# Add more commands and functions as needed

if __name__ == '__main__':
    cli()
