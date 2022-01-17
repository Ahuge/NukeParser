__author__ = 'Alex'
import re
import os

FUNCTION = re.compile(r"^\s\|\s\s([a-zA-Z0-9_]+)\(\.\.\.\)\r\n")
PARAM = re.compile(r"\s\|\s\s\s\s\s\s@param\s([a-zA-Z0-9_]+):.*?\r\n$")
DOC_LINE = re.compile(r"\s\|\s\s(.*)$")

HEADER_LINES = [
    "class %s(object):",
    "\n"
]


def get_data(from_path):
    with open(from_path, "rb") as fh:
        code_lines = fh.readlines()
    return code_lines


def get_headers(path):
    lines = HEADER_LINES
    modified_lines = []
    c = os.path.splitext(os.path.basename(path))[0]
    cls_name = c[0].upper() + c[1:]

    modified_lines.append(lines[0] % cls_name)
    modified_lines.append(lines[1])
    return modified_lines


def setup_headers(to_path):
    with open(to_path, "wb") as fh:
        fh.writelines(get_headers(to_path))


def start_function(line):
    match = FUNCTION.match(line)
    if match:
        return match.group(1)


def get_functions(code_lines):
    inside_function = False
    code_functions = []
    current_function = {}
    for line in code_lines:
        if not inside_function:
            name = start_function(line)
            if name:
                current_function['name'] = name
                current_function['params'] = []
                current_function['doc_string'] = ""
                inside_function = True

        else:
            match = FUNCTION.match(line)
            if match:
                # Quick! End our function and start again!
                code_functions.append(current_function)
                # Reset values
                current_function = {}
                inside_function = False

                name = start_function(line)
                if name:
                    current_function['name'] = name
                    current_function['params'] = []
                    current_function['doc_string'] = ""
                    inside_function = True

            else:
                # Still inside the function.
                param_match = PARAM.match(line)
                doc_match = DOC_LINE.match(line)

                if param_match:
                    current_function['params'].append(param_match.group(1))
                if doc_match:
                    current_function['doc_string'] += "    " + doc_match.group(1)

    return code_functions


def get_function_def(name, params):
    new_params = ["self"] + params
    line = "    def "
    line += name
    line += "("
    line += ", ".join(new_params)
    line += "):"
    return line


def write_python_file(code_functions, to_path):
    for function in code_functions:
        name = function['name']
        params = function['params']
        docstring = function['doc_string']

        write_lines = ["\n", get_function_def(name, params)]

        if len(docstring) > 5:
            write_lines.append("\n        \"\"\"\n" + docstring + "    \"\"\"")
        write_lines.append("\n        raise NotImplementedError(\"This function is not written yet. Please put in an "
                           "issue on the github page.\")\n")

        with open(to_path, "a") as fh:
            fh.writelines(write_lines)


def main(from_path, to_path):
    lines = get_data(from_path)

    setup_headers(to_path)
    functions = get_functions(lines)
    write_python_file(functions, to_path)

if __name__ == "__main__":
    os.path.join(os.path.dirname(__file__), "Node.txt")

    f = os.path.join(os.path.dirname(__file__), "Node.txt")
    t = os.path.join(os.path.dirname(__file__), "node.new")

    f = os.path.join(os.path.dirname(__file__), "Knob.txt")
    t = os.path.join(os.path.dirname(__file__), "knob.new")

    main(f, t)

