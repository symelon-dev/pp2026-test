def is_leap_year(year):
    """西暦 year が閏年なら True、そうでなければ False を返す。"""
    return year % 4 == 0


if __name__ == "__main__":
    for year in [2024, 2028, 2000, 1900]:
        print(year, is_leap_year(year))

