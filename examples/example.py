from easymp import parallel, addlogging, execute


@addlogging
def square(x):
    logger.info("Square: %d" % x)
    return x * x


@addlogging
@parallel
def process(x):
    y = square(x)
    logger.info("Input %d, output %d." (x, y))
    return True


if __name__ == "__main__":
    execute(process, it=range(20), nprocs=3)
