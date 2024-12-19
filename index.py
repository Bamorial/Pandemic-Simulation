import random
import matplotlib.pyplot as plt
from Classes.Building import Building
from Classes.Individual import Individual 
from Classes.Data import Data 
from Classes.Day import Day 
from Classes.School import School 
from Classes.Hospital import Hospital
from Classes.Shop import Shop 
from Constants.constants import INFECTION_DURATION, INITIAL_INFECTED, DAY_COUNT, POPULATION_LEN, NUMBER_OF_BUILDINGS


def getCity():
    schools_arr = [School() for _ in range(NUMBER_OF_BUILDINGS['school'])]
    hospitals_arr = [Hospital() for _ in range(NUMBER_OF_BUILDINGS['hospital'])]
    shops_arr = [Shop() for _ in range(NUMBER_OF_BUILDINGS['shop'])]
    city=schools_arr+hospitals_arr+shops_arr
    return city

def initialize_individuals(population_len, initial_infected):
    individuals = [Individual(i) for i in range(population_len)]
    for i in range(initial_infected):
        individuals[i].isHealthy = INFECTION_DURATION
    return individuals

def update_health_status(individuals):
    for individual in individuals:
        if individual.isHealthy == 1:
            individual.isImmune = True
            individual.isHealthy = 0
        elif individual.isHealthy != 0:
            individual.isHealthy -= 1

def simulate_building_visits(individuals, buildings):
    allBuildings = set()
    for individual in individuals:
        if not buildings:
            break
        currentIndex = random.randrange(0, len(buildings))
        while True:
            goToBuilding = buildings[currentIndex]
            if goToBuilding.currentCapacity < goToBuilding.capacity:
                goToBuilding.newVisit(individual)
                allBuildings.add(goToBuilding)
                break
            else:
                allBuildings.add(goToBuilding)
                buildings.remove(goToBuilding)
                if not buildings:
                    break
                currentIndex = (currentIndex + 1) % len(buildings)
                continue
    return allBuildings

def infect_in_buildings(buildings):
    for building in buildings:
        if building.visitors:
            for visitor in building.visitors:
                if visitor.isHealthy != 0:
                    building.InfectRand()
                    break

def log_day_data(day_count, individuals, data):
    healthySum = sum(1 for i in individuals if i.isHealthy != 0)
    immuneSum = sum(1 for i in individuals if i.isImmune)
    
    data.day.append(day_count)
    data.sick.append(healthySum)
    data.healthy.append(len(individuals) - healthySum)
    data.immune.append(immuneSum)
    data.population.append(len(individuals))

def plot_results(data):
    plt.plot(data.day, data.population, label="Population")
    plt.plot(data.day, data.sick, label="Sick Individuals")
    plt.plot(data.day, data.immune, label="Immune Individuals")
    plt.xlabel('Time (Days)')
    plt.ylabel('Population')
    plt.legend()
    plt.show()



def EpidemicSimulation(population_len, initial_infected=100, day_count=14):
    individuals = initialize_individuals(population_len, initial_infected)
    data = Data()
    day = Day()
    for day_count in range(day_count):
        print(f"Day: {day_count}")
        update_health_status(individuals)
        
        currentTime = day.currentTime
        while currentTime < day.duration:
            print(f"CURRENT TIME: {currentTime}")
            
            log_day_data(day_count, individuals, data)
            buildings = getCity()
            allBuildings = simulate_building_visits(individuals, buildings)
            infect_in_buildings(allBuildings)

            currentTime += 1
        
        day.Reset()
        print(f"Day: {day_count} ended")

    plot_results(data)
    city=getCity()

EpidemicSimulation(POPULATION_LEN, INITIAL_INFECTED, DAY_COUNT)