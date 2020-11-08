import myfitnesspal

client = myfitnesspal.Client('xxx', password='xxx')

day = client.get_date(2020, 11, 5)
print(day.meals)
dinner = day.meals[2]
print(dinner.entries)