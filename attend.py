import csv
import os
from datetime import date

FILE = "attendance.csv"   # 출석 기록을 저장할 파일


def add_attendance():
    """출석 한 건을 기록한다."""
    # 엔터만 치면 오늘 날짜를 자동으로 넣는다
    d = input("날짜 (YYYY-MM-DD, 엔터=오늘): ").strip()
    if d == "":
        d = str(date.today())

    name = input("이름: ").strip()
    if name == "":
        print("이름이 비어 있어요. 기록하지 않았습니다.")
        return

    # append 모드('a')로 열면 기존 내용 뒤에 한 줄씩 쌓인다
    with open(FILE, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow([d, name])

    print(f"기록 완료: {d} / {name}")


def show_list():
    """저장된 출석 목록을 보여준다."""
    if not os.path.exists(FILE):
        print("아직 출석 기록이 없습니다.")
        return

    with open(FILE, "r", encoding="utf-8") as f:
        reader = csv.reader(f)
        rows = list(reader)

    if not rows:
        print("아직 출석 기록이 없습니다.")
        return

    print("\n--- 출석 목록 ---")
    for row in rows:
        if len(row) < 2:
            continue  # 형식이 깨진 줄은 건너뛴다
        d, name = row[0], row[1]
        print(f"{d}  {name}")
    print("----------------\n")


def main():
    while True:
        print("1) 출석 기록   2) 목록 보기   3) 끝내기")
        choice = input("선택: ").strip()

        if choice == "1":
            add_attendance()
        elif choice == "2":
            show_list()
        elif choice == "3":
            print("종료합니다.")
            break
        else:
            print("1, 2, 3 중에서 골라주세요.")


if __name__ == "__main__":
    main()
