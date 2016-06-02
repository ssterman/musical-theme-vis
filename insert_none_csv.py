import csv
import string

SONG_LENGTH = 3
SONG_NUMBER = 1
SONG_START = 4

THEME_START = 4
THEME_END = 5
THEME_SONG_NUMBER = 7

def filter_themes(themes, song_number):
	result = []
	for row in themes:
		if row[THEME_SONG_NUMBER] == song_number:
			result.append(row)
	return result

def none_entry(start_time, end_time, song):
	length = end_time - start_time
	total_start_seconds = song[SONG_START] + start_time
	return ["none", "", "", "", start_time, end_time, length, song[SONG_NUMBER], total_start_seconds, "", ""]

songs_file = open('songs.csv')
songs_csv_file = csv.reader(songs_file)

themes_file = open('musical_themes.csv')
themes_csv_file = csv.reader(themes_file)

songs = []
songs_csv_file.next() # skip first header line
for row in songs_csv_file:
	new_row = []
	for item in row:
		try:
			new_row.append(int(item))
		except ValueError:
			new_row.append(item)
	songs.append(new_row)

themes = []
themes_csv_file.next() # skip first header line
for row in themes_csv_file:
	new_row = []
	for item in row:
		try:
			new_row.append(int(item))
		except ValueError:
			new_row.append(item)

	themes.append(new_row)

new_themes = []

for song in songs:
	song_themes = filter_themes(themes, song[SONG_NUMBER])

	new_themes.append(none_entry(0, song[SONG_LENGTH], song))

	# # if no themes present, add space for the length of the song
	if len(song_themes) == 0:
		# new_themes.append(none_entry(0, song[SONG_LENGTH], song))
		continue

	# # if first theme doesn't start at 0, add space at beginning of song
	# first_theme_start = song_themes[0][THEME_START] 
	# if first_theme_start != 0:
	# 	new_themes.append(none_entry(0, first_theme_start - 1, song))

	# curr_end = first_theme_start

	for theme in song_themes:
		# theme_start = theme[THEME_START]
		# if theme_start > curr_end + 1:
		# 	new_themes.append(none_entry(curr_end + 1, theme_start - 1, song))

		new_themes.append(theme)

		# theme_end = theme[THEME_END]
		# if theme_end > curr_end:
		# 	curr_end = theme_end

    # if last theme doesn't end at end of song, add space at end of song
	# last_theme_end = song_themes[len(song_themes) - 1][THEME_END]
	# if last_theme_end != song[SONG_LENGTH]:
	# 	new_themes.append(none_entry(last_theme_end, song[SONG_LENGTH], song))

print new_themes
with open("output.csv", "wb") as f:
	writer = csv.writer(f)
	writer.writerow(["theme_name","song_name","start_timestamp","end_timestamp","start_sec","end_sec","length_sec","song_number","total_start_sec","song_url","lyrics"])
	writer.writerows(new_themes)

just_themes = []
for theme in themes:
	if theme[0] not in just_themes:
		just_themes.append(theme[0])
print just_themes

