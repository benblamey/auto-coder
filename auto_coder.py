import re
import subprocess
import os
import itertools
import random
import string

def parse_man_page(command):
    global command_man_lines
    os.system('man {} | col -b > foo.txt'.format(command))
    with open('foo.txt', 'r') as content_file:
        content = content_file.read()
    command_man_lines = re.split(r'\n\s*\n', content, flags=re.MULTILINE)
    command_man_lines = [line for line in command_man_lines if '--' in line]
    return command_man_lines


def extract_candidate_args(adjective):
    global candidate_args
    relevant_lines = list(itertools.filterfalse(lambda line: adjective not in line, command_man_lines))
    #print(relevant_lines)
    candidate_args = []
    for line in relevant_lines:
        # relevant_lines.split(' ').where
        matches = re.findall(r'--?[^,\s\n]+', line)
        for match in matches:
            candidate_args.append(match)
    return candidate_args


if __name__ == '__main__':
    VERB = 'sort'  # TODO: map this to a linux shell command with a search
    ADJECTIVES = 'reverse'  # TODO: look up in thesaurus

    command_man_lines = parse_man_page(VERB)
    candidate_args = extract_candidate_args(ADJECTIVES)

    print(candidate_args)

    for i in range(1, 5):
        args_sample = random.sample(candidate_args, random.randint(1, len(candidate_args)))
        random.shuffle(args_sample)
        #print(args_sample)

        args = ' '.join(args_sample)
        print(args)

        command = '{} {} <input.txt'.format(VERB, args)
        print(command)

        exit_value = os.system(command)
        print(exit_value)

    # TODO: extract commands
    # TODO: extract tokens for search

# for line in command_man_lines:
#     print(line)
#     print('***')
#


# TODO: trial and error to find working command

# ls_command = 'man ls'
# print("\nCalling command '{}'".format(ls_command), flush=True)
# (ls_status, ls_output) = subprocess.getstatusoutput(ls_command)

# print("status: {}\noutput: '{}'".format(ls_status, ls_output))
