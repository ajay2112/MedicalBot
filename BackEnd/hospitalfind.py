from googleplaces import GooglePlaces, types


def hospitalfind(my_input) :
    YOUR_API_KEY = 'AIzaSyDuy19nMwHBvLvgkg9upGZkex9jqriWkQ0'

    google_places = GooglePlaces(YOUR_API_KEY)

    query_result = google_places.nearby_search(
        location=my_input, keyword='hospital',
        radius=2000, types=[types.TYPE_HOSPITAL])

    strr = " "
    flag = 0
    for place in query_result.places:
        place.get_details()
        strr = strr + "\n Name :" + (str(place.name).upper()) + "\n Address:" + str(place.formatted_address) + "\n Phone Number :" + (str(place.international_phone_number).upper()) + "\n Map Url :" + str(place.url) + "\n Web Link :" + str(place.website) + "\n Ratings:" + str(place.rating) +"\n"+("_"*50)+"\n"

        flag = flag+1
        if flag == 5:
            break

    return strr
    #returns nearby Pharmacy
    # dependency : python-google-places 1.4.1
