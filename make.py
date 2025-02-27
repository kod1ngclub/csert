from dataclasses import dataclass

# ==== model
@dataclass
class Header:
    path: str
    std: list[str]

@dataclass
class Source:
    path: str
    std: list[str]

@dataclass
class Stage:
    name: str
    headers: list[Header]
    sources: list[Source]

@dataclass
class Project:
    name: str
    guard: str

# ==== API
def Make(proj: Project, stages: list[Stage]):
    print("==== Make")
    print(f"> name: {proj.name}")
    print(f"> guard: {proj.guard}")

    print()

    headers: list[str]      = []
    headerstds: list[str]   = []
    sources: list[str]      = []
    sourcestds: list[str]   = []

    for stage in stages:
        for header in stage.headers:
            headers.append(header.path)

            for std in header.std:
                headerstds.append(std)

        for source in stage.sources:
            sources.append(source.path)

            for std in source.std:
                sourcestds.append(std)

    headerstds = list(dict.fromkeys(headerstds))
    sourcestds = list(dict.fromkeys(sourcestds))

    print("==== Header")
    for header in headers:
        print(f"> {header}")

    for headerstd in headerstds:
        print(f"  > {headerstd}")

    print()

    print("==== Source")
    for source in sources:
        print(f"> {source}")

    for sourcestd in sourcestds:
        print(f"  > {sourcestd}")

    print()

    EMPTY   = ""

    sheader = ""
    ssource = ""

    print("==== Building...")
    for stage in stages:
        for header in stage.headers:
            print(f"Extract from {header.path}")
            with open(header.path, "r", encoding="utf-8") as file:
                lines = file.readlines()

            # remove first 2 lines and last 1 line
            lines = lines[2:-1]

            # remove line starting from #include
            lines = [line for line in lines if not line.lstrip().startswith("#include")]

            sheader += EMPTY.join(lines)

        for source in stage.sources:
            print(f"Extract from {source.path}")
            with open(source.path, "r", encoding="utf-8") as file:
                lines = file.readlines()

            # remove first 1 line
            lines = lines[1:]

            # remove line starting from #include
            lines = [line for line in lines if not line.lstrip().startswith("#include")]

            ssource += EMPTY.join(lines)

    print()

    print("==== Writing out...")
    with open(f"{proj.name}.h", "w") as file:
        file.write(f"#ifndef {proj.guard}")
        file.write("\n")

        file.write(f"#define {proj.guard}")
        file.write("\n")

        for std in headerstds:
            file.write(f"#include <{std}>")
            file.write("\n")

        file.write(sheader)
        file.write("\n")

        file.write(f"#endif // {proj.guard}")

    print(f"Writed out to {proj.name}.h")

    with open(f"{proj.name}.c", "w") as file:
        file.write(f"#include \"{proj.name}.h\"")
        file.write("\n")

        for std in sourcestds:
            file.write(f"#include <{std}>")
            file.write("\n")

        file.write(ssource)

    print(f"Writed out to {proj.name}.c")


def Echo(proj: Project, stages: list[Stage]):
    print("==== Echo")
    print(f"> name: {proj.name}")
    print(f"> guard: {proj.guard}")

    print()

    for stage in stages:
        print(f"==== stage:{stage.name}")

        for header in stage.headers:
            print(f"> {header.path}")

            for std in header.std:
                print(f"  > {std}")

        for source in stage.sources:
            print(f"> {source.path}")

            for std in source.std:
                print(f"  > {std}")

        print()

# ==== main
proj = Project(
    name    = "csert",
    guard   = "CSERT_H"
)

STAGE_ASSERT = Stage(
    name="assert",
    headers=[
        Header(path="include/assert.h", std=["stdbool.h"])
    ],
    sources=[
        Source(path="src/assert.c", std=["stdio.h", "stdlib.h"])
    ]
)

Make(proj, [
    STAGE_ASSERT
])
