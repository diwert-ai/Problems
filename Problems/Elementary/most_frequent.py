#https://py.checkio.org/en/mission/the-most-frequent/

def most_frequent_my(data: list) -> str:
    """
    determines the most frequently occurring string in the sequence.
    """
    cnt = 0
    item = ''
    for i in data:
        n_cnt = data.count(i)
        if n_cnt > cnt:
            cnt = n_cnt
            item = i
    return item

def most_frequent(data: list) -> str:
    """
    determines the most frequently occurring string in the sequence.
    """
   
    return max(set(data),key=data.count)




if __name__ == "__main__":
    # These "asserts" using only for self-checking and not necessary for auto-testing
    print("Example:")
    print(most_frequent(["a", "b", "c", "a", "b", "a"]))

    assert most_frequent(["a", "b", "c", "a", "b", "a"]) == "a"

    assert most_frequent(["a", "a", "bi", "bi", "bi"]) == "bi"
    print("Done")
