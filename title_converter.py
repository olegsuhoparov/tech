from testdata.data import separators


def trim_a_string_to_a_word(article_title: str, length_for_shortening=25) -> str:
    if not isinstance(article_title, str):
        raise TypeError(f"Invalid datatype of your title, {type(article_title)}")
    elif len(article_title) <= length_for_shortening:
        return article_title

    while length_for_shortening:
        length_for_shortening -= 1
        if article_title[length_for_shortening] in separators \
                and article_title[length_for_shortening - 1] not in separators:
            break
    return "".join(article_title[:length_for_shortening]) + "..."


if __name__ == "__main__":
    print('\nPlease enter the full title of your article and the number of full characters in it as a integer, \n'
          'above which you want to shorten the title to the nearest full word, \n'
          'replacing everything after it with "..."')
    print("\nEnter a title:")
    title = input()
    try:
        print("\nEnter yhe length for shorten title:")
        length = int(input())
        print("Short title is: " + trim_a_string_to_a_word(title, length_for_shortening=length))
    except ValueError:
        print("You entered not a int as a length!")
