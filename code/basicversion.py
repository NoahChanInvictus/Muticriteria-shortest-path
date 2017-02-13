# -*- coding:utf-8 -*-
# Dijkstra's algorithm for multicriteria shorest path
# Noah Chan, Polytech Tours, Feb. 2017


import os
import csv
import timeuseage

def openfiles(node_file, arc_file):

    print('Current path:',os.getcwd())

    try:
        with open('../graphes/graphes/'+node_file) as node_f:
            node_csv = csv.reader(node_f)
            headers = next(node_csv)     #读取各列表头名称
            #print(headers)
            node_dict = {}
            for row in node_csv:
                temp_list = str(row).split('\\t')
                node_id = temp_list[0].strip("[]'")
                longtitude = temp_list[1]
                latitude = temp_list[2].strip("[]'")
                node_dict[node_id] = [longtitude,latitude]

        with open('../graphes/graphes/'+arc_file) as arc_f:
            node_csv = csv.reader(arc_f)
            headers = next(node_csv)     #读取各列表头名称
            #print(headers)
            arc_dict = {}
            for row in node_csv:
                temp_list = str(row).split('\\t')
                source = temp_list[0].strip("[]'")
                target = temp_list[1]
                length = temp_list[2]
                danger = temp_list[3].strip("[]'")
                if source not in arc_dict.keys():
                    arc_dict[source] = {target:[length,danger]}
                else:
                    arc_dict[source][target] = [length,danger]
                #print(source,target,length,danger)

        return node_dict, arc_dict


    except:
        print('Open files error')
        exit()

def Dijkstra(node_dict, arc_dict, source, target):

    #字符串整数化
    source = int(source)
    target = int(target)


    #initialization for the Dijkstra algorithm
    node_num = len(node_dict)
    dis = [float('inf')] * node_num
    dis[source] = 0
    flag = [False] * node_num     #define if the vertex has been explored
    pre = ['Unknown'] * node_num
    iternode = source
    #LC is the list of candidate for compare
    #LC = {str(iternode):['0','0']}
    # # ***************
    # # 测试代码
    # control = 0
    # #****************
    while iternode != target:
        LC = {}
        #从当前点出发找出所有直接相连的点加入LC
        try:
            for i in arc_dict[str(iternode)]:       #如果当前结点没有出度会报错
                LC[i] = arc_dict[str(iternode)][i]
        except:
            pass
        dis_iter = dis[iternode]
        #更新相连点的dis[i]

        #del LC[str(iternode)]
        flag[iternode] = True
        for (k,j) in LC.items():
            if dis[int(k)] > dis_iter + int(j[0]):
                dis[int(k)] = dis_iter + int(j[0])
                pre[int(k)] = iternode

        #从D[]里找出距离最短并且没有被explored的下一个点

        # for i in sorted(dis):
        #     #这里存在问题 如果dis中有重复值可能找到的下标不是真实位置
        #     #每一个节点都要从全部中找出最小的很慢
        #    if flag[dis.index(i)] == False:
        #         next_node = dis.index(i)
        #         print(next_node)
        #         break

        #改进版
        shortest_dist = float('inf')
        mark = True
        for (k,j) in LC.items():
            if dis[int(k)] < shortest_dist and flag[int(k)] == False:
                shortest_dist = dis[int(k)]
                next_node = int(k)
                mark = False
        if mark:
            for i in sorted(dis):
                #这里存在问题 如果dis中有重复值可能找到的下标不是真实位置
                #每一个节点都要从全部中找出最小的很慢
                if flag[dis.index(i)] == False:
                    next_node = dis.index(i)
                    print(next_node)
                    break



        iternode = next_node

        #测试代码
        #******************
        #print(LC)
        print(iternode)
        #print(mark)
        #print(flag[])
        # control += 1

        #if control == 3:
            #break
        #******************


    print('!'*99)
    #print(iternode)
    path = [iternode]
    while iternode != source:
        print(pre[iternode])
        path.append(pre[iternode])
        iternode = pre[iternode]

    return path



if __name__ == '__main__':
    starttime = timeuseage.start()
    #city = input()
    city = 'paris'
    node_file = city + '_noeuds.csv'
    arc_file = city + '_arcs.csv'
    print('Opening files:', node_file, arc_file)
    node_dict, arc_dict = openfiles(node_file, arc_file)
    print('Files opened sucessfully')
    print('Node number:', len(node_dict))
    print('Arc number', len(arc_dict))
    print('Starting initialize graph')
    source = '0'
    #target = '11300'
    target = '9999'
    #print(arc_dict)
    path = Dijkstra(node_dict, arc_dict, source, target)
    print(path)
    endtime = timeuseage.end()
    timeuse = timeuseage.timeuse(starttime, endtime)
    print('timeuseage:',timeuse,'seconds')
    #G = initialization()
