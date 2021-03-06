"""
EPython is a code-transformer that translates a statically typed subset of
Python syntax into an extension of Python for a particular backend.

The .epy file is first compiled into an AST
The AST is validated to ensure it uses only the allowed subset of Python
The AST is then fed to a transformer specific to the backend.

"""
import argparse
import ast

def main():
    parser = argparse.ArgumentParser(prog='epython', 
            description="Compile statically typed subset of Python to a backend.")

    parser.add_argument("file")
    parser.add_argument("--backend", default="cpython")

    args = parser.parse_args()

    with open(args.file) as myfile:
        source = myfile.read()

    res = compile(source, args.file, 'exec', flags=ast.PyCF_ONLY_AST)

    print(ast.dump(res))

if __name__ == "__main__":
    main()