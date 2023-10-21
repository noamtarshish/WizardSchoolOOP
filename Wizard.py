from functools import total_ordering

class Wizard:
    def __init__(self, name, house, potions, charms, in_dorm=False):
        """
        Function that start the init for the Wizard class
        :param name: name of the wizard
        :param house: house the wizard belong to
        :param potions: grade of the wizard in potions course
        :param charms: grade of the wizard in charms course
        :param in_dorm: boolean value represent if the wizard in dorm or not
        """
        self.name = name
        self.house = house
        self.potions = int(potions)
        self.charms = int(charms)
        self.in_dorm = in_dorm

    def get_avg(self):
        """
        Function that calculate the average of the wizard's courses
        """
        return float((self.potions + self.charms) / 2) #Calculate the average

    def enter_dorm(self, password):
        """
        Function that get password and check if this the right password for the wizard's house
        :param password: string represent password
        """
        true_password = self.house.password
        if true_password == password:
            self.in_dorm = True
        else:
            print("wrong password, try again")

    def exit_dorm(self):
        """
        Function that exit the wizard from the dorm
        """
        self.in_dorm = False

    def set_grade(self, course, grade):
        """
        Function that update grade for course
        :param course: number represent the course of the wizard
        :param grade: grade of the course to update
        """
        if course == 1:
            self.potions = grade
        else:
            self.charms = grade

    def is_wizard_in_dorm(self):
        """
        Function that check if wizard in dorm
        :return: True if the wizard in house, False if not
        """
        if self.in_dorm is True:
            return True
        else:
            return False

    def __repr__(self):
        """
        Function that return the repr with the details of the wizard
        """
        return "name: " + str(self.name) + ", average: " + str(self.get_avg()) + ", house: " + str(
            self.house.name) + ", in_dorm: " + str(self.in_dorm)

    @total_ordering
    # 6 function that check arithmetic equations between average of two wizards

    def __eq__(self, other):
        return self.get_avg() == other.get_avg()

    def __lt__(self, other):
        return self.get_avg() < other.get_avg()

    def __gt__(self, other):
        return self.get_avg() > other.get_avg()

    def __le__(self, other):
        return self.get_avg() <= other.get_avg()

    def __ge__(self, other):
        return self.get_avg() >= other.get_avg()

    def __ne__(self, other):
        return self.get_avg() != other.get_avg()
