class Solution:
    def multiply(self, mat1: List[List[int]], mat2: List[List[int]]) -> List[List[int]]:
        r1, c1 = len(mat1), len(mat1[0])
        r2, c2 = len(mat2), len(mat2[0])

        # Store non-zero entries of mat1
        mat1_map = defaultdict(list)
        for i in range(r1):
            for j in range(c1):     
                if mat1[i][j] != 0:
                    mat1_map[i].append((j, mat1[i][j]))  # (col, val) per row what columns are zer0

        # Store non-zero entries of mat2
        mat2_map = defaultdict(list)
        for i in range(r2):
            for j in range(c2):
                if mat2[i][j] != 0:
                    mat2_map[i].append((j, mat2[i][j]))  # (col, val)
        print(mat1_map)
        print(mat2_map)

        # Multiply sparse matrices
        result = [[0] * c2 for _ in range(r1)]
        print(result)
        for i in range(r1):
            for (col1, val1) in mat1_map.get(i, []):
                for (j, val2) in mat2_map.get(col1, []):
                    result[i][j] += val1 * val2

        return result
