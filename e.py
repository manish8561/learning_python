nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# square of n in a list with comprehension
# my_list = [n * n for n in nums]
my_list = [n for n in nums if n % 2 == 0]
print(my_list)

# Using a map + lambda
my_list2 = map(lambda n: n * n, nums)
print(my_list2)

# Dict comprehension
names = ["Bruce", "Clark", "Peter", "Logan", "Wade"]
heros = ["Batman", "Superman", "Spiderman", "Wolverine", "Deadpool"]

my_dict = {name: hero for name, hero in zip(names, heros)}
print(my_dict)
