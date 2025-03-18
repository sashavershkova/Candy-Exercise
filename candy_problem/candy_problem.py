def get_friends_favorite_candy_count(favorites):
    candies_count = {}

    for friend in favorites:
        for candy in friend[1]:
            if candy in candies_count:
                candies_count[candy] += 1
            else:
                candies_count[candy] = 1

    return candies_count

def create_new_candy_data_structure(data):
    candies_people_dict = {}
    
    for friend_fav in data:
        for candy in friend_fav[1]:
            candies_people_dict[candy] = []
    
    for candy in candies_people_dict:
        for friend_fav in data:
            if candy in friend_fav[1]:
                candies_people_dict[candy].append(friend_fav[0])
    
    return candies_people_dict

def get_friends_who_like_specific_candy(data, candy_name):
    candies_people_dict = create_new_candy_data_structure(data)
    for candy in candies_people_dict:
        if candy == candy_name:
            return tuple(candies_people_dict[candy])

def create_candy_set(data):
    candy_set = set()
    for friend_fav in data:
        for candy in friend_fav[1]:
            candy_set.add(candy)
    return candy_set


