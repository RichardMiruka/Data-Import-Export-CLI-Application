# Data-Import-Export-CLI-Application
This is a CLI application that simplifies the data import/export process. This involves efficiently handling large data files, ensuring data validation and integrity, and providing a reliable and scalable import/export solution.
The Data Import/Export CLI Application is a command-line tool designed to simplify the process of importing and exporting large amounts of data. It provides an efficient and reliable solution for handling data files, ensuring data validation and integrity, and seamlessly interacting with a database.

## Features

- Import data from various file formats into a database
- Export data from a database to different file formats
- Efficiently handle large data files
- Perform data validation and integrity checks
- Simple and intuitive command-line interface

## Installation

1. Clone the repository:

```shell
git clone https://github.com/RichardMiruka/Data-Import-Export-CLI-Application.git

2. Navigate to the project directory:

```shell
cd Data-Import-Export-CLI-Application

3. Install the required dependencies using Pipenv:

```shell
pipenv install

## Usage
Import Data
To import data from a file into the database, use the following command:

```shell
pipenv run cli import_data <file_path>
Replace <file_path> with the path to the data file you want to import.

Export Data
To export data from the database to a file, use the following command:

```shell
pipenv run cli export_data <file_path>
Replace <file_path> with the desired path and name of the exported file.

## Configuration
The application uses a configuration file (config.ini) to specify the database connection details. Update this file with your database credentials and settings before running the import/export commands.

## Contributing
Contributions are welcome! If you have suggestions, bug reports, or feature requests, please open an issue or submit a pull request.

License
This project is licensed under the MIT License. 
