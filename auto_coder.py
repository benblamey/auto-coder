import re
import subprocess
import os
import itertools
import random
import string


def parse_man_page(command):
    os.makedirs('man_cache', exist_ok=True)
    os.system('man {} | col -b > man_cache/man_{}.txt'.format(command, command))
    # from: https://unix.stackexchange.com/questions/15855/how-to-dump-a-man-page

    with open('man_cache/man_{}.txt'.format(command), 'r') as content_file:
        content = content_file.read()
    command_man_lines = re.split(r'\n\s*\n', content, flags=re.MULTILINE)
    command_man_lines = [line for line in command_man_lines if '-' in line]

    print(command_man_lines)

    # TODO: parse synopsis section also (see tar)
    # TODO: score for relevence
    return command_man_lines


def extract_candidate_args(command_man_lines, adjective):
    relevant_lines = list(itertools.filterfalse(lambda line: adjective.lower() not in line.lower(), command_man_lines))
    # print(relevant_lines)
    candidate_args = []
    for line in relevant_lines:
        # relevant_lines.split(' ').where
        matches = re.findall(r'--?[^,\s\n]+', line)
        for match in matches:
            candidate_args.append(match)
    return candidate_args


def auto_generate(verb, adjective):
    command_man_lines = parse_man_page(verb)
    candidate_args = extract_candidate_args(command_man_lines, adjective)
    print(candidate_args)

    for i in range(1, 5):
        # TODO: avoid duplicates
        args_sample = random.sample(candidate_args, random.randint(0, len(candidate_args)))
        random.shuffle(args_sample)
        # print(args_sample)

        args = ' '.join(args_sample)
        # print(args)

        print('running...')
        command = '{} {} <input.txt'.format(verb, args)
        print(command)

        exit_value = os.system(command)
        print('exit value: {}'.format(exit_value))

        # TODO: cost function - number of arguments
        # TODO: check return value
        # TODO: ask user which output is correct
        # TODO: prefer double-dash


if __name__ == '__main__':
    # TODO: map 1st arg this to a linux shell command with a search
    # TODO: look up args in thesaurus
    # TODO: allow soft-matching/partial/word-stem of adjectives
    # TODO: allow data for args (e.g. for regex)

    auto_generate('sort', 'numeric')

    # auto_generate('tar', 'Extract files')

    # auto_generate('uniq', 'case')
    #auto_generate('uniq', 'count')

# for line in command_man_lines:
#     print(line)
#     print('***')
#


# TODO: trial and error to find working command

# ls_command = 'man ls'
# print("\nCalling command '{}'".format(ls_command), flush=True)
# (ls_status, ls_output) = subprocess.getstatusoutput(ls_command)

# print("status: {}\noutput: '{}'".format(ls_status, ls_output))
