import sys
sys.setrecursionlimit(10**9)  # 재귀 깊이 제한을 높임
input = sys.stdin.readline
result=[]
def post_order(start, end):
    if start > end:  # 시작 지점이 끝 지점보다 크면 리턴
        return
    root = pre[start]  # 현재 서브트리의 루트
    idx = start + 1

    # 오른쪽 서브트리의 시작 지점을 찾음
    while idx <= end:
        if pre[idx] > root:
            break
        idx += 1

    # 왼쪽 서브트리
    post_order(start + 1, idx - 1)
    # 오른쪽 서브트리
    post_order(idx, end)

    # 현재 노드 출력
    print(root)


pre = []
while True:
    try:
        pre.append(int(input()))
    except:
        break

post_order(0, len(pre) - 1)