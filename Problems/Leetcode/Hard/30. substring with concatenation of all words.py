# https://leetcode.com/problems/substring-with-concatenation-of-all-words/
# You are given a string s and an array of strings words.
# All the strings of words are of the same length.
# A concatenated substring in s is a substring that contains all the strings
# of any permutation of words concatenated.
# Return the starting indices of all the concatenated substrings in s.
# You can return the answer in any order.
from typing import List
from itertools import permutations


class Solution:

    def __init__(self):
        self.indices = []
        self.word_map = dict()

    # первый подход - наивное решение (brute forсe)
    # очень долго из перебора всех перестановок
    def find_substring_bf(self, s: str, words: List[str]) -> List[int]:
        answer = []
        cash_perm = set()
        for perm in permutations(range(len(words))):
            words_perm = ''.join(words[pos] for pos in perm)
            if words_perm not in cash_perm:
                answer += indices if (indices := list(self.findall(words_perm, s))) else []
                cash_perm.add(words_perm)
        return answer

    # более быстрый алгоритм с использованием словарей
    # сложность по врмени O(n*(n+l)), где n кол-во слов,
    # l - длина строки
    def find_substring(self, s: str, words: List[str]) -> List[int]:
        cash_words = dict()
        zero_used = dict()
        n = len(words)
        m = len(words[0])
        answer = []
        for word in words:
            if word not in cash_words:
                self.findall_word(word, s)
                if word in self.word_map.values():
                    cash_words[word] = 1
                    zero_used[word] = 0
                else:
                    return []
            else:
                cash_words[word] += 1
        self.indices = sorted(self.indices)
        for i in range(len(self.indices)-n+1):
            cur_index = index = self.indices[i]
            used = zero_used.copy()
            used[self.word_map[index]] = 1
            for _ in range(n-1):
                cur_index = cur_index + m
                if (cur_index in self.word_map
                        and used[self.word_map[cur_index]] < cash_words[self.word_map[cur_index]]):
                    used[self.word_map[cur_index]] += 1
                else:
                    break
            if used == cash_words:
                answer.append(index)
        return answer

    @staticmethod
    def findall(pattern, string):
        index = string.find(pattern)
        while index != -1:
            yield index
            index = string.find(pattern, index + 1)

    def findall_word(self, word, string):
        index = string.find(word)
        while index != -1:
            self.indices.append(index)
            self.word_map[index] = word
            index = string.find(word, index + 1)


def test0():
    strings = ["wordgoodgoodgoodbestword",
               "barfoothefoobarman",
               "barfoofoobarthefoobarman",
               "fsdfoktoammdasoktoamtoamok",
               "asdtentendasd"]
    words_sets = [["word", "good", "best", "word"],
                  ["foo", "bar"],
                  ["bar", "foo", "the"],
                  ["ok", "to", "am"],
                  ["ten", "ten"]]

    for string, words in zip(strings, words_sets):
        print(Solution().find_substring(string, words))
        print(string)
        for word in words:
            print(f'{word}: {list(Solution.findall(word, string))}')


def test1():
    string = "pjzkrkevzztxductzzxmxsvwjkxpvukmfjywwetvfnujhweiybwvvsrfequzkhossmootkmyxgjg" \
             "fordrpapjuunmqnxxdrqrfgkrsjqbszgiqlcfnrpjlcwdrvbumtotzylshdvccdmsqoadfrpsvnwp" \
             "izlwszrtyclhgilklydbmfhuywotjmktnwrfvizvnmfvvqfiokkdprznnnjycttprkxpuykhmpchi" \
             "ksyucbmtabiqkisgbhxngmhezrrqvayfsxauampdpxtafniiwfvdufhtwajrbkxtjzqjnfocdheku" \
             "mttuqwovfjrgulhekcpjszyynadxhnttgmnxkduqmmyhzfnjhducesctufqbumxbamalqudeibljgb" \
             "speotkgvddcwgxidaiqcvgwykhbysjzlzfbupkqunuqtraxrlptivshhbihtsigtpipguhbhctcvub" \
             "nhqipncyxfjebdnjyetnlnvmuxhzsdahkrscewabejifmxombiamxvauuitoltyymsarqcuuoezcbq" \
             "pdaprxmsrickwpgwpsoplhugbikbkotzrtqkscekkgwjycfnvwfgdzogjzjvpcvixnsqsxacfwndzv" \
             "rwrycwxrcismdhqapoojegggkocyrdtkzmiekhxoppctytvphjynrhtcvxcobxbcjjivtfjiwmduhz" \
             "jokkbctweqtigwfhzorjlkpuuliaipbtfldinyetoybvugevwvhhhweejogrghllsouipabfafcxnh" \
             "ukcbtmxzshoyyufjhzadhrelweszbfgwpkzlwxkogyogutscvuhcllphshivnoteztpxsaoaacgxya" \
             "ztuixhunrowzljqfqrahosheukhahhbiaxqzfmmwcjxountkevsvpbzjnilwpoermxrtlfroqoclex" \
             "xisrdhvfsindffslyekrzwzqkpeocilatftymodgztjgybtyheqgcpwogdcjlnlesefgvimwbxcbzva" \
             "ibspdjnrpqtyeilkcspknyylbwndvkffmzuriilxagyerjptbgeqgebiaqnvdubrtxibhvakcyotkfo" \
             "nmseszhczapxdlauexehhaireihxsplgdgmxfvaevrbadbwjbdrkfbbjjkgcztkcbwagtcnrtqryuqix" \
             "tzhaakjlurnumzyovawrcjiwabuwretmdamfkxrgqgcdgbrdbnugzecbgyxxdqmisaqcyjkqrntxqmdr" \
             "czxbebemcblftxplafnyoxqimkhcykwamvdsxjezkpgdpvopddptdfbprjustquhlazkjfluxrzopqdst" \
             "ulybnqvyknrchbphcarknnhhovweaqawdyxsqsqahkepluypwrzjegqtdoxfgzdkydeoxvrfhxusrujnm" \
             "jzqrrlxglcmkiykldbiasnhrjbjekystzilrwkzhontwmehrfsrzfaqrbbxncphbzuuxeteshyrveamjs" \
             "fiaharkcqxefghgceeixkdgkuboupxnwhnfigpkwnqdvzlydpidcljmflbccarbiegsmweklwngvygbqpe" \
             "scpeichmfidgsjmkvkofvkuehsmkkbocgejoiqcnafvuokelwuqsgkyoekaroptuvekfvmtxtqshcwsztkr" \
             "zwrpabqrrhnlerxjojemcxel"
    words = ["dhvf", "sind", "ffsl", "yekr", "zwzq",
             "kpeo", "cila", "tfty", "modg",
             "ztjg", "ybty", "heqg", "cpwo", "gdcj",
             "lnle", "sefg", "vimw", "bxcb"]

    for word in words:
        print(f'{word}: {list(Solution.findall(word,string))}')

    print(Solution().find_substring(string, words))


if __name__ == '__main__':
    test0()
    test1()
