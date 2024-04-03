def eggs_solution(breaks):
    if breaks(50):
        for i in range(1,51):
            if breaks(i):
                return i - 1
    else: 
        if breaks(75):
            for i in range(51,76):
                if breaks (i):
                    return i-1
        else:
            if breaks(87):
                for i in range(76,88):
                    if breaks (i):
                        return i-1
            else:
                if breaks(94):
                    for i in range(88,95):
                        if breaks (i):
                            return i-1
                else:
                    if breaks(97):
                        for i in range(95,98):
                            if breaks (i):
                                return i-1
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

