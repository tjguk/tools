import os, sys
import dataclasses

DEFAULT_LINE_WIDTH = 144

@dataclasses.dataclass
class Dimensions:
    screen_height: int
    line_size: int
    chunk_size: int = dataclasses.field(init=False)

    def __post_init__(self):
        if self.screen_height:
            self.chunk_size = self.line_size * self.screen_height
        else:
            self.chunk_size = None

def dimensions():
    try:
        w, h = os.get_terminal_size()
    except OSError:
        w, h = (DEFAULT_LINE_WIDTH, None)
    return Dimensions(
        screen_height = (h - 3) if h else None,
        line_size = (w - 3) // 4
    )

def lines_from_chunk(chunk, dims):
    pos = 0
    while True:
        yield chunk[pos:pos+dims.line_size]
        pos += dims.line_size
        if pos > len(chunk):
            break

def main(filepath):
    with open(filepath, "rb") as f:
        n_lines = 1
        while True:
            dims = dimensions()
            if dims.chunk_size:
                chunk = f.read(dims.chunk_size)
            else:
                chunk = f.read()
            if not chunk: break

            for line in lines_from_chunk(chunk, dims):
                line += b" " * (dims.line_size - len(line))
                printable_line = "".join(chr(c) if 32 <= c <= 126 else "." for c in line)

                print(printable_line, "|", line.hex(" "))
                if dims.screen_height:
                    if n_lines % dims.screen_height == 0:
                        try:
                            input("Press enter to continue...")
                        except KeyboardInterrupt:
                            sys.exit()
                n_lines += 1

if __name__ == '__main__':
    main(*sys.argv[1:])
