import pytest
from candy_problem.candy_problem import * 


def test_create_candy_data_structure_type():
    # Arrange
    friend_favorites = [
        ["Sally", [ "lollipop", "bubble gum", "laffy taffy"]],
        [ "Bob", ["milky way", "licorice", "lollipop"]],
        [ "Arlene", ["chocolate bar", "milky way", "laffy taffy"]],
        [ "Carlie", ["nerds", "sour patch kids", "laffy taffy"]]
    ]
    candy_name = "lollipop"

    # Act
    new_candy_data_1 = get_friends_favorite_candy_count(friend_favorites)
    new_candy_data_2 = create_new_candy_data_structure(friend_favorites)
    new_candy_data_3 = get_friends_who_like_specific_candy(friend_favorites, candy_name)
    new_candy_data_4 = create_candy_set(friend_favorites)

    # Assert
    assert type(new_candy_data_1) == dict
    assert type(new_candy_data_2) == dict
    assert type(new_candy_data_3) == tuple
    assert type(new_candy_data_4) == set


# Add your own assertions to the test below
def test_create_candy_data_structure_values():

    # Arrange
    friend_favorites = [
        ["Sally", [ "lollipop", "bubble gum", "laffy taffy"]],
        [ "Bob", ["milky way", "licorice", "lollipop"]],
        [ "Arlene", ["chocolate bar", "milky way", "laffy taffy"]],
        [ "Carlie", ["nerds", "sour patch kids", "laffy taffy"]]
    ]

    candy_name = "lollipop"

    # Act
    new_candy_data_1 = create_new_candy_data_structure(friend_favorites)
    new_candy_data_2 = get_friends_favorite_candy_count(friend_favorites)
    new_candy_data_3 = get_friends_who_like_specific_candy(friend_favorites, candy_name)
    new_candy_data_4 = create_candy_set(friend_favorites)


    # Assert
    assert len(new_candy_data_1) == 8
    assert new_candy_data_2 == {
        "lollipop" : 2,
        "bubble gum": 1,
        "laffy taffy": 3,
        "milky way": 2,
        "licorice": 1,
        "chocolate bar": 1,
        "nerds": 1,
        "sour patch kids": 1
    }
    assert new_candy_data_3 == ("Sally", "Bob")
    assert new_candy_data_4 == {"lollipop", "bubble gum", "laffy taffy", 
                                "milky way", "licorice", "chocolate bar",
                                "nerds", "sour patch kids"}


'''
5. 
Starting with nominal cases, write tests for each of the functions 
in the file tests/test_candy_data_structure.py then write tests to 
handle edge cases.
'''