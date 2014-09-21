# -*- coding: utf-8 -*-

def isoddtype(mabang_type):
    return mabang_type % 2

def isoutofsize(size, row, column):
    if size <= row or size <= column:   return 1
    else: return 0

def isendofrowavalilable(size_of_mabang, current_column_position):
    if size_of_mabang > current_column_position:
        if mabangjean[0][current_column_position] == 0: return 1
    else: return 0

def isendofcolumnavalilable(size_of_mabang, current_row_position):
    if size_of_mabang > current_row_position:
        if mabangjean[current_row_position][0] == 0: return 1
    else: return 0

def iscurrentpostionavalaible(current_row_position, current_column_position):
    if mabangjean[current_row_position][current_column_position] == 0: return 1
    else: return 0


print "마마, 마방진의 크기를 말씀해 주십시요. "

continue_flag = 1

while (continue_flag  ==1):
    print "마방진의 크기를 입력하세요: ",
    size_of_mabang = int(raw_input())
    while size_of_mabang < 3:
        print "마방진 크기는 2보다 커야  합니다"
        print "마방진의 크기를 입력하세요: ",
        size_of_mabang = int(raw_input())

    print size_of_mabang, "크기의 마방진은 아래와 같습니다"
    mabangjean = []
    row = []

    for i in range(size_of_mabang):
        for j in range(size_of_mabang):
            row.append(0)
        mabangjean.append(row)
        row = []

    total_number = size_of_mabang * size_of_mabang
    current_row_position = 0
    current_column_position = 0

    if isoddtype(size_of_mabang):
        for i in range(1, total_number + 1):
            if i == 1:
                current_row_position = size_of_mabang - 1
                current_column_position = size_of_mabang / 2
                mabangjean[current_row_position][current_column_position] = i
            else:
                current_row_position  = current_row_position + 1
                current_column_position = current_column_position + 1
                if isoutofsize(size_of_mabang, current_row_position , current_column_position):
                    if isendofrowavalilable(size_of_mabang, current_column_position):
                        current_row_position = 0

                        if iscurrentpostionavalaible(current_row_position, current_column_position):
                            mabangjean[current_row_position][current_column_position] = i
                        else:
                            mabangjean[current_row_position-1][current_column_position] = i
                            continue

                    elif isendofcolumnavalilable(size_of_mabang, current_row_position):
                        current_column_position = 0
                        if iscurrentpostionavalaible(current_row_position, current_column_position):
                            mabangjean[current_row_position][current_column_position] = i
                            continue
                        else:
                            mabangjean[current_row_position-1][current_column_position] = i
                            continue
                    else:
                        current_row_position  = current_row_position - 2
                        current_column_position = current_column_position - 1
                        mabangjean[current_row_position][current_column_position] = i


                else:
                    if iscurrentpostionavalaible(current_row_position, current_column_position):
                         mabangjean[current_row_position][current_column_position] = i
                    else:
                        current_row_position  = current_row_position - 2
                        current_column_position = current_column_position - 1
                        mabangjean[current_row_position][current_column_position] = i



    else:
        for i in range(1, total_number + 1):
            if i == 1:
                current_row_position = 0
                current_column_position = 0
                mabangjean[current_row_position][current_column_position] = i
                continue
            else:
                current_column_position = current_column_position  + 1



                if current_column_position  == size_of_mabang:
                    current_row_position = current_row_position +1
                    current_column_position = 0

                revers_column_position = abs(current_column_position - size_of_mabang+1)

                if current_row_position == current_column_position or \
                   current_row_position ==  revers_column_position:
                    mabangjean[current_row_position][current_column_position] = i
                    continue


                if current_row_position == 0 and current_column_position == size_of_mabang-1:
                    mabangjean[current_row_position][current_column_position] = i
                    continue

                if current_row_position == size_of_mabang-1:
                    if current_column_position == 0:
                        mabangjean[current_row_position][current_column_position] = i
                        continue
                    elif current_column_position == size_of_mabang-1:
                        mabangjean[current_row_position][current_column_position] = i
                        continue


        current_row_position = size_of_mabang - 1
        current_column_position = size_of_mabang - 1
        for i in range(1, total_number+1):


            if iscurrentpostionavalaible(current_row_position, current_column_position):
                mabangjean[current_row_position][current_column_position] = i


            current_column_position = current_column_position - 1
            if current_column_position  == -1:
                current_row_position = current_row_position -1
                current_column_position =size_of_mabang - 1


    for row in mabangjean:
        for value in row:
            print value, "\t",
        print

    while 1:
        print  "한판더 하시렵니까[Y/n]"
        continue_code = str(raw_input()).upper()
        if (continue_code == 'Y'):
            break
        elif (continue_code == 'N'):
            print "편히 쉬십시요. 마마"
            continue_flag = 0
            break
        else:
            print "Y나 N을 입력해주시기 바랍니다."


