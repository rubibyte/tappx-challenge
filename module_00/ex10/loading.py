import time


def ft_progress(lst):
    total = len(lst)
    processed = 0
    start_time = time.time()
    len_total = len(str(total))
    for i, item in enumerate(lst):
        yield item
        processed += 1
        percentage = (processed / total) * 100
        elapsed_time = time.time() - start_time
        remaining_time = (elapsed_time / processed) * (total - processed)
        progress_bar = '=' * int(percentage / 2)
        arrow = '>' if i < total - 1 else ''
        progress_bar_str = "ETA: {:.2f}s [{:>3}%] [{:<50}] {}/{} | \
                            elapsed time {:.2f}s".format(remaining_time,
                                                         int(percentage),
                                                         progress_bar + arrow,
                                                         processed, total,
                                                         elapsed_time)
        print(f"\r{progress_bar_str}", end='')
    print("\n...", end='')


# listy = range(1000)
# ret = 0
# for elem in ft_progress(listy):
#     ret += (elem + 3) % 5
#     time.sleep(0.01)
# print()
# print(ret)

# listy = range(3333)
# ret = 0
# for elem in ft_progress(listy):
#     ret += elem
#     time.sleep(0.005)
# print()
# print(ret)


# listy = range(10)
# ret = 0
# simple = 0
# for elem in ft_progress(listy):
#     simple += elem
#     ret += (elem+3) % 5
#     print(elem, simple, ret)
#     time.sleep(0.3)
# print(simple)
# print(ret)
# listy = range(3333)
# ret = 0
# for elem in ft_progress(listy):
#     ret += elem
#     time.sleep(0.0005)
# print()
# print(ret)
