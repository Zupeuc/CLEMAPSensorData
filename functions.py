

def combination(data, number, letter):

    x = data["time"]

    p1 = data["l1_p"]
    p2 = data["l2_p"]
    p3 = data["l3_p"]

    q1 = data["l1_q"]
    q2 = data["l2_q"]
    q3 = data["l3_q"]

    i1 = data["l1_i"]
    i2 = data["l2_i"]
    i3 = data["l3_i"]

    v1 = data["l1_v"]
    v2 = data["l2_v"]
    v3 = data["l3_v"]

    # fig, ax = plt.subplots()
    if letter == "p":
        if number == 1:
            return x, p1

        if number == 12:
            return x, p1, p2

        if number == 13:
            return x, p1, p3

        if number == 2:
            return x, p2

        if number == 23:
            return x, p2, p3

        if number == 3:
            return x, p3

        if number == 123:
            return x, p1, p2, p3

    if letter == "q":
        if number == 1:
            return x, q1

        if number == 12:
            return x, q1, q2

        if number == 13:
            return x, q1, q3

        if number == 2:
            return x, q2

        if number == 23:
            return x, q2, q3

        if number == 3:
            return x, q3

        if number == 123:
            return x, q1, q2, q3

    if letter == "i":
        if number == 1:
            return x, i1

        if number == 12:
            return x, i1, i2

        if number == 13:
            return x, i1, i3

        if number == 2:
            return x, i2

        if number == 23:
            return x, i2, i3

        if number == 3:
            return x, i3

        if number == 123:
            return x, i1, i2, i3

    if letter == "v":
        if number == 1:
            return x, v1

        if number == 12:
            return x, v1, v2

        if number == 13:
            return x, v1, v3

        if number == 2:
            return x, v2

        if number == 23:
            return x, v2, v3

        if number == 3:
            return x, v3

        if number == 123:
            return x, v1, v2, v3


def extreme_outlier(dataframe, value):
    for previous, current in zip(dataframe, dataframe[1:]):
        if current > value:
            dataframe = dataframe.replace(current, previous)
    return dataframe

