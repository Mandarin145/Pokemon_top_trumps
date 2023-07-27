import random
import requests

def pokemon_id():
    # function to generate multiple random pokemon ID & info
    # Kanto, Johto, Hoenn, Sinnoh only

    # creating an empty list to store the dictionaries returned from the API into
    # lists have square brackets []
    pokemon_list = []

    # to select 8 random numbers in the range between 1-491
    # this method prevents the numbers from being repeated 100%, so the player and opponent can't have the same pokemon
    # and the same pokemon can't be selected in player or opponent's hands
    # random.choice is pick 1 thing, random.sample is get a list back
    random_numbers = random.sample(range(1, 491), 8)
    for number in random_numbers:
        # old code pokemon_number = random.randint(1, 491)

    # getting info from Pokemon API
    # f before quotation mark is the same as .format{} at the end
    # url = 'https://pokeapi.co/api/v2/pokemon/{}/'.format(pokemon_number) would also work

        url = f'https://pokeapi.co/api/v2/pokemon/{number}/'

    # the requests.get gets the information from the API url
        response = requests.get(url)

    # to check response from website, see dog link
    # .json gets the useful information into python???
        pokemon = response.json()

    # creating dictionary from API, assigned to variable pokemon_dictionary as there is more than one pokemon
    # dictionaries have curly brackets {}
    # so each time the loop iterates it will assign the dictionary (stats) for that pokemon to the variable 'pokemon_dictionary'
    # which is then saved into the loop using the list.append
        pokemon_dictionary = {
            'ID': pokemon['id'],
            'name': pokemon['name'],
            'height': pokemon['height'],
            'weight': pokemon['weight'],
            'pokemon_type': pokemon['types'][0]['type']['name']
        }
    # adding this dictionary into the list
    # since list.append can only append one item, I had to assign all of the data to the variable
        pokemon_list.append(pokemon_dictionary)

    # return pokemon list to save it to whatever calls the function
    # in this case, it will save pokemon lists to variables 'player_pokemon' and 'opponent_pokemon'

    # print(response)
    return pokemon_list


# created a new function to run the game
def game():

# assigning pokemon to player and computer
# running pokemon_id to create 1 list - which selects 8 random pokemon
# assigns 1st 4 in list to player and 2nd 4 in list to opponent, list slicing
# 1st value in brackets is the 1st you want to pull from the list, last value is the value AFTER the last value you want
# e.g. [2:5] will pull index 2,3,4 (3rd, 4th, 5th values)
# if you are slicing from the 1st value, you can just put [:x], where there is no need for 0
# similarly if you are slicing until the last value, you can just put [x:] and not fill in the final value
# here player_pokemon = index 0,1,2,3, opponent_pokemon = index 4,5,6,7
# position 8 does not actually exist (only selected 8 random pokemon & position 8 would be 9th pokemon)
    eight_pokemon = pokemon_id()
    player_pokemon = eight_pokemon[:4]
    opponent_pokemon = eight_pokemon[4:]

# player choosing their pokemon
# calling first from list (number ref, counting from 0) and then from dictionary (words)
    player_pokemon_choice = input(f"Choose your Pokemon: {player_pokemon[0]['name']}, {player_pokemon[1]['name']}, {player_pokemon[2]['name']}, {player_pokemon[3]['name']} (0,1,2,3)")
# assigning pokemon from list based on player choice
    my_pokemon = player_pokemon[int(player_pokemon_choice)]
    my_pokemon_name = my_pokemon['name']
    print(f"You chose {my_pokemon['name']}!")

# alternative code to call from list and get player choice of Pokemon
# different method for print and input based on their syntax
    # print("Choose your Pokemon:", player_pokemon[0]['name'], ",", player_pokemon[1]['name'], ",",
    #       player_pokemon[2]['name'], "or", player_pokemon[3]['name'])
    # player_choice = input("Player choice? (1, 2, 3 or 4)")


# old opponent choosing pokemon from the 4 already randomly picked in pokemon_id
# old random pokemon selected using random integer generation & counting from list
#     old opponent_pokemon_choice = random.randint(0, 3)
# old assigning pokemon based on random choice and calling from list
#     old opp_pokemon = opponent_pokemon[opponent_pokemon_choice]


    # assigning pokemon to opponent based on the list of 4 options
    # using a random choice on the 4 options
    opp_pokemon = random.choice(opponent_pokemon)
    opp_pokemon_name = opp_pokemon['name']
    print(f"Opponent chose {opp_pokemon['name']}!")


# assigning variables pokemon type rock paper scissors with fire, water, grass
# so i can return this information to be used in a different function
# need inverted commas when calling from dictionary!!
    my_pokemon_type = my_pokemon['pokemon_type']
    opponent_pokemon_type = opp_pokemon['pokemon_type']


