# compute the disk usage of a given directory

import os

class DiskUsage(object):
    def __init__(self, path):
        self.path = path

    def get_disk_usage(self):
        return self._disk_usage_helper(self.path)

    def _disk_usage_helper(self, path):
        """
        Return the number of bytes used by the file/folder and any descendents
        """

        total = os.path.getsize(path)
        if os.path.isdir(path):
            for filename in os.listdir(path):
                childpath = os.path.join(path, filename)
                total += self._disk_usage_helper(childpath)

        print(str(total) + '\t' + path)

        return total
