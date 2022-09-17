# Description:
#
# Your task in order to complete this Kata is to write a function which formats a duration, given as a number of seconds, in a human-friendly way.
#
# The function must accept a non-negative integer. If it is zero, it just returns "now". Otherwise, the duration is expressed as a combination of years, days, hours, minutes and seconds.
#
# It is much easier to understand with an example:
#
# * For seconds = 62, your function should return
#     "1 minute and 2 seconds"
# * For seconds = 3662, your function should return
#     "1 hour, 1 minute and 2 seconds"
#
# For the purpose of this Kata, a year is 365 days and a day is 24 hours.
#
# Note that spaces are important.
# Detailed rules
#
# The resulting expression is made of components like 4 seconds, 1 year, etc. In general, a positive integer and one of the valid units of time, separated by a space. The unit of time is used in plural if the integer is greater than 1.
#
# The components are separated by a comma and a space (", "). Except the last component, which is separated by " and ", just like it would be written in English.
#
# A more significant units of time will occur before than a least significant one. Therefore, 1 second and 1 year is not correct, but 1 year and 1 second is.
#
# Different components have different unit of times. So there is not repeated units like in 5 seconds and 1 second.
#
# A component will not appear at all if its value happens to be zero. Hence, 1 minute and 0 seconds is not valid, but it should be just 1 minute.
#
# A unit of time must be used "as much as possible". It means that the function should not return 61 seconds, but 1 minute and 1 second instead. Formally, the duration specified by of a component must not be greater than any valid more significant unit of time.
#
# My solution:
def format_duration(seconds):
    year = 31536000
    day = 86400
    hour = 3600
    minute = 60
    result = ''

    if seconds == 0:
        return 'now'
    if seconds >= year:
        year_count = int(seconds / year)
        if year_count > 1:
            result += f'{year_count} years, '
        else:
            result += f'{year_count} year, '
        seconds = seconds % year
    if seconds >= day:
        day_count = int(seconds / day)
        if day_count > 1:
            result += f'{day_count} days, '
        else:
            result += f'{day_count} day, '
        seconds = seconds % day
    if seconds >= hour:
        hour_count = int(seconds / hour)
        if hour_count == 0:
            pass
        if hour_count > 1:
            result += f'{hour_count} hours, '
        else:
            result += f'{hour_count} hour, '
        seconds = seconds % hour
    if seconds >= minute:
        minute_count = int(seconds / minute)
        if minute_count == 0:
            pass
        if minute_count > 1:
            result += f'{minute_count} minutes, '
        else:
            result += f'{minute_count} minute, '
        seconds = seconds % minute
    if seconds < minute and seconds == 1:
        result += f'{seconds} second, '
    if seconds < minute and seconds != 1 and seconds != 0:
        result += f'{seconds} seconds, '

    result = result[:-2]
    result = ' and '.join(result.rsplit(', ', 1))

    return result
