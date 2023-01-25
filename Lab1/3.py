st_hr,st_min,ed_hr,ed_min = input().split()

park_time = abs((int(ed_hr) - int(st_hr)) * 60 + (int(ed_min) - int(st_min)))

ans = 0

print(park_time)

if(park_time <= 15):
    print(ans)
elif(park_time <= 180):
    while(park_time > 0):
        ans += 10
        park_time -= 60
    print(ans)
elif(park_time <= 360):
    park_time -= 180
    ans += 30
    while(park_time > 0):
        ans += 20
        park_time -= 60
    print(ans)
elif(park_time > 360):
    ans += 200
    print(ans)