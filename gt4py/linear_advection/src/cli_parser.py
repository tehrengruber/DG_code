import argparse
parser = argparse.ArgumentParser(
    description="CLI tool for running DG scheme on the Linear Advection Problem",
    formatter_class=argparse.ArgumentDefaultsHelpFormatter
)
parser.add_argument(
    '-n', type=int, metavar='', default=20, help="The number of elements used for both horizontal directions"
)
parser.add_argument(
    '-p', type=int, metavar='', default=0, help="The polynomial degree (leads to a p+1 order method in space)"
)
parser.add_argument(
    '-rk', type=int, metavar='', default=1, help="The order of Runge Kutta method"
)
parser.add_argument(
    '-b', type=str, metavar='', default='numpy', help="The name of the desired backend"
)
parser.add_argument(
    "--perf", action="store_true", help="Disables all output including plotting (used for performance benchmarking)"
)
args = parser.parse_args()

n, r, runge_kutta, backend = args.n, args.p, args.rk, args.b
perf_flag = args.perf