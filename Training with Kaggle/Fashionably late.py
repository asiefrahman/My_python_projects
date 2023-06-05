
def fash_late(arrivals, guests):
    if arrivals.index(guests) > len(arrivals)/2 and arrivals.index(guests) < len(arrivals)-1:
        return True

arrivals = ['jodu', 'modhu', 'ram', 'sham', 'kodu', 'aam', 'jam']
guests = 'aam'

print(fash_late(arrivals, guests))