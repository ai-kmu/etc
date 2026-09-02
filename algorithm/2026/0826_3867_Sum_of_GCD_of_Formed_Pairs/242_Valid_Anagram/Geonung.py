class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        print(type(s))
        print("".join(sorted(s)))
        print("".join(sorted(t)))
        print("".join(sorted(s)) == "".join(sorted(t)))
        return "".join(sorted(s)) == "".join(sorted(t))
