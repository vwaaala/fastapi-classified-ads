import csv
from io import StringIO

from Car import PersonalCarSchema, PersonalCarService


async def process_csv_file(file, db):
    csv_file = await file.read()
    data = csv.DictReader(StringIO(csv_file.decode('utf-8')))

    for row in data:
        schema_data = PersonalCarSchema.CarResponseShort(**row)
        PersonalCarService.create_car(db, schema_data)
