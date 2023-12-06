#!/usr/bin/env python3
from mimesis import Datetime
dt = Datetime()

class DateTime:
    year = dt.year(minimum=1999, maximum=2001)
    month = dt.month()
    day_of_month = dt.day_of_month()
    data = year, month, day_of_month
    birth_date = f"Year: {year} Month: {month} Day: {day_of_month}"

    def get_birth_date(self):
        return self.birth_date