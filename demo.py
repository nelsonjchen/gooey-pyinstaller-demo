import time

from gooey import Gooey, GooeyParser


@Gooey
def main():
    parser = GooeyParser(description='Add some o\'s your name!')
    parser.add_argument('name',
                        action='store',
                        help='Your name')
    parser.add_argument('-n', '--number-of-os', type=int, default=5,
                        help='Numbers of o\'s to add to your name')
    args = parser.parse_args()
    name = args.name
    number_of_os = args.number_of_os
    os_added = 0
    while os_added < number_of_os:
        time.sleep(1)
        name += "o"
        os_added = os_added + 1
    print(f"Here's the name with some O's!: {name}")


if __name__ == "__main__":
    main()
