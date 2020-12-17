#CECS274 Lab Sec 07 Larry Delgado
import AdjacencyList
import DLList
import random
import matplotlib.pyplot as matplot

class Person: #node
    def __init__(self) -> bool:
        #CLEAN=0, INFECTED=1,DEAD=2,RECOVERED=3
        self.state = 0
        self.recover = 0
class covid19_Simulation:
    def __init__(self):
        self.people = 10000 #number of people 100000
        self.alpha = 0.01
        self.recovDays = 4
        self.fatalityR = 0.03
        self.initialSet = 0.01
        self.tr = 0.015
        self.clean = 0
        self.infected = 0
    #graph with n nodes(peopple)
    def getInteractionGraph(self, g, plist):
        for j in range(self.people):
            i = plist.get( random.randint(0,j) )
            if random.randint(0,1) < self.alpha:
                g.add_edge(j,i)
            else:
                k = plist.get( random.randint(0, random.randint(0,j)) ) #random node that node i points
                g.add_edge(j,k)
            return g

    def simulation(self, graph, day,plist):
        dead = 0
        recovered = 0
        
        while day <= 30:
            print("DAY: " + str(day) + " CLEAN: "+ str(self.clean) + " INFECTED: " + str(self.infected))                     #+"          DEAD: " + str(dead) + " RECOVERED: " + str(recovered))
            for v in range(plist.size()): #v nodes
                infectedPerson = plist.get(v)
                if infectedPerson.state == 1:
                    neighbors = graph.out_edges(0) #list
                    for n in range(neighbors.size()):
                        
                        neighbor = neighbors.get(n)
                        if random.randint(0,1) < self.tr:
                            neighbor.state = 1
                            self.infected += 1
                            self.clean -= 1
                            neighbor.recover = self.recovDays
                        infectedPerson.recover = infectedPerson.recover -1
                        if infectedPerson.recover == 0:
                            if 0 < self.fatalityR:
                                infectedPerson.state = 2 #dead
                                dead += 1
                                self.infected -= 1
                            else:
                                infectedPerson.state = 3 #recovered
                                recovered += 1
                                self.infected -= 1
            day += 1
        matplot.plot(day, self.infected)
        
    def initialInfectedNodes(self, graph, plist):
        for v in range(plist.size()):
            x = plist.get(v)
            neighbors = graph.out_edges(v)
            if random.randint(0,20) < self.initialSet:
                x.state = 1
                self.infected += 1
                for neighbor in range(neighbors.size()):
                    if graph.has_edge(v, int(neighbor) ):
                        neighbor.recover = recovDays
            else:
                x.state = 0 #clean
                self.clean += 1

def main():
    covid19 = covid19_Simulation()
    al = DLList.DLList()
    for population in range(covid19.people):
        person = Person()
        al.append(person)
    #With lockdown
    g1 = AdjacencyList.AdjacencyList(covid19.people)
    #Without lockdown
    g2 = AdjacencyList.AdjacencyList(covid19.people)
        
    covid19.getInteractionGraph(g1,al)
    covid19.initialInfectedNodes(g1,al)
    covid19.simulation(g1,0,al)
    matplot.show()

    
main()
