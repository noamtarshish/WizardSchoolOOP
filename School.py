import copy
from House import House
from Wizard import Wizard

class School:
    def __init__(self, name, headmaster, houses=[]):
        """
        Function that define the init for the school class
        :param name: name of the school
        :param headmaster: name of the head master of the school
        :param houses: list of the houses in the school in shallow copy
        """
        self.name = name
        self.headmaster = headmaster
        self.houses = copy.copy(houses)

    def set_name(self, new_name):
        """
        Function that get the name of the school update the name
        """
        self.name = new_name

    def add_house(self, wiz):
        """
        Function that get list of houses and check if the house found in school houses list, if not, the function will append the house
        """
        for house in wiz:
            if house not in self.houses:
                self.houses.append(house)

    def set_headmaster(self, new_headmaster):
        """
        Function that get the name of the headmaster of the school and update his name
        """
        self.headmaster = new_headmaster

    def avg_house_calculate(self, house):
        """
        Helper function to best_house_avg the calculate the house avg
        :param house: the house we want to calculate the average
        :return: house average
        """
        house_avg = 0
        for wizard in house.get_wizards():
            house_avg += Wizard.get_avg(wizard)

        return house_avg / len(house.wizard_list)

    def best_house_avg(self):
        """
        Function that return the house that his wizards has the best average with bubble sort
        :return: the house with the highest average
        """

        houses_list1 = copy.copy(self.houses)  #shallow copy to work with copied list and in order to not change the original list
        for house in range(len(houses_list1)):
            minimum = house
            for j in range(house + 1, len(houses_list1)):  # bubble sort
                if self.avg_house_calculate(houses_list1[minimum]) > self.avg_house_calculate(houses_list1[j]):
                    minimum = j

            tmp = houses_list1[house] #swap
            houses_list1[house] = houses_list1[minimum]
            houses_list1[minimum] = tmp

        return houses_list1[-1] #return the house with the highest average in the sorted houses list

    def sort_house_by_score(self, houses):
        """
        Helper function to best house score that sort the list of houses by the score with merge sort(with nlogn complexity)
        :param houses: list of houses to sort
        :return: sorted list
        """

        if len(houses) > 1: #Merge Sort
            middle = len(houses) // 2
            left = houses[:middle] #dividing the list to two seperate list by the middle
            right = houses[middle:]
            self.sort_house_by_score(left) #the same for every seperate list
            self.sort_house_by_score(right)
            i = 0
            j = 0
            k = 0

            while i < len(left) and j < len(right): #while loops to check where to stop
                if left[i].score < right[i].score:
                    houses[k] = left[i]
                    i += 1
                else:
                    houses[k] = right[j]
                    j += 1
                k += 1

            while i < len(left):
                houses[k] = left[i]
                i += 1
                k += 1

            while j < len(right):
                houses[k] = right[j]
                j += 1
                k += 1

        return houses

    def best_house_score(self):
        """
        Function that return the house with the highest score in school, using merge sort implemented in function sort_house
        """
        sorted_score_list = self.sort_house_by_score(self.houses) #Calling to the sort function to sort the list
        return sorted_score_list[-1] #return the house with the highest score in the sorted list


    def __repr__(self):
        """
        Function that return repr of the school included name, and headmaster of the school
        """
        return self.name + " school for witchcraft and wizardry, under head master " + self.headmaster
