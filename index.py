import random
import copy
import matplotlib.pyplot as plt
from Classes.Building import Building
from Classes.Individual import Individual 
from Classes.Data import Data 
from Classes.Day import Day 
from Classes.School import School 
from Classes.Hospital import Hospital
from Classes.Shop import Shop 

infectionRate = 4

def EpidemicSimulation(population_len, initial_infected=100, day_count=14):
    individuals = [Individual(i) for i in range(population_len)]
    for i in range(initial_infected):
        individuals[i].isHealthy=3
    data = Data()
    day = Day()
    schools = [School() for i in range(0)]
    hospitals = [Hospital() for i in range(0)]
    shops = [Shop() for i in range(100)]
    
    for dayCount in range(day_count):
        for i in individuals:
            if i.isHealthy == 1: 
                i.isImmune = True
                i.isHealthy = 0
            elif i.isHealthy != 0:
                i.isHealthy -= 1
        
        currentTime = day.currentTime
    
        while currentTime < day.duration:
            print('CURRENT TIME ' + str(currentTime))
            print('Day: ' + str(dayCount))
            
            healthySum = 0
            immuneSum = 0
            for i in individuals:
                if i.isHealthy != 0: healthySum += 1
                if i.isImmune == True: immuneSum += 1 
            
            print('Individuals: ' + str(len(individuals)))
            print('Sick: ' + str(healthySum))
            print('Healthy: ' + str(len(individuals) - healthySum))

            data.day.append(dayCount) 
            data.sick.append(healthySum)
            data.healthy.append(len(individuals) - healthySum)
            data.immune.append(immuneSum)
            data.population.append(len(individuals))

            buildings = schools + hospitals + shops
            allBuildings=set()            
            for individual in individuals:
                print(individual)
                if len(buildings) == 0:
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
                        if len(buildings) == 0:
                            break
                        currentIndex = (currentIndex + 1) % len(buildings)
                        continue
            
            currentTime += 1
            print(allBuildings)
            for building in allBuildings:
                if len(building.visitors) > 0:
                    for visitor in building.visitors:
                        if visitor.isHealthy != 0:
                            building.InfectRand(infectionRate)
                            break
        
        for individual in individuals:
            print(individual)
        
        print('Day: ' + str(dayCount) + ' ended')
        day.Reset()
    
    plt.plot(data.day, data.population, label="Population")
    plt.plot(data.day, data.sick, label="Sick Individuals")
    plt.plot(data.day, data.immune, label="Immune Individuals")
    plt.xlabel('Time (Days)')
    plt.ylabel('Population')
    plt.legend()
    plt.show()

EpidemicSimulation(1000)