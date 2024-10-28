import unittest
from src.scheduler import assign_shift
from src.utils import load_data

class TestScheduler(unittest.TestCase):
    def setUp(self):
        # テスト用のダミーデータを読み込み
        self.staff_data = load_data("data/staff_data.json")
        self.clinic_shifts = load_data("data/clinic_shifts.json")
        self.special_dates = load_data("data/special_dates.json")
    
    def test_assign_shift(self):
        # シフト割り当てを実行
        shift_schedule = assign_shift(self.staff_data, self.clinic_shifts, self.special_dates)
        
        # シフトスケジュールが生成されているか確認
        self.assertIsNotNone(shift_schedule)
        # 特定の日付・シフト枠に職員が割り当てられているかを確認
        self.assertTrue(any(shift_schedule[date]["morning"] for date in shift_schedule))

if __name__ == "__main__":
    unittest.main()
