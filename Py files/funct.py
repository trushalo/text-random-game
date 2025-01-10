# functions outside objects

import random
import time
# import json

import kivy_local as kl
import zpg_lists as zl
from datetime import datetime

'''Global functions:

    find_highest_intensity_mood
    gender_article
    get_current_time_hhmmss
    upper (change first letter of string to upper case)
    create_random_dict
    random_activity
    random_name
    create_npc_list
    space_loop
    random_name'''

data_list = []


def update_variable_list(new_data) :
    """
    Updates a list of variables with new incoming data.
    Maintains a maximum of five variables in the list.

    Args:
      new_data: The new data to be added to the list.

    Returns:
      The updated list of variables.
    """

    # Add the new data to the beginning of the list
    data_list.insert(0, new_data)

    # If the list exceeds the maximum size, remove the oldest element
    if len(data_list) > 5 :
        data_list.pop()


def find_highest_intensity_mood(mood_dictionary) :
    """Finds the mood with the highest intensity and returns it.

  Args:
    mood_dictionary: A dictionary with mood descriptions as keys and intensities as values.

  Returns:
    The mood with the highest intensity.
  """

    highest_intensity = max(mood_dictionary.values())
    highest_intensity_moods = [mood for mood, intensity in mood_dictionary.items() if intensity == highest_intensity]

    # Return a random mood from the list of highest intensity moods
    return random.choice(highest_intensity_moods)


def gender_article(gender) :
    if gender in zl.gender_are :
        return 'are'
    elif gender in zl.gender_is :
        return 'is'
    else :
        return 'is'


def get_current_time_hhmmss() :
    """
    Gets the current time in HH:MM:SS format.

    Returns:
      A string representing the current time in HH:MM:SS format.
    """
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    return current_time


def upper(first) :
    return first[0].upper() + first[1 :]


def create_random_dict(keys, value_range) :
    """Creates a dictionary with random values for given keys.

  Args:
    keys: A list of keys for the dictionary.
    value_range: A tuple (min, max) defining the range of value values.

  Returns:
    A dictionary with random values for the given keys.
  """

    random_dict = { }
    for key in keys :
        value = random.randint(*value_range)
        random_dict[key] = value
    return random_dict


def random_activity(comment_list, character) :
    """Selects a random activity from the list and updates the character's mood.

  Args:
    comment_list: A list of tuples, where each tuple contains a comment, mood, and energy impact.
    character: The character object whose mood_dict should be updated.

  Returns:
    The random comment.
  """

    random_act = random.choice(comment_list)
    if random_act[2] :
        character.mood_dict[random_act[1]] = character.mood_dict.get(random_act[1], 0) + random_act[2]
    return random_act[0]


def random_name(first_name, last_name) :
    """Concatenates first and last name lists.

  Args:
    first_name: A list of strings, first_name.
    last_name: A list of strings, last_name.

  Returns:
    The random name.
  """
    return random.choice(first_name) + ' ' + random.choice(last_name)


def create_npc_list(location, value) :
    """Creates a list of NPCs associated with a location

    Args:
        location: a location (ship, station, sector, or planets)
        value: size. 3 NPC for size 1 for every size increase.
    """

    npc_list = []
    j_list = zl.job_list
    npc_count = value * 3
    count: int = 0
    for _ in range(npc_count) :
        # Create an instance of NPC
        j_list_2: list[str] = [j_list[count]]
        npc = NPC(location, j_list_2)

        npc_list.append(npc)
        count = count + 1
    return npc_list


def space_loop(character) :
    '''Creates loop of recurring comment pulls indicating the character
    is in space until moods exceed thresholds which triggers mood loops.'''
    # Count is used to test length of loop. Remove.
    # count = 0
    while (80 > character.mood_dict['angry'] > 20 and character.mood_dict['sad'] < 80 and character.mood_dict[
        'sad'] > 20 and character.mood_dict['greedy'] < 80 and character.mood_dict['greedy'] > 20 and
           character.mood_dict['reckless'] < 80 and character.mood_dict['reckless'] > 20) :
        comment = get_current_time_hhmmss() + ': ' + random_activity(zl.comment_list, character)
        update_variable_list(comment)
        #        update_comments(comment)
        # Printing of character.mood_dict is used to test mood change. Remove.
        print(comment + ' ' + str(character.mood_dict))
        # Count is used to test length of loop. Remove.
        # count = +1
        # Count is used to test length of loop. Remove.
        time.sleep((random.randint(41, 150)) / 240)  # print(count)

    if character.mood_dict['angry'] >= 80 :
        return emote_loop(character, zl.angry_list)
    if character.mood_dict['angry'] <= 20 :
        return emote_loop(character, zl.chill_list)
    if character.mood_dict['reckless'] >= 80 :
        return emote_loop(character, zl.reckless_list)
    if character.mood_dict['reckless'] <= 20 :
        return emote_loop(character, zl.careful_list)
    if character.mood_dict['sad'] >= 80 :
        return emote_loop(character, zl.sad_list)
    if character.mood_dict['sad'] <= 20 :
        return emote_loop(character, zl.happy_list)
    if character.mood_dict['greedy'] >= 80 :
        return emote_loop(character, zl.greedy_list)
    if character.mood_dict['greedy'] <= 20 :
        return emote_loop(character, zl.philanthropy_list)


