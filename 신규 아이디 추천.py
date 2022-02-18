# 입력 값을 받아 신규 아이디 추천
def solution(new_id):

#1단계 (모든 대문자를 대응되는 소문자로 치환)
    new_id = new_id.lower()

#2단계 (특수문자 '~!@#$%^&*()=+[{]}:?,<>/'를 제거)
    new_id = [*new_id]
    Asterisk = ['~', '!', '@', '#', '$', '%', '^', '&', '*',
            '(', ')', '=', '+', '[', '{', ']', '}', ':', '?', ',',                 '<', '>', '/']
    for char in new_id:
        for i in Asterisk:
            if i == char:
                new_id[new_id.index(char)] = ''
    new_id = ''.join(new_id)

#3단계 (마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환)
    while new_id.count('..') > 0:
        new_id = new_id.replace('..','.')

#4단계 (마침표(.)가 처음이나 끝에 위치한다면 제거)
    new_id = [*new_id]
    if '.' in new_id[0]:
        new_id[0] = ""
    if '.' in new_id[-1:]:
        new_id[-1:] = ""
    new_id = ''.join(new_id)
    
#5단계 (빈 문자열이라면, new_id에 "a"를 대입)
    if bool(new_id):
        pass
    else:
        new_id = "a"
#6단계 (길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거)
    if len(new_id) >= 16:
        new_id = new_id[:15]
    
#4단계 (마침표(.)가 처음이나 끝에 위치한다면 제거)
    new_id = [*new_id]
    if '.' in new_id[0]:
        new_id[0] = ""
    if '.' in new_id[-1:]:
        new_id[-1:] = ""
    new_id = ''.join(new_id)

#7단계 (new_id의 길이가 2자 이하라면, new_id의 마지막 문자를 new_id의 길이가 3이 될 때까지 반복해서 끝에 붙임)
    while len(new_id) <= 2:
        new_id = new_id+new_id[-1:]
    return new_id