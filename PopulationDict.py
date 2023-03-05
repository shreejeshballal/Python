pop = {}

n = int(input("Enter no of country:"))
for i in range(n):
    name = input("Enter country name:")
    pop[name] = int(input("Enter population:"))

boomerPopulation = 0
boomerCountry = ''
for country in pop:
    if pop[country]>boomerPopulation:
        boomerPopulation = pop[country]
        boomerCountry = country

print(boomerCountry)
