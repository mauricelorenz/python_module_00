def ft_count_harvest_recursive(days=None, last_day=None):
    if days is None:
        days = int(input("Days until harvest: "))
        last_day = days
    if days > 1:
        ft_count_harvest_recursive(days - 1, last_day)
    print(f"Day {days}")
    if days == last_day:
        print("Harvest time!")
