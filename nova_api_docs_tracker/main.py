# -*- coding: utf-8 -*-

import glob
import os
import re

SPLIT_FILE_RE = re.compile(r'\n([\w\s]+)\n\=+\n', re.MULTILINE)

def main():
    # TODO(auggy): args: inc files path
    path = ''
    output = {}

    # get inc files
    inc_files = get_inc_files(path)

    for filename in inc_files:
        contents = inc_files[filename]
        # TODO(auggy): link to file on github??

        # TODO(auggy): this should use docutils
        extracted_contents = extract_stuff(split_inc_file(contents))

        # verify body
        output['body'] = extracted_contents['body']

        # verify methods names
        output['methods_list'] = '\n'.join(extracted_contents['methods'].keys())

        methods = {}
        for method_name in extracted_contents['methods']:
            method_content = extracted_contents['methods'][method_name]

            # verify parameters
            # TODO(auggy): create parameters list

            # verify examples
            # TODO(auggy): I don't think we need anything special here...

            methods[method_name] = method_content

        output['methods'] = methods

        # TODO(auggy): print to local file using Jinja templates
        print "Body: %(body)s \n " + \
              "Method List: %(methods_list)s \n" + \
              "Methods: %(methods)s" \
              % output

        # TODO(auggy): post bugs to Launchpad using local files
        # TODO(auggy): keep track of bugs...?

        # TODO(auggy): option for retrieving and editing LP bugs...


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
    result['methods'] = dict(zip(map(lambda x: re.sub('\\n', '', x), split_contents[3::2]), split_contents[2::2]))
    return result

# Allow for local debugging
if __name__ == '__main__':
    main()