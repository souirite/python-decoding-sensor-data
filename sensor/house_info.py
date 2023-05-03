from datetime import date
class HouseInfo:
    def __init__(self, data) -> None:
        self.data = data
    
    def get_data_by_area(self, field, rec_area = 0):
        field_data = []
        for record in self.data:
            if rec_area == 0:
                field_data.append(record[field])
            elif rec_area == int(record["area"]):
                field_data.append(record[field])
        return field_data
    
    def get_data_by_date(self,rec_data,rec_date= date.today()):
        field_data = []
        for record in self.data:
            if date.strftime(rec_date,"%m/%d/%y") == record["date"]:
                field_data.append(record[rec_data])
        return field_data

