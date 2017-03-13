import random as rand

"""
generate questions according to the parameters
    count: number of questions
    threshold: upper value of results
"""


def genqs(count, threshold, ops):
    questions = {}
    c = 0
    while len(questions) < count:
        q, r = genq(threshold, ops)
        questions[q] = r
    return questions


def genq(threshold, ops):
    ok = False
    l = len(ops)
    op = rand.randint(0, l - 1)
    while not ok:
        n1 = rand.randint(0, threshold)
        n2 = rand.randint(0, threshold)
        q = str(n1) + ops[op] + str(n2)
        if ops[op] == '/':
            if n2 < 2 or n1 % n2 or n1 == n2 or n1 == 0:
                continue
        if ops[op] == '*':
            if n1 < 2 or n2 < 2:
                continue
        r = eval(q)
        if 0 <= r <= threshold:
            ok = True
    return q, r


if __name__ == "__main__":
    count = 100
    threshold = 20
    operations = ['+', '-']
    questions = genqs(count, threshold, operations)
    for k,v in questions.iteritems():
        print("%s = %d" % (k, v))
