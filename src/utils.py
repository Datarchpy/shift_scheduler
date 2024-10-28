import json

def load_data(filepath):
    """JSONファイルを読み込む関数"""
    with open(filepath, "r", encoding="utf-8") as file:
        return json.load(file)

def get_shift_hours(shift_type):
    """シフトの種類に応じた労働時間を返す"""
    shift_hours = {
        "morning_afternoon": 8.5,
        "afternoon_night": 7,
        "night": 5.5,
        "himeji_friday": 5,
        "himeji_saturday": 7
    }
    return shift_hours.get(shift_type, 0)
