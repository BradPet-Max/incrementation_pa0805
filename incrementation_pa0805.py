def climb_stairs(N, stairs=None):
    """
    Returns a valid list of steps to climb a staircase of N stairs.

    Rules:
    - You can only take 1, 2, or 3 steps at a time.
    - You cannot take the same step size twice in a row.
    """

    if stairs is None:
        stairs = []

    # Base case: exactly reached the top
    if N == 0:
        return stairs

    # Try possible step sizes
    for step in [1, 2, 3]:

        # Check:
        # 1. step does not exceed remaining stairs
        # 2. step is not same as previous step
        if step <= N and (len(stairs) == 0 or stairs[-1] != step):

            result = climb_stairs(N - step, stairs + [step])

            # If a valid solution is found, return it
            if result:
                return result

    # No valid solution found
    return None


# Example usage
print(climb_stairs(5))