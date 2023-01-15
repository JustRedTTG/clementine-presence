import threading, sys
from hexicapi.save import save, load
import time, pypresence, oauth
from clementineremote import ClementineRemote

c = ClementineRemote()
p = pypresence.Presence(oauth.client_id)
p.connect()
s = time.time()-c.track_position
e = s+c.current_track['length']
def update(title: str = "song title", album: str = "album", current_track: int = 1, out_of_tracks: int = 2):
	global s, e
	p.update(
		details=title,
		large_image="clementine",
		small_image="logo",
		state=album,
		start=s,
		end=e,
		party_id=":)",
		party_size=[current_track, out_of_tracks]
	)

track = c.current_track['track_id']
tracks = int(input("how many tracks: "))

while True:
	if track != c.current_track['track_id']:
		track = c.current_track['track_id']
		s = time.time() - c.track_position
		e = s + c.current_track['length']
	update(c.current_track['title'], c.current_track['track_album'], c.current_track['track'], tracks)
	try:
		time.sleep(5)
	except KeyboardInterrupt:
		c.disconnect()
		break