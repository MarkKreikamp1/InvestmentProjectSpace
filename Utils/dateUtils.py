from datetime import datetime


class DateUtils:
    def __init__(self):
        pass

    @staticmethod
    def get_current_date() -> datetime:
        return datetime.strptime((datetime.now().strftime("%Y-%m-%d %H:%M:%S")), "%Y-%m-%d %H:%M:%S")

    @staticmethod
    def convert_string_to_date_time(date_string) -> datetime:
        return datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")

