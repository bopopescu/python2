"""
    三維串列的練習-rain
    輸入一字串，字串為”all” 表示計算60個月的總平均降雨量，”year”、”season”和

    ”month”分別表示計算某年、某季或某月的平均降雨量。若為後三者，再輸入一
    個正整數表示那一年、那一季或那一月。
    說明：5年12個月的降雨量以三維陣列形式事先給好60個浮點數
    需做誤錯處理：
    a. 輸入除了”all”、”year”、”season”和”month”以外的字串
    b. 若輸入”year”，而正整數輸入1至5以外的數字
    c. 若輸入”season”，而正整數輸入1至4以外的數字
    d. 若輸入”month”，而正整數輸入1至12以外的數字
    """
import random

def mk_list():
        fall_list = []
        for i in range(5):
            fall_list.append([])
            for j in range(4):
                fall_list[i].append([])
                for k in range(3):
                    fall_list[i][j].append(round(random.uniform(1, 15), 1))
        return fall_list

    def list_into_onemean(l):
        total = 0
        for i in range(len(l)):
            total += l[i]
        return total / len(l)

    def rawtotal_all(l):
        mean_in_years = []
        mean_in_seasons = []
        for i in range(len(l)):
            mean_in_season = []
            for j in range(len(l[i])):
                k = list_into_onemean(l[i][j])
                # print(i, j, list_into_onemean(l[i][j]))
                mean_in_season.append(k)
            k = list_into_onemean(mean_in_season)
            mean_in_years.append(k)
            mean_in_seasons.append(mean_in_season)
        k = list_into_onemean(mean_in_years)
        return k, mean_in_years, mean_in_seasons

    def do_round(l):

        k = []
        for i in range(len(l)):
            k.append(round(l[i], 1))
        return k

    def safe_key(x, y):

        key = {'all': [], 'year': range(1, 6), 'season': range(1, 5), 'month': range(1, 13)}

        if x in key and y in key[x]:
            return True
        else:
            return False
        print(safe_key(time, time_index))

    # print('檢查', safe_key2('season',4))

    make_data_list = mk_list()

    mean_of_all, mean_of_years, mean_of_seasons = rawtotal_all(make_data_list)

    def list_output(time,time_index):

        if time == 'season':
            return do_round(mean_of_seasons[time_index])
        elif time == 'year':
            return do_round(mean_of_years[time_index])

    def safe_input():

        print('all','year','season',sep='\n')

        time = input('Enter the time you want to search:').strip()

        if time.strip() == 'all':
            print('The resault of all is:')
            print(round(mean_of_all, 1))

        else:
            time_index = eval(input('Enter the index:'))

            if safe_key(time, time_index):
                print('The resault of {} {}'.format(time,time_index))
                print(list_output(time,time_index))

            else:
                print('Your input is wrong, please try again.')
                main()
    safe_input()


main_4()