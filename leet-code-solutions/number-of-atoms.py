class Solution:
    def countOfAtoms(self, formula: str) -> str:
        store = Counter()
        stack = [store]

        i = 0
        while i < len(formula):
            if formula[i] == "(":
                i += 1
                store = Counter()
                stack.append(store)

            elif formula[i] == ")":
                i += 1
                end = i
                while i < len(formula) and formula[i].isdigit():
                    i += 1

                mul = int(formula[end:i] or 1)
                top = stack.pop()

                for ele, val in top.items():
                    stack[-1][ele] += val*mul

                store = stack[-1]

            else:
                start = i
                i += 1

                while i < len(formula) and formula[i].islower():
                    i += 1

                ele = formula[start:i]
                start = i
                while i < len(formula) and formula[i].isdigit():
                    i += 1

                mult = int(formula[start:i] or 1)
                stack[-1][ele] += mult

        return "".join(ele + (str(store[ele]) if store[ele] > 1 else "") for ele in sorted(store))
                


        