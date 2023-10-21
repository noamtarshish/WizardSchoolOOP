from functools import total_ordering
from Wizard import *
import copy
class House:
    def __init__(self, name, school, head, password, score=0, wizard_list=[]):
        """
        Function that define the init for House class
        :param name: the name of the house
        :param school: the school that the house belong
        :param head: the name of the head of the school
        :param password: password for entering the dorms
        :param score: score of the house
        :param wizard_list: copied list of the wizards belong to the house
        """
        self.name = name
        self.school = school
        self.head = head
        self.password = password
        self.score = int(score)
        self.wizard_list = copy.copy(wizard_list)

    def get_wizards(self):
        """
        Function that return list of the wizards belong to the house
        """
        return self.wizard_list

    def set_head(self, head):
        """
        Function that get the name of the new head of the house and update his name
        """
        self.head = head

    def add_score(self, points):
        """
        Function that add score as 'points' to the score of the house
        """
        self.score += points

    def change_password(self, new_password):
        """
        Function that get str of the new password of the house and update his password
        """
        self.password = new_password

    def add_wizard(self, wiz):
        """
        Function that get list of wizard and check if the wizard found in house wizard list, if not, the function will append the wizard
        """
        for wizard in wiz:
            if wizard not in self.wizard_list:
                self.wizard_list.append(wizard)


    def is_wizard_in_house(self, wiz):
        """
        Recursive function that check if wizard in house via house wizard list
        :param wiz: wizard
        :return: True if the wizard in house and False if not
        """

        return self.helper(wiz, 0) #calling to the helper function

    def helper(self, wiz, index):
        """
        Helper recursive function to is_wizard_in_house that do the recursion to check if wizard in house
        :param wiz: wizard
        :param index: index
        :return: True if the wizard in house and False if not
        """
        if len(self.wizard_list) == index: #break conditions
            return False
        if self.wizard_list[index].name == wiz.name: #if there is wizard with the same name return True
            return True
        else:
            return self.helper(wiz, index+1)


    def rank_wizards(self, rank):
        """
        Function that sort(in bubble sort) all the wizard of the house by their average of courses and return the wizard with the given rank
        :param rank: number represent the rank of the needed wizard
        :return: the wizard with the rank that given in the function
        """
        wizard_list1 = copy.copy(self.wizard_list) #shallow copy to work with copied list and in order to not change the original list
        for i in range(len(wizard_list1)):
            minimum = i
            for j in range(i+1, len(wizard_list1)): #bubble sort
                if Wizard.get_avg(wizard_list1[minimum]) > Wizard.get_avg(wizard_list1[j]):
                    minimum = j

            tmp = wizard_list1[i]
            wizard_list1[i] = wizard_list1[minimum]
            wizard_list1[minimum] = tmp

        if rank > len(wizard_list1): #condition which wizard needs to return
            return wizard_list1[0]
        elif 0 < rank <= len(wizard_list1):
            return wizard_list1[-rank]
        else:
            return None

    def __repr__(self):
        """
        Function that return repr of the house included name, score and wizard list of the house
        """
        arrange_wizard_str = ""
        for wizard in self.wizard_list:
            arrange_wizard_str += str(wizard.name) + ' | '
        arrange_wizard_str = arrange_wizard_str[:-2]

        return "House of " + self.name + " has " + str(self.score) + " points. The proud wizards of " + self.name + " are:" \
            + arrange_wizard_str

    @total_ordering
    # 6 function that check arithmetic equations between score of two houses

    def __eq__(self, other):
        return self.score == other.score

    def __lt__(self, other):
        return self.score < other.score

    def __gt__(self, other):
        return self.score > other.score

    def __le__(self, other):
        return self.score <= other.score

    def __ge__(self, other):
        return self.score >= other.score

    def __ne__(self, other):
        return self.score != other.score

    def __contains__(self, wizard_name):
        """
        Function that check if wizard found in house by its name
        :param wizard_name: name of the wizard
        :return: True if there is wizard with the same name in house, False if not
        """
        name_wizard_list = []
        for wizard in self.wizard_list:
            name_wizard_list.append(wizard.name)
        return wizard_name in name_wizard_list














