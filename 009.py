# 009 - Brute Force 2

def find_subset_sum(N, A, S):
    # 初期化
    DP = [[False] * (S + 1) for _ in range(N + 1)]
    DP[0][0] = True

    # 選択状況を追跡する2次元配列
    choices = [[[] for _ in range(S + 1)] for _ in range(N + 1)]

    # 動的計画法による漸化式の計算
    for i in range(1, N + 1):
        for j in range(S + 1):
            DP[i][j] = DP[i - 1][j]
            choices[i][j] = choices[i - 1][j]
            if j >= A[i - 1]:
                if DP[i - 1][j - A[i - 1]]:
                    DP[i][j] = True
                    choices[i][j] = choices[i - 1][j - A[i - 1]] + [A[i - 1]]

    # 組み合わせの表示
    if DP[N][S]:
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    N, S = map(int, input().split())
    A = list(map(int, input().split()))

    # 関数呼び出し
    find_subset_sum(N, A, S)
