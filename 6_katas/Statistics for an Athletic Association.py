# You are the "computer expert" of a local Athletic Association (C.A.A.). Many teams of runners come to compete. Each time you get a string of all race results of every team who has run. For example here is a string showing the individual results of a team of 5 runners:

# "01|15|59, 1|47|6, 01|17|20, 1|32|34, 2|3|17"

# Each part of the string is of the form: h|m|s where h, m, s (h for hour, m for minutes, s for seconds) are positive or null integer (represented as strings) with one or two digits. Substrings in the input string are separated by ,  or ,.

# To compare the results of the teams you are asked for giving three statistics; range, average and median.

# Range : difference between the lowest and highest values. In {4, 6, 9, 3, 7} the lowest value is 3, and the highest is 9, so the range is 9 − 3 = 6.

# Mean or Average : To calculate mean, add together all of the numbers and then divide the sum by the total count of numbers.

# Median : In statistics, the median is the number separating the higher half of a data sample from the lower half. The median of a finite list of numbers can be found by arranging all the observations from lowest value to highest value and picking the middle one (e.g., the median of {3, 3, 5, 9, 11} is 5) when there is an odd number of observations. If there is an even number of observations, then there is no single middle value; the median is then defined to be the mean of the two middle values (the median of {3, 5, 6, 9} is (5 + 6) / 2 = 5.5).

# Your task is to return a string giving these 3 values. For the example given above, the string result will be

# "Range: 00|47|18 Average: 01|35|15 Median: 01|32|34"

# of the form: "Range: hh|mm|ss Average: hh|mm|ss Median: hh|mm|ss"`

# where hh, mm, ss are integers (represented by strings) with each 2 digits.

# Remarks:

# if a result in seconds is ab.xy... it will be given truncated as ab.
# if the given string is "" you will return ""



def stat(results):
    if not results:
        return ""

    def time_to_seconds(time_str):
        h, m, s = map(int, time_str.split('|'))
        return h * 3600 + m * 60 + s
    
    times = sorted(time_to_seconds(t) for t in results.split(', '))

    def seconds_to_time(seconds):
        h, seconds = divmod(seconds, 3600)
        m, s = divmod(seconds, 60)
        return f"{h:02}|{m:02}|{s:02}"

    range_value = seconds_to_time(times[-1] - times[0])
    average_value = seconds_to_time(sum(times) // len(times))

    if len(times) % 2 == 1:
        median_value = seconds_to_time(times[len(times) // 2])
    else:
        median_value = seconds_to_time((times[len(times) // 2 - 1] + times[len(times) // 2]) // 2)

    return f"Range: {range_value} Average: {average_value} Median: {median_value}"

# Test example
#results = "01|15|59, 1|47|6, 01|17|20, 1|32|34, 2|3|17"
result_string = stat("02|15|59, 2|47|16, 02|17|20, 2|32|34, 2|17|17, 2|22|00, 2|31|41")
print(result_string)


# more compact

# from statistics import median, mean

# def stat(s):
#     if not s: return ''

#     t = [itime(w) for w in s.split(',')]
#     return 'Range: {} Average: {} Median: {}'.format(stime(max(t) - min(t)), stime(int(mean(t))), stime(int(median(t))))

# def itime(w):
#     return sum([int(c) * 60**i for i, c in enumerate(w.split('|')[::-1])])
    
# def stime(n):
#     return '{:02d}|{:02d}|{:02d}'.format(n // 3600, (n % 3600) // 60, n % 60)