import json

import nltk

import re


def cleanText(readData):
    # 텍스트에 포함되어 있는 특수 문자 제거

    text = re.sub('[-=+,#/\?:^$.@*\"※~&%ㆍ!』\\‘|\(\)\[\]\<\>`\'…》]', '', readData)
    return text


with open('output_cali') as json_file:
    json_data = json.load(json_file)
    hash_tag_all = []
    com_hash_tag = []

    for i in json_data:
        try:
            hash_tag = i['description']  # 해시태그만 추출
        except KeyError:  # 해시태그가 없는 데이터도 있어서 제거함
            continue

        hash_tag = hash_tag.split('#')  # 해시태그로 스플릿
        hash_tag = hash_tag[1:]  # 첫번째 원소는 해시태그가 아닌 설명문장이 있으므로 2번째 원소부터 사용
        if len(hash_tag) == 0:
            continue
        hash_tag = [line.replace('\n', '').replace(' ', '') for line in hash_tag]
        hash_tag = [cleanText(line) for line in hash_tag]
        for line in hash_tag:
            if len(line) >= 50:
                hash_tag.remove(line)

        hash_tag_all.extend(hash_tag)  # 계속 합치기

    for line in hash_tag_all:
        text = re.sub('[^a-zA-Z]', '', line)
        text = text.lower()
        if ('' != text) & ('california' != text):  # 공백 제거
            com_hash_tag.append(text)

    unsorted_dic = {}  # 이 밑으로는 실습 2-1의 정렬코드를 이용
    temp = nltk.FreqDist(com_hash_tag)
    for w in com_hash_tag:
        unsorted_dic[temp[w]] = w

    unsorted_dic = sorted(unsorted_dic.items(), reverse=True)

    sorted_dic = {}
    for i in range(0, 50):
        sorted_dic[unsorted_dic[i][1]] = unsorted_dic[i][0]
    temp.plot(50, cumulative=False)
