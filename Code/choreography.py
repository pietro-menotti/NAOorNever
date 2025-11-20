from aima.search import *
from position import *
import random

pos = {k: v for k, v in POSITION.items() if v < 9 or k == 'Stand_from_sit'}
man_pos = MANDATORY_POSITION

VALID_TRANSITIONS = {
    "Stand": ["Mani_sui_fianchi", "Ballo_braccia",
                "Diagonal_left", "DanceMove",
                 'Move_backward', "Move_forward", "AirGuitar",
                "ComeOn", "Dab", "PulpFiction", "TheRobot",],
    "StandInit": ["Arms_opening", "Diagonal_right","Mani_sui_fianchi", "Ballo_braccia",
                  'Move_backward', "Move_forward", "AirGuitar",
                  "ComeOn", "Dab", "DanceMove", "PulpFiction", "TheRobot"],
    "StandZero": ["Arms_opening", "Diagonal_right","Mani_sui_fianchi", "Ballo_braccia",
                  'Move_backward', "Move_forward", "AirGuitar",
                  "ComeOn", "Dab", "DanceMove", "PulpFiction", "TheRobot"],
    "Hello": ["Arms_opening", "Diagonal_right","Mani_sui_fianchi", "Ballo_braccia",
                  'Move_backward', "Move_forward", "AirGuitar",
                  "ComeOn", "Dab", "DanceMove", "PulpFiction", "TheRobot"],
    "Wipe_Forehead": ["Arms_opening", "Diagonal_left", "Diagonal_right",
                       'Move_backward', "Move_forward", "AirGuitar",
                       "ComeOn", "Dab", "DanceMove", "PulpFiction", "TheRobot",
                       "Mani_sui_fianchi", "Ballo_braccia"],
    "Sit": ["Stand_from_sit"],
    "SitRelax": ["Stand_from_sit"],
    "Stand_from_sit": list(pos.keys()),
    "Crouch": ["Stand"],
    'Arms_opening': list(man_pos.keys()),
    'Diagonal_left': list(man_pos.keys()),
    'Diagonal_right': list(man_pos.keys()),
    'Move_backward': list(man_pos.keys()),
    'Move_forward': list(man_pos.keys()),
    'Union_arms': list(man_pos.keys()),
    'AirGuitar': list(man_pos.keys()),
    'ComeOn': list(man_pos.keys()),
    'Dab': list(man_pos.keys()),
    'DanceMove': list(man_pos.keys()),
    'PulpFiction': list(man_pos.keys()),
    'TheRobot': list(man_pos.keys()),
    'Mani_sui_fianchi': list(man_pos.keys()),
    'Ballo_braccia': list(man_pos.keys()),
}

def is_valid_transition(p_from, p_to):
    """
    Check if the transition is valid given the VALID_TRANSITIONS 'table'.
    """
    return p_to in VALID_TRANSITIONS.get(p_from, [])


class Choreography(Problem):

    def __init__(self, initial, goal, available_moves):
        self.available_moves = list(available_moves)
        self.initial = (initial, (initial,))
        self.goal = (goal, ())
        super().__init__(self.initial, self.goal)

    def actions(self, state):
        position, moves = state

        # We force the robot to stand whenever is sitting
        if position in ("Sit", "SitRelax") and "Stand_from_sit" not in moves:
            return [(position, "Stand_from_sit")]

        # Optional moves remaining
        remaining = [m for m in self.available_moves if m not in moves and m != "Stand_from_sit"]

        # Filter the non valid moves
        remaining = [m for m in remaining if is_valid_transition(position, m)]

        actions = [(position, mv) for mv in remaining]

        # Goal added only if feasible
        if is_valid_transition(position, self.goal[0]):
            actions.append((position, self.goal[0]))

        return actions

    def result(self, state, action):
        position, moves = state
        next_position = action[1]
        return (next_position, moves + (next_position,))

    def goal_test(self, state):
        position, moves = state
        # We need to reach the goal with at least one move
        num_optional = sum(1 for m in moves if m in pos and m not in man_pos)
        return position == self.goal[0] and num_optional >= 1


def generate(start, end, available_moves):
    return Choreography(start, end, available_moves)


def main():
    mandatory = list(man_pos.keys())
    final = []

    available_moves = [p for p in pos if p not in man_pos]

    print("Generating choreography...\n")

    for i in range(len(mandatory) - 1):
        start = mandatory[i]
        end = mandatory[i + 1]

        print(f"--- Segment {start} → {end} ---")

        final.append(start)

        problem = generate(start, end, available_moves)
        solution = iterative_deepening_search(problem)

        if solution is None:
            print(f"No solution for {start} → {end}")
            continue

        steps = solution.state[1][1:-1]  # esclude start e goal

        print(f"Moves: {steps}\n")
        final.extend(steps)

        # Remove used moves
        for step in steps:
            if step in available_moves:
                available_moves.remove(step)

    final.append(mandatory[-1])

    print("\nFinal choreography:")
    print(final)

    # Salva su file
    with open("choreography.txt", "w") as f:
        for step in final:
            f.write(step + "\n")

if __name__ == "__main__":
    main()

