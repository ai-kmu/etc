#자동완성
#9:37~11:37

#words=["go","gone","guild"]
# # words=["abc","def","ghi","jklm"]
# words=["word","war","warrior","world"]

#word의 각각의 character를 나타내는 노드
class Node:
    def __init__(self,char):
        #해당 character에 몇번 들렸는지를 나타냄
        self.character_visit_count=0
        #해당 노드가 갖고 있는 children 노드들
        self.children_nodes={}

#단어의 character를 노드 형식으로 연결하는 트리 구조
class Tree:
    def __init__(self):
        #초기화하면서 root 노드 만듬
        self.root=Node(None)

    #Tree구조에 노드를 넣는 함수
    def insert(self,str):
        node=self.root
        for char in str:
            #노드 방문 할 때마다 방문횟수 1씩 증가
            node.character_visit_count+=1
            #만약 지금 넣으려는 character과 매칭되는 child 노드가 없다면
            if char not in node.children_nodes:
                #새로운 character 노드를 만들어서 children 노드 dictionary에 추가함
                node.children_nodes[char]=Node(char)
            #가리키는 노드의 위치를 해당 character의 노드로 변경
            node=node.children_nodes[char]

        #마지막 노드 방문횟수 1씩 증가(위의 for문에서 마지막 노드는 생성만 하고 방문횟수는 안 올려줬음)
        node.character_visit_count+=1



def solution(words):
    answer = 0

    #단어들 입력
    tree=Tree()
    for word in words:
        tree.insert(word)

    #answer 계산하기
    #주어진 단어들 돌면서
    for word in words:
        #각각의 단어를 자동완성하는데 몇개의 character를 쳐야하는지 count하는데 사용하는 변수
        count=0
        #현재 가리키는 노드를 root노드로 함
        current_node = tree.root
        #해당 단어의 character를 돌면서
        for char in word:
            #현재 가리키는 노드를 현재 character에 해당하는 노드로 함
            current_node = current_node.children_nodes[char]
            #한번 character를 쳤으니 count값 1증가
            count +=1
            #만약 이 character를 방문한 횟수가 1번이면 지금 자동완성이 된다는 뜻이니 해당 단어에서의 count 종료
            if current_node.character_visit_count==1:
                break


        # print("/")
        # print(count)
        #답에 해당 단어가 몇개의 character를 쳐야 되는지 더해줌
        answer+=count


    #print(answer)
    return answer

# if __name__ == '__main__':
#     solution(words)