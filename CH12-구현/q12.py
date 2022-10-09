# 다음을 통해 테스트합니다 https://school.programmers.co.kr/learn/courses/30/lessons/60061

# class Pillar:
#     def __init__(self, x1, y1, x2, y2):
#         self.top = [x1, y1]
#         self.bottom = [x2, y2]

# class Floor:
#     def __init__(self, x1, y1, x2, y2):
#         self.left = [x1, y1]
#         self.right = [x2, y2]

# def canAddPillar(item, pillarSet, floorSet):
#     if(item[1] == 0):
#         return True
#     for pillar in pillarSet:
#         if(pillar.top[0] == item[0] and pillar.top[1] == item[1]):
#             return True
#     for floor in floorSet:
#         if(floor.left[0] == item[0] and floor.left[1] == item[1]):
#             return True
#         elif(floor.right[0] == item[0] and floor.right[1] == item[1]):
#             return True
#     return False

# def canAddFloor(item, pillarSet, floorSet):
#     for pillar in pillarSet:
#         if(pillar.top[0] == item[0] and pillar.top[1] == item[1]):
#             return True
#         elif(pillar.top[0] == item[0] + 1 and pillar.top[1] == item[1]):
#             return True
#     for floor in floorSet:
#         if(floor.right[0] == item[0] and floor.right[1] == item[1]):
#             for floor in floorSet:
#                 if(floor.left[0] == item[0] + 1 and floor.left[1] == item[1]):
#                     return True
#     return False

# def deletePillar(item, pillarSet, floorSet):
#     for pillar in pillarSet:
#         if(pillar.bottom[0] == item[0] and pillar.bottom[1] == item[1] + 1):
#             return 0
#     cnt = 0
#     for floor in floorSet:
#         if((floor.left[0] == item[0] and floor.left[1] == item[1] + 1) or (floor.right[0] == item[0] and floor.right[1] == item[1] + 1)):
#             cnt += 1
#     if(cnt > 0):
#         return 0
#     pillarIndex = 0
#     for idx, pillar in enumerate(pillarSet):
#         if(pillar.bottom[0] == item[0] and pillar.bottom[1] == item[1]):
#             pillarIndex = idx
#             break;
#     pillarSet.pop(pillarIndex)
#     return 0

# def deleteFloor(item, pillarSet, floorSet):
#     cond1, cond2, cond3 = [0, 0, 0]

#     for pillar in pillarSet:
#         if(pillar.bottom[0] == item[0] + 1 and pillar.bottom[1] == item[1]):
#             cond1 = 1
#         elif(pillar.top[0] == item[0] + 1 and pillar.top[1] == item[1]):
#             cond2 = 1
#     for floor in floorSet:
#         if(floor.left[0] == item[0] + 1 and floor.left[1] == item[1]):
#             cond3 = 1
#     if(cond1 and not cond2 and not cond3):
#         return 0
#     elif(not cond1 and not cond2 and cond3):
#         return 0

#     floorIndex = 0
#     for idx, floor in enumerate(floorSet):
#         if(floor.left[0] == item[0] and floor.left[1] == item[1]):
#             floorIndex = idx
#             break
#     floorSet.pop(floorIndex)

#     return 0

# def solution(n, build_frame):
#     pillarSet = []
#     floorSet = []

#     if(build_frame[0][2] == 1):
#         floorSet.append(Floor(build_frame[0][0], build_frame[0][1], build_frame[0][0]+1, build_frame[0][1]))
#     else:
#         pillarSet.append(Pillar(build_frame[0][0], build_frame[0][1] + 1, build_frame[0][0], build_frame[0][1]))

#     build_frame.pop(0)

#     for item in build_frame:
#         if(item[3] == 1 and item[2] == 0 and canAddPillar(item, pillarSet, floorSet)):
#             pillarSet.append(Pillar(item[0], item[1] + 1, item[0], item[1]))
#         elif(item[3] == 1 and item[2] == 1 and canAddFloor(item, pillarSet, floorSet)):
#             floorSet.append(Floor(item[0], item[1], item[0] + 1, item[1]))
#         elif(item[3] == 0 and item[2] == 0):
#             deletePillar(item, pillarSet, floorSet)
#         elif(item[3] == 0 and item[2] == 1):
#             deleteFloor(item, pillarSet, floorSet)

#     answer = []
#     for pillar in pillarSet:
#         answer.append([pillar.bottom[0], pillar.bottom[1], 0])
#     for floor in floorSet:
#         answer.append([floor.left[0], floor.left[1], 1])

#     answer.sort(key=lambda x: x[2])
#     answer.sort(key=lambda x: x[1])
#     answer.sort()

#     return answer

def possible(answer):
    for x, y, type in answer:
        if type == 0:
            if y == 0 or [x, y - 1, 0] in answer or [x - 1, y, 1] in answer or [x, y, 1] in answer:
                pass
            else:
                return False
        else:
            if [x, y - 1, 0] in answer or [x + 1, y - 1, 0] in answer or [x - 1, y, 1] in answer and [x + 1, y, 1] in answer:
                pass
            else:
                return False
    return True


def solution(n, build_frame):
    answer = []
    for frame in build_frame:
        x, y, type, action = frame
        if action == 1:
            answer.append([x, y, type])
            if not possible(answer):
                answer.remove([x, y, type])
            pass
        else:
            answer.remove([x, y, type])
            if not possible(answer):
                answer.append([x, y, type])
            pass
    return sorted(answer)
