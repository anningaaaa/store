import xlrd
an = xlrd.open_workbook(filename='2020年每个月的销售情况.xlsx',encoding_override=True)
store = {}
'''
    存储结构：
        风衣：{
            "sum_money":xxxx,  # 总销售额
            "sum_count":xxx,   # 总销售量
        },
        "羽绒服":{
            "sum_money":xxx,
            "sum_count":xxxxx,    
        }
'''
nsheet = an.nsheets
for i in range(nsheet):
    st = an.sheet_by_index(i)
    nrow = st.nrows
    for j in range(1,nrow):
        cell = st.row_values(j)
        if cell[1] in store:
            store[cell[1]]={
                "sum_money":round(store[cell[1]]["sum_money"] + cell[2] * cell[4],2),
                "sum_count":int(store[cell[1]]["sum_count"] + cell[4])
            }
        else:
            store[cell[1]] = {
                "sum_money":round(cell[2] * cell[4],2),
                "sum_count":int(cell[4])
            }
all_sum = sum(store[item]["sum_money"] for item in store)
all_count = sum(store[item]["sum_count"] for item in store)
print("\033[1;35m全年的统计总销售额：￥\033[0m",round(all_sum,2))
print("\033[1;35m全年的统计总销售量：\033[0m",round(all_count,2),"件！")
for name in store:
    print("\033[1;33m------------------------------------------\033[0m")
    print("\033[1;32m",name,"的销售额占比为：\033[0m",round(store[name]["sum_money"] / all_sum * 100,2),"%")
    print("\033[1;34m",name,"的销售量占比为：\033[0m", round(store[name]["sum_count"] / all_count * 100,2), "%")