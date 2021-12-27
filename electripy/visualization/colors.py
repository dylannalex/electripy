from numpy import MAY_SHARE_EXACT


BLACK = (0, 0, 0)
BLUE = (54, 74, 255)
RED = (255, 54, 54)
YELLOW = (242, 255, 115)
WHITE = (255, 255, 255)
GREEN = (51, 255, 0)
ORANGE = (255, 164, 6)


class RedBlueColorGenerator:
    def __init__(self, max_value: float):
        """
        A RedBlueColorGenerator instance let you generate a color
        for representing the length of a vector.

        Given a set of positive values {x0, x1, ..., xn}, where each
        value represents the norm of a given vector, we want to map
        each value to blue or red color where the shortest number is
        the most blue and the greatest is the most red.

        Since a color is represented with an RGB value (which would
        have the following structure: RGB_value = [0-255, 0, 0-255])
        we need to map each value in the set to a number between 0
        and 255 for red and for blue.

        To do that we first have to normalize the set, which means
        that we want to transform each element of the set to a number
        between 0 and 1. We can do that by dividing each element by xn:

                    normalized_set = {x0/xn, x1/xn, ..., xn}

        Now we have normalized our set we can map a xi value to an RGB color
        by using the following formula:

            RGB_value = (255 * normalized_value, 0, brightness - brightness * normalized_value)

        Where the brightness is a value between n and 255 (where n < 255)
        that indicates how 'blue' a vector can be.
        """
        self.max_value = max_value

    def get_color(self, value, brightness):
        if self.max_value == 0:
            return (0, 0, 0)
        normalized_value = value / self.max_value
        return (255 * normalized_value, 0, brightness - brightness * normalized_value)
