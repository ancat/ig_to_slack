def get_state(state_file):
    with open(state_file, 'r') as fh:
        return list(map(lambda x: x.strip(), fh))

def put_state(state_file, state):
    with open(state_file, 'w') as fh:
        return fh.write("\n".join(state))
