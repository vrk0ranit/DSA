class Solution:
    def totalNumbers(self, digits: List[int]) -> int:

        ans = set()

        def solve(path, used):
            if len(path) == 3:
                num = path[0] * 100 + path[1] * 10 + path[2]
                if num % 2 == 0:
                    ans.add(num)
                return

            for i in range(len(digits)):
                if used[i]:
                    continue

                # No leading zero
                if len(path) == 0 and digits[i] == 0:
                    continue

                used[i] = True
                path.append(digits[i])

                solve(path, used)

                path.pop()
                used[i] = False

        solve([], [False] * len(digits))

        return len(ans)