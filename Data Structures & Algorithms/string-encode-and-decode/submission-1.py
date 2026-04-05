class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join(f'{len(s)}#{s}' for s in strs)

    def decode(self, s: str) -> List[str]:
        res, idx = [], 0
        while idx < len(s):
            delimiter_pos = s.find('#', idx)  # find the first `#` delimiter
            if delimiter_pos < 0:
                break
            num = int(''.join(s[i] for i in range(idx, delimiter_pos)))
            idx = delimiter_pos + 1 + num
            res.append(''.join(s[i + delimiter_pos + 1] for i in range(0, num)))
        return res
