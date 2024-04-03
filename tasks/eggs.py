def eggs_solution(breaks):
    if breaks(50):
        for i in range(1,49):
            if breaks(i):
                return i - 1
            else:
                return 49
    else: 
        if breaks(75):
            for i in range(51,74):
                if breaks (i):
                    return i-1
                else:
                    return 74
        else:
            if breaks(87):
                for i in range(76,86):
                    if breaks (i):
                        return i-1
                    else:
                        return 86
            else:
                if breaks(94):
                    for i in range(88,93):
                        if breaks (i):
                            return i-1
                        else:
                            return 93
                else:
                    if breaks(97):
                        for i in range(95,96):
                            if breaks (i):
                                return i-1
                            else:
                                return 96
                    else:
                        if breaks(99):
                            if breaks(98):
                                return 97
                            else:
                                return 98
                        else:
                            if breaks(100):
                                return 99
                            else:
                                return 100

