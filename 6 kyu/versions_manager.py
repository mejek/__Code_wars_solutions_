# In this kata we are going to mimic a software versioning system.
#
# You have to implement a VersionManager class.
#
# It should accept an optional parameter that represents the initial version.
# The input will be in one of the following formats: "{MAJOR}", "{MAJOR}.{MINOR}",
# or "{MAJOR}.{MINOR}.{PATCH}". More values may be provided after PATCH but they should be ignored.
# If these 3 parts are not decimal values, an exception with the message
# "Error occured while parsing version!" should be thrown. If the initial
# version is not provided or is an empty string, use "0.0.1" by default.
#
# This class should support the following methods, all of which should be chainable (except release):
#
#     major() - increase MAJOR by 1, set MINOR and PATCH to 0
#     minor() - increase MINOR by 1, set PATCH to 0
#     patch() - increase PATCH by 1
#     rollback() - return the MAJOR, MINOR, and PATCH to their values before the
#     previous major/minor/patch call, or throw an exception with the message
#     "Cannot rollback!" if there's no version to roll back to
#     release() - return a string in the format "{MAJOR}.{MINOR}.{PATCH}"
#
# May the binary force be with you!
# My solution:

class VersionManager:
    def __init__(self, version = '0.0.1'):
        self.validate_digits(version)
        self.version = self.create_version(version)
        self.version_history = ['0.0.1']


    def validate_digits(self, version):
        if version == '':
            return
        split_list = version.split('.')
        for n in range(len((split_list))):
            if n > 2:
                break
            try:
                int(split_list[n])
            except:
                raise Exception("Error occured while parsing version!")

    def create_version(self, version):
        if version == None or version == '':
            return [0, 0, 1]
        else:
            version_list = []
            for n in range(3):
                try:
                    version_list.append(int(version.split('.')[n]))
                except:
                    version_list.append(0)
            return version_list

    def major(self):
        self.version[0] += 1
        self.version[1] = 0
        self.version[2] = 0
        self.version_history.append(f'{self.version[0]}.{self.version[1]}.{self.version[2]}')
        return self

    def minor(self):
        self.version[1] += 1
        self.version[2] = 0
        self.version_history.append(f'{self.version[0]}.{self.version[1]}.{self.version[2]}')
        return self

    def patch(self):
        self.version[2] += 1
        self.version_history.append(f'{self.version[0]}.{self.version[1]}.{self.version[2]}')
        return self

    def rollback(self):
        try:
            self.version = self.create_version(self.version_history[-2])
            self.version_history = self.version_history[:-1]
        except:
            raise Exception('Cannot rollback!')
        return self

    def release(self):
        return f'{self.version[0]}.{self.version[1]}.{self.version[2]}'