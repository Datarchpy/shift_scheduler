from src.scheduler import assign_shift
from src.exporter import export_shift_schedule_to_csv
from src.validators import validate_shift_schedule
from src.utils import load_data

def main():
    # データの読み込み
    staff_data = load_data("data/staff_data.json")
    clinic_shifts = load_data("data/clinic_shifts.json")
    special_dates = load_data("data/special_dates.json")
    
    # シフト割り当ての実行
    shift_schedule = assign_shift(staff_data, clinic_shifts, special_dates)
    
    # バリデーションの実行
    validate_shift_schedule(shift_schedule, staff_data)
    
    # CSV出力
    export_shift_schedule_to_csv(shift_schedule, filename="2024_11_shift_schedule.csv")

if __name__ == "__main__":
    main()
