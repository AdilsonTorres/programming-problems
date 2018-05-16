
songs = {
    0: 'PROXYCITY',
    1: 'P.Y.N.G.',
    2: 'DNSUEY!',
    3: 'SERVERS',
    4: 'HOST!',
    5: 'CRIPTONIZE',
    6: 'OFFLINE DAY',
    7: 'SALT',
    8: 'ANSWER!',
    9: 'RAR?',
    10: 'WIFI ANTENNAS',
}

N = int(input())

for i in range(N):
    x, y = map(int, input().strip().split(' '))
    print(songs[x+y])