from Wizard import *
from School import *
from House import *
from Guider import *


if __name__ == '__main__':
    # Objects creation - School, Houses, Wizards
    s_hogwarts = School(name='Hogwarts', headmaster='Albus Dumbeldore')

    h_gryffindor = House(name='Gryffindor', school=s_hogwarts, head='Prof. McGonnagel', password='grifgrif')
    h_slytherin = House(name='Slytherin', school=s_hogwarts, head='Severus Snape', password='sleek')

    w_harry = Wizard(name='Harry Potter', house=h_gryffindor, potions=75, charms=90)
    w_ron = Wizard(name='Ron Wisely', house=h_gryffindor, potions=65, charms=75)
    w_malfoy = Wizard(name='Draco Malfoy', house=h_slytherin, potions=90, charms=95)
    w_goyle = Wizard(name='Gregory Goyle', house=h_slytherin, potions=65, charms=45)
    w_tarshish = Wizard(name='Noam Tarshish', house=h_slytherin, potions=95, charms=100)

    # Adding Wizards to Houses -
    wiz_list = [w_harry, w_ron, w_malfoy, w_goyle, w_tarshish]
    h_gryffindor.add_wizard(wiz_list[:2])
    print(h_gryffindor.get_wizards())
    h_slytherin.add_wizard(wiz_list[2:])
    print(h_slytherin.get_wizards())

    print(h_gryffindor.is_wizard_in_house(w_goyle)) #False
    print(h_slytherin.is_wizard_in_house(w_goyle)) #True
    print(h_gryffindor.is_wizard_in_house(w_harry)) #True
    print(h_slytherin.is_wizard_in_house(w_harry)) #False
    print(h_slytherin.is_wizard_in_house(w_tarshish)) #True
    print(Wizard.__repr__(w_tarshish))
    print(h_slytherin)
    print(h_gryffindor.head)
    print(s_hogwarts.houses)


    print("########################")

    print("Wizard average:")
    print(w_harry.get_avg()) # 82.5
    print(w_malfoy.get_avg()) # 92.5
    print(w_malfoy > w_harry) #True
    # w_harry.set_grade(1, 100)
    print(w_harry == w_malfoy) #False
    print(w_malfoy > w_harry) #True

    print("########################")

    print("Enter dormitory:")
    w_harry.enter_dorm('grifgrif')
    w_ron.enter_dorm('incorrectpassword')
    print(w_harry.is_wizard_in_dorm()) # True
    print(w_ron.is_wizard_in_dorm()) # False
    w_harry.exit_dorm()
    print(w_harry.is_wizard_in_dorm()) # False

    print("########################")

    print("Wizard comparisons:")
    print(w_harry == w_malfoy) # False, 95.0 != 92.5
    print(w_ron > w_goyle) # True, 70.0 > 55.0

    print("########################")

    print("Print Wizard:")
    print(w_harry.get_avg())
    print(w_harry) # name: Harry Potter, average: 95.0, house: Griffyndor, in_dorm: False

    print("########################")

    # House Tests
    print(h_gryffindor.get_wizards())
    print(House.__repr__(h_gryffindor))

    print("########################")

    print("Score houses:")
    h_gryffindor.add_score(50)
    print(h_gryffindor)
    h_slytherin.add_score(45)
    print(h_slytherin)
    print(h_gryffindor < h_slytherin) # False, 50 > 45
    print(h_gryffindor == h_slytherin) #False
    print(h_gryffindor > h_slytherin) #True

    print("########################")

    # change password
    h_gryffindor.change_password('quidditch')
    w_ron.enter_dorm('quidditch')
    w_ron.enter_dorm('grifgrif') # wrong password, try again
    print(w_ron.is_wizard_in_dorm()) # True

    print("########################")

    # rank wizards
    print(h_slytherin.rank_wizards(1)) # w_tarshish
    print(h_slytherin.rank_wizards(2)) # w_malfoy
    print(h_slytherin.rank_wizards(3)) # w_goyle
    print(h_gryffindor.rank_wizards(1)) # w_harry
    print(h_gryffindor.rank_wizards(2)) # w_ron

    print("########################")

    print("check contains:")
    print(h_gryffindor.__contains__('Harry Potter')) #True
    print(h_gryffindor.__contains__('Gregory Goyle')) #False
    print(h_slytherin.__contains__('Harry Potter')) #False
    print(h_slytherin.__contains__('Gregory Goyle')) #True
    print(h_slytherin.__contains__('Noam Tarshish')) #True



    print("########################")

    # add houses to School
    houses_list = [h_gryffindor, h_slytherin]
    s_hogwarts.add_house(houses_list)
    print(s_hogwarts.avg_house_calculate(h_gryffindor))
    print(s_hogwarts.avg_house_calculate(h_slytherin))
    print(s_hogwarts.best_house_avg()) # Should return h_slytherin
    print(s_hogwarts.best_house_score()) # Should return h_gryffindor
    print(School.__repr__(s_hogwarts))
    print(s_hogwarts.houses)


    print("########################")

    # Guider Class -
    g_fred = Guider(name='Fred Weesley', house=h_gryffindor, potions=55, charms=65, play_quidditch=True)
    g_shay = Guider(name= 'Shay yeled zin', house=h_slytherin, potions=100, charms=100, play_quidditch=False)
    print(g_fred) # Guider (Fred Weesley, Gryffindor, 60.0)
    print(Guider.__repr__(g_fred))
    print(g_shay == g_fred) #False
    print(g_shay > g_fred) #True
    print(g_shay.play_guidditch) #False
