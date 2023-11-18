#8-6. City Names

print("\n --- Cities ---")
def city_country(city, country):
    output = f'"{city.title()}, {country.title()}"'

    return output

place = city_country('accra', 'ghana')
print(place)

place = city_country('paris', 'france')
print(place)

place = city_country('barcelona', 'spain')
print(place)


#8-7. Album

print("\n --- Music Albums ---")
def make_album(artist_name, album_title, num_of_songs=None):
    album = {'artist': artist_name, 'title': album_title}

    if num_of_songs:
        album['no. of songs'] = num_of_songs

    return album

music_album = make_album('sia', 'this is acting')
print(music_album)

music_album = make_album('rihanna', 'unapologetic')
print(music_album)

music_album = make_album('adele', '30')
print(music_album)

music_album = make_album('alicia keys', 'girl on fire', 5)
print(music_album)


#8-8. User Albums

def make_album(artist_name, album_title):
    album = {'artist': artist_name, 'title': album_title}
    return album

while True:
    print("\nEnter an album's artist and title")
    print("(Enter 'q' to quit)")

    artist = input("Artist: ")
    if artist == 'q':
        break

    title = input("Title: ")
    if title == 'q':
        break

    music_album = make_album(artist, title)
    print(music_album)