def emote_loop(character, emote_list) :
    while (character.mood_dict['angry'] >= 80 or character.mood_dict['angry'] <= 20 or character.mood_dict[
        'sad'] >= 80 or character.mood_dict['sad'] <= 20 or character.mood_dict['greedy'] >= 80 or character.mood_dict[
               'greedy'] <= 20 or character.mood_dict['reckless'] >= 80 or character.mood_dict['reckless'] <= 20) :
        comment = (get_current_time_hhmmss() + ': ' + random_activity(emote_list, character))
        update_variable_list(comment)
        # Printing of character.mood_dict is used to test mood change. Remove.
        # print(character.mood_dict)
        # Count is used to test length of loop. Remove.
        # count = +1
        # Count is used to test length of loop. Remove.
        if character.mood_dict['angry'] <= 0 :
            comment = (get_current_time_hhmmss() + ': ' + character.first_name + ' has met a chill end')
            update_variable_list(comment)
            # print(count)
            break
        elif character.mood_dict['angry'] > 100 :
            comment = (get_current_time_hhmmss() + ': ' + character.first_name + ' has met an angry end')
            update_variable_list(comment)
            # print(count)
            break
        elif character.mood_dict['sad'] <= 0 :
            comment = (get_current_time_hhmmss() + ': ' + character.first_name + ' has met a happy end')
            update_variable_list(comment)
            # print(count)
            break
        elif character.mood_dict['sad'] > 100 :
            comment = (get_current_time_hhmmss() + ': ' + character.first_name + ' has met a sad end')
            update_variable_list(comment)
            # print(count)
            break
        elif character.mood_dict['greedy'] <= 0 :
            comment = (get_current_time_hhmmss() + ': ' + character.first_name + ' has met a giving end')
            update_variable_list(comment)
            # print(count)
            break
        elif character.mood_dict['greedy'] > 100 :
            comment = (get_current_time_hhmmss() + ': ' + character.first_name + ' has met a greedy end')
            update_variable_list(comment)
            # print(count)
            break
        elif character.mood_dict['reckless'] <= 0 :
            comment = (get_current_time_hhmmss() + ': ' + character.first_name + ' has met a careful end')
            update_variable_list(comment)
            # print(count)
            break
        elif character.mood_dict['reckless'] > 100 :
            comment = (get_current_time_hhmmss() + ': ' + character.first_name + ' has met a reckless end')
            update_variable_list(comment)
            # print(count)
            break
        else :
            time.sleep((random.randint(41, 150)) / 240)
            space_loop(character)
    print(character.__dict__)


'''Classes:
    Ship
    Character
    NPC
    '''


class Ship :
    def __init__(self, value) :
        self.value = value
        self.ship_name = random.choice(zl.ship_names)
        self.max_health = value * random.randint(80, 100)
        self.current_health = round(self.max_health * random.uniform(.5, 1), 0)
        self.NPC_List = create_npc_list(self.ship_name, value)


class Character :
    def __init__(self, name) :
        self.first_name = name
        self.last_name = ''
        self.mood_dict = create_random_dict(['angry', 'sad', 'reckless', 'greedy'], (30, 70))
        self.stats_dict = create_random_dict(['intelligence', 'charisma', 'speed'], (40, 75))
        self.wealth = random.randint(1000, 3000)
        self.gender = random.choice(zl.gender)
        self.article = gender_article(self.gender)
        self.ship = Ship(1)
        self.job = random.choice(zl.job_list)
        print(f'You suddenly find yourself forcibly compressed into a tiny space.'
              f'\nYou are now cohabitating {self.first_name}\'s brain.'
              f'\n{upper(self.gender)} {self.article} the {self.job} of the {self.ship.ship_name} '
              f'and {self.article} currently flying in deep space.')


my_character = None


def create_character_from_user_input() :
    """
    Creates an instance of Character based on user input.

    Returns:
    An instance of Character in a global variable.
    """
    name = random_name(zl.first_names, zl.last_names)
    global my_character
    my_character = Character(name)
    return my_character


class NPC :
    def __init__(self, location, job_list) :
        """
        Creates an NPC with characteristics and adds it to the NPC dictionary.

        Args:
            location: The current location of the NPC.
            job_list: A list of possible jobs for the NPC.

        Returns:
            A dictionary containing the NPC information.
        """

        self.first_name = random.choice(zl.first_names)
        self.last_name = random.choice(zl.last_names)
        self.job = random.choice(job_list)
        self.relationship = random.randint(-10, 10)  # Initial relationship value
        self.mood_dict = create_random_dict(['angry', 'sad', 'reckless', 'greedy'], (40, 60))
        self.stats_dict = create_random_dict(['intelligence', 'charisma', 'speed'], (40, 75))
        self.wealth = random.randint(-1000, 10000)
        self.location = location
        self.relationship = random.randint(-10, 10)
        self.gender = random.choice(zl.gender)
        self.article = gender_article(self.gender)
