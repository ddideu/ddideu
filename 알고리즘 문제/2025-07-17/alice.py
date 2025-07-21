friend = int(input())
friend_tracks = list(map(str,input().split()))
my_track = str(input())
cnt = 0
for track in friend_tracks:
    if track == my_track:
        cnt += 1

print(cnt)