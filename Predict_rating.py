import pickle
import pandas as pd

loaded_model = pickle.load(open('finalized_model.sav', 'rb'))

def map_yes_no_binary(var) :
    val = str(var).lower()
    if val == "yes" or val == "ye" or val == "y":
        return 1
    else :
        return 0

print("\n==============================")
print("Welcome to Rating Predictor")
print("============================== \n")

print("This app will let you predict your Airbnb rating, based on data collected over listings from Seattle \n \n")

host_is_superhost = input("Are you a superhost? [y/n] :")
host_is_superhost = int(map_yes_no_binary(host_is_superhost))

accommodates = int(input("\nHow many people can you accommodate? :"))

bathrooms = float(input("\nHow many bathrooms? :"))

bedrooms = float(input("\nHow many bedrooms? :"))

beds = float(input("\nHow many beds? :"))

price = float(input("\nWhat's the price per night? $"))

cleaning_fee = float(input("\nWhat's the cleaning fee? $"))

instant_bookable = input("\nInstant bookable? [y/n] :")
instant_bookable = int(map_yes_no_binary(instant_bookable))

is_proper_house = input("\nIs the property a House, Apartment, Touwnhouse, Condominium, Bungalow, Loft? [y/n] :")
is_proper_house = int(map_yes_no_binary(is_proper_house))

is_proper_bed = input("\nIs the bed a proper bed? [y/n] :")
is_proper_bed = int(map_yes_no_binary(is_proper_bed))

is_private_room = input("\nIs it a private room? [y/n] :")
is_private_room = int(map_yes_no_binary(is_private_room))

number_amenities = int(input("\nNumber of amenities? "))

description = str(input("\nDescription of your property :"))
description_length = len(description)

cols = ['host_is_superhost', 'accommodates', 'bathrooms',
        'bedrooms', 'beds', 'price', 'cleaning_fee', 'instant_bookable',
        'is_proper_house', 'is_proper_bed', 'is_private_room','number_amenities', 'description_length']
frame_pd = pd.DataFrame(columns = cols)

frame_pd = frame_pd.append({'host_is_superhost': host_is_superhost, 'accommodates': accommodates, 'bathrooms': bathrooms,
                 'bedrooms': bedrooms, 'beds': beds, 'price': price, 'cleaning_fee': cleaning_fee,
                 'instant_bookable': instant_bookable, 'is_proper_house': is_proper_house, 'is_proper_bed': is_proper_bed,
                 'is_private_room': is_private_room, 'number_amenities': number_amenities, 'description_length': description_length}, ignore_index = True)
rating = loaded_model.predict(frame_pd)
if float(rating[0]) > 100.0 :
    rating[0] = 100.0

print("\n\nYour expected Airbnb rating is " + str(rating[0]) + " out of 100")
