import csv
import datetime
import calendar

def export_shift_schedule_to_csv(shift_schedule, filename="shift_schedule.csv"):
    """シフトスケジュールをCSVファイルとしてエクスポートする関数"""
    with open(filename, mode='w', encoding='utf-8-sig', newline='') as file:
        writer = csv.writer(file)

        # ヘッダーの作成
        writer.writerow(["日付", "曜日", "午前", "午後", "夜診", "姫路"])

        # 各日付ごとにシフトを出力
        for date_str, shifts in shift_schedule.items():
            # 日付と曜日を取得
            date_obj = datetime.datetime.strptime(date_str, "%Y-%m-%d")
            weekday = calendar.day_name[date_obj.weekday()]

            # 各シフト枠に割り当てられた職員名を取得
            morning_staff = ", ".join(shifts["morning"]) if shifts["morning"] else ""
            afternoon_staff = ", ".join(shifts["afternoon"]) if shifts["afternoon"] else ""
            night_staff = ", ".join(shifts["night"]) if shifts["night"] else ""
            himeji_staff = ", ".join(shifts["姫路"]) if "姫路" in shifts and shifts["姫路"] else ""

            # CSV行を書き込み
            writer.writerow([date_str, weekday, morning_staff, afternoon_staff, night_staff, himeji_staff])

    print(f"シフトスケジュールがCSV形式で {filename} に出力されました。")
