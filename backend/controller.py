import shell_command_runner
def images(name=None):
    command_output = shell_command_runner.run(['docker', 'images'])
    lno = 1
    images = []
    for line in command_output.split('\n'):
        tokens = []
        for word in ' '.join(line.split()).split(' '):
            tokens.append(word)
        if len(tokens) != 7:
            continue
        if name is None:
            images.append({'name': tokens[0], 'tag': tokens[1], 'id': tokens[2]})
            continue
        if not tokens[0].partition(name)[1] == "":
            images.append({'name': tokens[0], 'tag': tokens[1], 'id': tokens[2]})
    return images
