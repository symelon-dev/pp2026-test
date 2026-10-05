# leap.py の is_leap_year が正しいかを確かめる。
# 実行方法: python checkpoints/01/check_leap.py
import sys
import unicodedata
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from leap import is_leap_year

GREEN = "\033[32m"
RED = "\033[31m"
BOLD = "\033[1m"
RESET = "\033[0m"


def pad(text, width):
    # 全角文字は端末で 2 文字分の幅を取るので、表示幅で揃える
    shown = sum(2 if unicodedata.east_asian_width(c) in "WF" else 1 for c in text)
    return text + " " * (width - shown)


def label(value):
    return "閏年" if value else "閏年でない"


def hint(year):
    if year % 400 == 0:
        return "決まり③：400 で割り切れる年は閏年"
    if year % 100 == 0:
        return "決まり②：100 で割り切れる年は閏年でない"
    return "決まり①：4 で割り切れる年は閏年"


cases = [
    (2024, True),
    (2025, False),
    (2000, True),
    (1900, False),
    (2100, False),
    (2400, True),
]

print(f"{BOLD}  {pad('年', 6)} {pad('正しい答え', 12)} {pad('あなたのプログラム', 20)} 判定{RESET}")
print(f"  {'-' * 6} {'-' * 12} {'-' * 20} {'-' * 4}")

failed = []
for year, expected in cases:
    actual = is_leap_year(year)
    if actual == expected:
        mark = f"{GREEN}✓ OK{RESET}"
    else:
        mark = f"{RED}✗ NG{RESET}"
        failed.append(year)
    print(f"  {pad(str(year), 6)} {pad(label(expected), 12)} {pad(label(actual), 20)} {mark}")

print()
if failed:
    print(f"{RED}{BOLD}{len(cases)} 件中 {len(failed)} 件が NG です。{RESET}")
    print("NG の年が守れていない決まり：")
    for year in failed:
        print(f"  {year} 年 → {hint(year)}")
    sys.exit(1)
print(f"{GREEN}{BOLD}{len(cases)} 件すべて OK です。{RESET}")
