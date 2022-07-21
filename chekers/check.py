from testdata.data import separators


def function_works_correctly(title, length, result):
    if len(title) <= length:
        assert title == result, f"There are unexpected symbols in string: {title} -> {result}"
    else:
        length_result = len(result)
        assert result.endswith("..."), f"Article before changing - {title}, after changing - {result}"
        if length_result > 3:
            assert result[-4] not in separators, f"There is a separator character before the ellipsis, {result}"
            assert title[length_result - 3] in separators, f"The last replaced character was not a separator: " \
                                                           f"before changing - {title}, after changing - {result}"
