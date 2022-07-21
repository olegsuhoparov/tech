from testdata.data import separators


def cut_title_until_value(title_article: str, length_article_for_shorten=25) -> str:
    length_title = len(title_article)
    if not isinstance(title_article, str):
        raise TypeError(f"Invalid datatype of your title, {type(title_article)}")
    if length_title < length_article_for_shorten + 1:
        if len(title_article) == 0:
            raise ValueError("Article doesn't have a title")
        return title_article

    new_title = []
    index = 0

    for letter in title_article:
        if index == length_article_for_shorten:
            break
        new_title += letter
        index += 1

    while index:
        index -= 1

        if index == 0:
            new_title.pop(index)
            break
        elif new_title[index] in separators:
            new_title.pop(index)
            if new_title[index - 1] not in separators:
                break
        else:
            new_title.pop(index)

    return "".join(new_title) + "..."


if __name__ == "__main__":
    print('\nPlease enter the full title of your article and the number of full characters in it as a integer, \n'
          'above which you want to shorten the title to the nearest full word, \n'
          'replacing everything after it with "..."')
    print("\nEnter a title:")
    title = input()
    try:
        print("\nEnter yhe length for shorten title:")
        length = int(input())
        print("Short title is: " + cut_title_until_value(title, length_article_for_shorten=length))
    except ValueError:
        print("You entered not a int as a length!")
