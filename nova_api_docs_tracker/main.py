# -*- coding: utf-8 -*-

import argparse
import glob
import os
import re

from nova_api_docs_tracker.templates import templates

SPLIT_FILE_RE = re.compile(r'\n([\w\s]+)\n\=+\n', re.MULTILINE)
METHODS_LIST_RE = re.compile(r'rest_method:: ([A-Z]+.*$)', re.MULTILINE)

def main():
    args = parse_args()
    path = args.path
    output = {}

    # get inc files
    inc_files = get_inc_files(path)

    body_template = templates['body']
    method_template = templates['methods']
    parameters_template = templates['parameters']
    examples_template = templates['examples']

    for filename in inc_files:
        output['inc_file'] = filename

        contents = inc_files[filename]
        # TODO(auggy): link to inc source code in repo, cgit or github
        output['source_link'] = ''

        # TODO(auggy): this should use docutils
        extracted_contents = extract_stuff(split_inc_file(contents))

        # verify body
        rendered_body = body_template.render(output)

        # TODO(auggy): print to local file
        print rendered_body


        # verify methods names
        output['methods_list'] = get_methods_list(extracted_contents['methods'])
        rendered_methods = method_template.render(output)

        # TODO(auggy): print to local file
        print rendered_methods

        for method_name in extracted_contents['methods']:
            method_content = extracted_contents['methods'][method_name]

            # verify parameters
            output['method_name'] = method_name
            output['parameters_list'] = get_parameters_list(method_content)
            rendered_parameters = parameters_template.render(output)

            # TODO(auggy): print to local file
            print rendered_parameters

            # verify examples
            rendered_examples = examples_template.render(output)

            # TODO(auggy): print to local file
            print rendered_examples

        # TODO(auggy): post bugs to Launchpad using local files
        # TODO(auggy): keep track of bugs...?

        # TODO(auggy): option for retrieving and editing LP bugs...

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

        # TODO(auggy): remove rest of path from filename
        inc_files[filename] = f.read()

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

# Allow for local debugging
if __name__ == '__main__':
    main()