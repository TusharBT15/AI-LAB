src = [1, 2, 3, -1, 4, 5, 6, 7, 8]
target = [1, 2, 3, 4, 5, -1, 6, 7, 8]


def iddfs(src, target, depth):
    for limit in range(0, depth+1):
        visited_states = []
        visited_states.append(src)
        if dfs(src, target, limit, visited_states):
            print(visited_states)
            return True
    return False


def gen(state, m, b):
    temp = state[:]
    if m == 'l':
        temp[b], temp[b-1] = temp[b-1], temp[b]
    if m == 'r':
        temp[b], temp[b+1] = temp[b+1], temp[b]
    if m == 'd':
        temp[b], temp[b+3] = temp[b+3], temp[b]
    if m == 'u':
        temp[b], temp[b-3] = temp[b-3], temp[b]
    return temp


def next_state(state):
    blank = state.index(-1)
    moves = []
    if blank >= 3:
        moves.append('u')
    if blank <= 5:
        moves.append('d')
    if (blank % 3) > 0:
        moves.append('l')
    if (blank % 3) < 2:
        moves.append('r')
    return moves, blank


def dfs(src, target, limit, visited_states):
    if src == target:
        return True
    if limit <= 0:
        return False
    moves, blank = next_state(src)
    for move in moves:
        nextmove = gen(src, move, blank)
        if not nextmove in visited_states:
            visited_states.append(nextmove)
            if dfs(nextmove, target, limit-1, visited_states):
                return True
    return False


print(iddfs(src, target, 2))


