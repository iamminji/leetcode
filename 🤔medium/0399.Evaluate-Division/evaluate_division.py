# 399. Evaluate Division
# https://leetcode.com/problems/evaluate-division/

from collections import defaultdict


class Solution:

    # directed graph 문제다.
    # 각 노드 간선에는 특정 float 값이 주어지고 다음 노드로 이동할 때 마다 곱셈 연산이 된다.
    # 반대 방향의 간선은 주어진 간선의 역수다.
    def search_graph(self, s, e, graph, visited):

        if e in graph[s]:
            return True

        for s2, v2 in graph[s].items():
            if s2 not in visited:
                visited.add(s2)
                # 초기에 자기 자신도 그래프에 1.0 으로 넣어주었기 때문에 스킵한다.
                # 값을 찾은 경우 s, e 쌍의 그래프 값에 찾았던 s2, e 쌍의 간선 값과 s, s2 쌍의 값을 곱한다.
                if s != s2 and self.search_graph(s2, e, graph, visited):
                    graph[s][e] = graph[s2][e] * v2
                    return True
        return False

    def calcEquation(self, equations: 'List[List[str]]', values: 'List[float]',
                     queries: 'List[List[str]]') -> 'List[float]':

        # 주어진 값을 활용하여 그래프 형태로 만들어준다.
        # 여기선 딕셔너리로 만들어 주었다.
        # 예를 들어
        # a -> b, b -> c 에서 a -> b 간선이 2.0, b -> c 에서 간선이 3.0 이라면 딕셔너리엔 다음과 같은 값을 넣는다.
        # {'a': {'a': 1.0, 'b': 2.0}, 'b': {'a': 0.5, 'b': 1.0, 'c': 3.0}}
        #
        # 그러면 찾고자 하는 값 a -> c 가 온다면
        # a 로 시작하는 딕셔너리 {'a': 1.0, 'b': 2.0} 에서 타겟 노드를 찾고, 없으면 모든 키를 방문한다.
        # 결국 'b' 로 시작하는 값 {'a': 0.5, 'b': 1.0, 'c': 3.0} 에서 'c' 를 찾게 되고 그 값 3.0 을 리턴 하여 처음 시작했던 a -> b 의 2.0 과 곱한다.
        # 코드에선 search_graph 의 graph[s][e] = graph[s2][e] * v2 부분이다. 그리고 그 값을 'a': {'c': 6.0} 에 업데이트 한다.
        # 이런식으로 계속 반복하면서 (재방문을 막기 위한 visited 도 써가며) 주어진 queries 의 모든 간선의 값을 구한다.

        graph = defaultdict(dict)
        for nodes, v in zip(equations, values):
            # 자기 자신은 1.0 으로 업데이트 한다.
            graph[nodes[0]].update({nodes[0]: 1.0})
            graph[nodes[1]].update({nodes[1]: 1.0})

            # 주어진 간선와 그 반대 간선을 업데이트 한다.
            graph[nodes[0]].update({nodes[1]: v})
            graph[nodes[1]].update({nodes[0]: 1.0 / v})

        res = []
        # 쿼리로 그래프를 찾는다.
        for q in queries:
            visited = set()
            # q[0] -> q[1] 로 가는 간선을 찾음
            self.search_graph(q[0], q[1], graph, visited)
            
            # end (혹은 target) 노드가 그래프에 없으면 -1을 추가
            if q[1] not in graph[q[0]]:
                res.append(-1.0)
            else:
                res.append(graph[q[0]][q[1]])


        return res


if __name__ == '__main__':
    sol = Solution()
    assert sol.calcEquation([["a", "b"], ["b", "c"]], [2.0, 3.0],
                            [["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"]]) == [6.0, 0.5, -1.0, 1.0, -1.0]
