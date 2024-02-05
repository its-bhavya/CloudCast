from toolkit import get_tables


def init(m):
    predicted, actual = get_tables()
    offset = 0
    workb = []
    for i in range(30):
        workb.append(abs(predicted[i][1]-actual[i][1]))
        workb.append(abs(predicted[i][2]-actual[i][2]))
        workb.append(abs(predicted[i][3]-actual[i][3]))
        offset += workb[-1]+workb[-2]+workb[-3]
    workb.sort(reverse=True)
    optimal = offset
    for x in workb[:m]:
        optimal -= x
    scale = offset - optimal
    return offset, scale

def judge(offset, scale, diff):
    score = ((diff-offset)/scale) * 100
    return round(score)
