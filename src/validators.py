def validate_shift_schedule(shift_schedule, staff_data):
    errors = []

    # 各職員の連続勤務、労働時間、勤務希望のチェック
    for staff in staff_data:
        staff_name = staff["name"]
        weekly_hours = 0
        monthly_hours = 0
        consecutive_days = 0
        previous_working_day = None

        for date_str, shifts in shift_schedule.items():
            # 当日の勤務シフトを確認
            is_working_today = any(staff_name in shifts[shift] for shift in shifts if shifts[shift])
            
            # 連続勤務チェック
            if is_working_today:
                consecutive_days += 1
                if consecutive_days > 5:
                    errors.append(f"{staff_name} が {date_str} に 5日以上連続勤務しています。")
            else:
                consecutive_days = 0

            # 労働時間のチェック
            if is_working_today:
                shift_hours = sum(get_shift_hours(shift, staff_name) for shift in shifts if staff_name in shifts[shift])
                weekly_hours += shift_hours
                monthly_hours += shift_hours

                if weekly_hours > staff["max_hours_per_week"]:
                    errors.append(f"{staff_name} が週の労働時間 {weekly_hours} 時間を超過しています。")
                if monthly_hours > staff["max_hours_per_month"]:
                    errors.append(f"{staff_name} が月の労働時間 {monthly_hours} 時間を超過しています。")
            
            # 週の初めに週労働時間をリセット
            if previous_working_day and (date_str.weekday() < previous_working_day.weekday()):
                weekly_hours = 0
            
            previous_working_day = date_str if is_working_today else previous_working_day

    # 結果の出力
    if errors:
        print("シフトスケジュールに以下のエラーがあります：")
        for error in errors:
            print(" -", error)
    else:
        print("シフトスケジュールは全ての条件を満たしています。")

def get_shift_hours(shift, staff_name):
    # シフトに応じた勤務時間を返す
    shift_hours = {
        "morning_afternoon": 8.5,
        "afternoon_night": 7,
        "night": 5.5,
        "姫路_金曜": 5,
        "姫路_土曜": 7
    }
    return shift_hours.get(shift, 0) if staff_name in shift else 0
