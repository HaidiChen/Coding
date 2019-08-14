# draw a typical English ruler

class EnglishRuler(object):
    def __init__(self, num_inches, major_length):
        """
        Draw English ruler with given number of inches, major tick length.
        """

        self._draw_line(major_length, '0')
        for j in range(1, num_inches + 1):
            self._draw_interval(major_length - 1)
            self._draw_line(major_length, str(j))

    def _draw_line(self, tick_length, tick_label=''):
        """
        Draw one line with given tick length(followed by optional label)
        """

        line = '-' * tick_length
        if tick_label:
            line += ' ' + tick_label
        print(line)

    def _draw_interval(self, center_length):
        """
        Draw tick interval based upon a central tick length
        """

        if center_length > 0:
            self._draw_interval(center_length - 1)
            self._draw_line(center_length)
            self._draw_interval(center_length - 1)
