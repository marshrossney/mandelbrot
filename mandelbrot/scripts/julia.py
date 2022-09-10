import matplotlib.pyplot as plt

from mandelbrot.fractals import Julia
from mandelbrot.scripts.parser import parser

parser.add_argument(
    "-c",
    "--const",
    type=float,
    nargs=2,
    help="Real and imaginary parts of the additive constant",
    metavar=("REAL", "IMAG"),
)


def main(arg_str=None):
    args = parser.parse_args(arg_str)

    c = complex(args.const[0], args.const[1])
    centre = complex(args.midpoint[0], args.midpoint[1])

    fig = Julia(c, centre, args.extent, args.resolution).get_figure(args.cmap)

    if args.output:
        fig.gca().set_axis_off()
        fig.gca().set_title("")
        fig.tight_layout()
        fig.savefig(args.output, dpi=300)
    else:
        plt.show()


if __name__ == "__main__":
    main()
