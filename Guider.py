from Wizard import Wizard
class Guider(Wizard):

    def __init__(self, name, house, potions, charms, play_quidditch, in_dorm=False):
        """
        Function that initial the init for guider class
        :param name: name of the guider
        :param house: house that the guider belong
        :param potions: grade of the wizard in potions course
        :param charms: grade of the wizard in charms course
        :param play_quidditch: boolean value represent if the guider play quidditch or not
        :param in_dorm: boolean value represent if the guider in dorms or not
        """
        super().__init__(name, house, potions, charms, in_dorm) #inheritance from wizard class
        self.play_guidditch = play_quidditch

    def __repr__(self):
        """
        Function that return the repr with the details of the guider
        """
        return "Guider (" + self.name + ", " + str(self.house.name) + ", " + str(self.get_avg()) + ")"


