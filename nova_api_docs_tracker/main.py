# -*- coding: utf-8 -*-

import argparse
import glob
import os
import re
import sys

from nova_api_docs_tracker.templates import templates

SPLIT_FILE_RE = re.compile(r'\n([\w\s]+)\n\=+\n', re.MULTILINE)
METHODS_LIST_RE = re.compile(r'rest_method:: ([A-Z]+.*$)', re.MULTILINE)

def main():
    args = parse_args()
    path = args.path

    # check path
    if not os.path.exists(path):
        print "Error: Path: {} does not exist!".format(path)
        sys.exit(1)

    lp_out = dict()
    output = dict()

    # get inc files
    inc_files = get_inc_files(path)

    body_template = templates['body']
    method_template = templates['methods']
    parameters_template = templates['parameters']
    examples_template = templates['examples']

    for filename in inc_files:
        output['inc_file'] = filename

        contents = inc_files[filename]['contents']

        # TODO(auggy): link to inc source code in repo, cgit or github
        source_file = inc_files[filename]['path']  # can we derive it from the path?
        output['source_link'] = source_file

        # TODO(auggy): this should use docutils
        extracted_contents = extract_stuff(split_inc_file(contents))

        # verify body
        rendered_body = body_template.render(output)
        lp_out[filename]['body'] = rendered_body

        # verify methods names
        output['methods_list'] = get_methods_list(extracted_contents['methods'])
        rendered_methods = method_template.render(output)
        lp_out[filename]['methods_list'] = rendered_methods

        for method_name in extracted_contents['methods']:
            method_content = extracted_contents['methods'][method_name]

            # verify parameters
            output['method_name'] = method_name
            output['parameters_list'] = get_parameters_list(method_content)
            rendered_parameters = parameters_template.render(output)
            lp_out[filename]['methods'][method_name]['parameters'] = rendered_parameters

            # verify examples
            rendered_examples = examples_template.render(output)
            lp_out[filename]['methods'][method_name]['examples'] = rendered_examples

    # instantiate new Launchpad client
    # lp_client = ...?

    bugs = dict()

    for filename in lp_out:
        # print body locally in case of LP error
        print_local_file(
            contents=lp_out[filename]['body'], output_file='body_' + filename)

        # TODO(auggy): create a bug in LP to verify body content
        # lp_client.post...?
        bugs[filename]['body'] = '' # bug id

        # print methods locally in case of LP error
        print_local_file(contents=lp_out[filename]['methods_list'], output_file='methods_' + filename)

        # TODO(auggy): create a bug in LP to verify methods list
        # lp_client.post...?
        bugs[filename]['methods_list'] = '' # bug id

        for method_name in lp_out[filename]['methods']:
            # print parameters locally in case of LP error
            print_local_file(
                contents=lp_out[filename]['methods'][method_name]['parameters'],
                output_file=
                '_'.join(method_name.split()) + '_parameters__' + filename)

            # TODO(auggy): create a bug in LP to verify parameters
            # lp_client.post...?
            bugs[filename]['methods'][method_name]['parameters'] = '' # bug id

            print_local_file(
                contents=lp_out[filename]['methods'][method_name]['examples'],
                output_file=
                '_'.join(method_name.split()) + '_examples__' + filename)

            # TODO(auggy): create a bug in LP to verify examples
            # lp_client.post...?
            bugs[filename]['methods'][method_name]['examples'] = '' # bug id

    # TODO(auggy): keep track of bugs...?
    # dump out bugs to local file

def parse_args():
    parser = argparse.ArgumentParser("Post bugs to Launchpad for verifying API docs")
    parser.add_argument("path",
                        type=str,
                        help="inc files location",
                        nargs="?")
    return parser.parse_args()


def get_inc_files(path):
    inc_files = {}
    for filename in glob.glob(os.path.join(path, '*.inc')):
        print "Processing %(filename)s..." % {'filename': filename}
        f = open(filename, 'r')

        parts = filename.split('/')
        shortened_filename = parts[-1]
        inc_files[shortened_filename] = {'contents': f.read(), 'path': filename}

    return inc_files


def split_inc_file(contents):
    split_file = re.split(SPLIT_FILE_RE, contents)
    return split_file


def extract_stuff(split_contents):
    result = dict()

    result['body'] = split_contents[0]
    result['methods'] = dict(zip(map(lambda x: re.sub('\\n', '', x), split_contents[1::2]), split_contents[2::2]))
    return result

def get_methods_list(contents):
    list = ''
    for k in contents:
        v = contents[k]
        found = re.search(METHODS_LIST_RE, v)
        if found:
            url = found.group(1)
        else:
            continue
        list = list + url + ' (' + k + ')\n'
    return list


def get_parameters_list(contents):
    # TODO(auggy): if we decide this is helpful
    return []


def print_local_file(contents, output_file):
    print "Writing backup file: {}".format(output_file)
    with open('../out/' + output_file, 'w') as f:
        f.write(contents.encode("utf-8", "ignore"))

# Allow for local debugging
if __name__ == '__main__':
    main()