# player choosing their stat
# while loop to prevent code from breaking if incorrect entry is typed (e.g. typo)
    valid_input = False
    while not valid_input:
        player_stat_choice = input("Choose your stat: ID, height, weight")
        if player_stat_choice == 'ID' or player_stat_choice == 'height' or player_stat_choice == 'weight':
                valid_input = True
        else:
            print('We do not understand, please choose ID, height or weight')

# assigning stat based on player choice calling from dictionary
    my_stat = my_pokemon[player_stat_choice]

# assigning stat to opponent based on player choice and calling from dictionary
    opponent_stat = opp_pokemon[player_stat_choice]

    # if clause to determine winner
    if my_stat > opponent_stat:
        print("Your stat:", my_stat)
        print("Opponent stat:", opponent_stat)
        print("You win!")
        return 'win', my_pokemon_type, opponent_pokemon_type, my_pokemon_name, opp_pokemon_name
    # need to return the pokemon types and names so I can reuse them in the type battle
    # save the output into new variables in the script to run both game functions
    elif my_stat < opponent_stat:
        print("Your stat:", my_stat)
        print("Opponent stat:", opponent_stat)
        print("You lose!")
        return 'loss', my_pokemon_type, opponent_pokemon_type, my_pokemon_name, opp_pokemon_name
    else:
        print("Your stat:", my_stat)
        print("Opponent stat:", opponent_stat)
        print("Draw!")
        return 'draw', my_pokemon_type, opponent_pokemon_type, my_pokemon_name, opp_pokemon_name




# separate function for type battle
# so it runs after the top trumps game
# as otherwise return will kill the code
def type_battle():

# while loop to continue running the 'rock, paper, scissors' game if you put a silly response in
    valid_input = False
    while not valid_input:
# pokemon type rock paper scissors with fire, water, grass
# only executes if player pokemon == water, grass or fire
# don't forget inverted commas!
    # need separate inclusion of my_pokemon_type for each 'or'
    # while loop needs to be after the input
    # otherwise the input is not being updated, and the else clause will repeat indefinitely as the if/elif are not being met
    # therefore it was permanently not matching the criteria valid_input = false, so was looping indefinitely
    # because the while loop started after the input
        if (my_pokemon_type == 'fire' or my_pokemon_type == 'water' or my_pokemon_type == 'grass') and (opponent_pokemon_type == 'fire' or opponent_pokemon_type == 'water' or opponent_pokemon_type == 'grass'):
            selection = input('Bonus round! Do you want to play Pokemon Type Battle (!) ? (Y/N)')
            if selection == 'Y':
                print(f"{my_pokemon_name} type is {my_pokemon_type}, {opp_pokemon_name} type is {opponent_pokemon_type}")
                valid_input = True
                if my_pokemon_type == 'fire' and opponent_pokemon_type == 'grass':
                    print('You win!')
                    return 'win'
                elif my_pokemon_type == 'grass' and opponent_pokemon_type == 'water':
                    print('You win!')
                    return 'win'
                elif my_pokemon_type == 'water' and opponent_pokemon_type == 'fire':
                    print('You win!')
                    return 'win'
                elif my_pokemon_type == opponent_pokemon_type:
                    print("It's a draw!")
                    return 'draw'
                else:
                    print('You lose!')
                    return 'lose'
            elif selection == 'N':
                valid_input = True
                print("Wrong answer! Game Over!")
                # exit(0) terminates the code with exit code 0, i.e. no errors
                # stops the whole code from continuing
                exit(0)
            else:
                print("We do not understand, please answer Y or N")
        else:
            valid_input = True
            print("No bonus round this time :(")
            return 'no bonus round'

# now creating empty list to store results in
list_of_results_1 = []
list_of_results_2 = []

# for loop to run game 3 times
# and then store results in separate file
# will store all results including type battle
for number in range(3):
    result_of_game_1 = game()

    # following lines calling from the list that I return in game 1
    # and assigning answers to variables that are used in game 2
    # this way it uses the information from the original pokemon selected
    my_pokemon_type = result_of_game_1[1]
    opponent_pokemon_type = result_of_game_1[2]
    my_pokemon_name = result_of_game_1[3]
    opp_pokemon_name = result_of_game_1[4]

    # running type battle code, which will use the variables assigned above
    result_of_game_2 = type_battle()

    # saving results of top trumps
    # it is only saving the actual game results by appending reference [0], and not the pokemon names or types
    list_of_results_1.append(result_of_game_1[0])
    # saving results of type battle
    list_of_results_2.append(result_of_game_2)
print("Results:", "Top Trumps", list_of_results_1, "Type Battle", list_of_results_2)
filename = 'pokemon_game_log.txt'
with open(filename, 'a') as file_object:
    file_object.write(f'\n{list_of_results_1}\n')
    file_object.write(f'\n{list_of_results_2}\n')






# type rock paper scissors - if type is fire or water or grass, and opponent type is fire water or grass, then play
# can we also import the second type???
# high scores file - write to a file of the scores, if you win you get 3 points, lose 1 point, draw 2 points
# so when you have results at the end it will have scores & save those to the file