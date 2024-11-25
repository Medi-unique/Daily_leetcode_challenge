class Solution:
  def slidingPuzzle(self, board: List[List[int]]) -> int:
    start = ''.join(str(num) for row in board for num in row)
    target = "123450"

    moves = {0: [1, 3], 1: [0, 2, 4], 2: [1, 5],
             3: [0, 4], 4: [1, 3, 5], 5: [2, 4]}

    queue = deque([(start, 0)]) 
    visited = set()
    while queue:
        state, moves_made = queue.popleft()

        if state == target:
            return moves_made

        zero_pos = state.index('0')
        for next_pos in moves[zero_pos]:

            nextState = list(state)
            nextState[zero_pos], nextState[next_pos] = nextState[next_pos], nextState[zero_pos]
            
            new_state = ''.join(nextState)
            if new_state not in visited:
                visited.add(new_state)
                queue.append((new_state, moves_made + 1))
                
    return -1