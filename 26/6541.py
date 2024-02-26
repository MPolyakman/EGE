f = open('6541.txt')
k, cnt_of_guests = map(int, f.readline().split())
guests = [list(map(int,guest.split())) for guest in f]
timeline = [0]*1000
for time in guests:
    for hour in range(time[0],time[1]+1):
        timeline[hour] += 1
print(max(timeline)/k)
print(timeline[max(guests)[0]+1])
