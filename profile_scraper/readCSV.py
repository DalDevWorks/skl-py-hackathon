import csv
from .models import Profile


def readCSV(file):
    # Open and read info from local csv file.
    with open(file, "rb") as csvfile:
        next(csvfile)
        reader = csv.reader(csvfile)
        for row in reader:
            user = Profile(
                twitterUserName=row[0].rsplit('/', 1)[-1],
                twitterSource=row[0],
                firstName=row[1],
                lastName=row[2],
                domain=row[3],
                company=row[4],
                jobTitle=row[5],
                city=row[6],
                state=row[7],
                country=row[8],
                linkedin=row[9],
                cdSize=row[10],
                cdIndustry=row[11],
                hqCity=row[14],
                hqState=row[15],
                hqCountry=row[16],
            )
            user.save()
