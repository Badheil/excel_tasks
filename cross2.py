import pandas as pd
import numpy as np
entit = {
    'Росморречфлот': 'Федеральное агентство морского и речного транспорта',
    'Ространснадзор': 'Федеральная служба по надзору в сфере транспорта',
    'Роснедра': 'Федеральное агентство по недропользованию',
    'Минпросвещения России': 'Министерство просвещения Российской Федерации',
    'Россельхознадзор': 'Федеральная служба по ветеринарному и фитосанитарному надзору',
    'ФТС России': 'Федеральная таможенная служба',
    'Росавтодор': 'Федеральное дорожное агентство',
    'ФССП России': 'Федеральная служба судебных приставов',
    'ФСТЭК России': 'Федеральная служба по техническому и экспортному контролю',
    'Росстандарт': 'Федеральное агентство по техническому регулированию и метрологии',
    'Росводресурсы': 'Федеральное агентство водных ресурсов',
    'Росархив': 'Федеральное архивное агентство',
    'МИД России': 'Министерство иностранных дел Российской Федерации',
    'Минэкономразвития России': 'Министерство экономического развития Российской Федерации',
    'Ростехнадзор': 'Федеральная служба по экологическому, технологическому и атомному надзору',
    'Росреестр': 'Федеральная служба государственной регистрации, кадастра и картографии',
    'Росфинмониторинг': 'Федеральная служба по финансовому мониторингу',
    'Ростуризм': 'Федеральное агентство по туризму',
    'ФСО России': 'Федеральная служба охраны Российской Федерации (федеральная служба)',
    'Минздрав России': 'Министерство здравоохранения Российской Федерации'
}
data1 = {'Организация_сокращенно': [
    'Росморречфлот',
    'Ространснадзор', 
    'Роснедра', 
    'Минпросвещения России', 
    'Россельхознадзор', 
    'ФТС России', 
    'Росавтодор', 
    'ФССП России', 
    'ФСТЭК России', 
    'Росстандарт', 
    'Росводресурсы', 
    'Росархив', 
    'МИД России', 
    'Минэкономразвития России', 
    'Ростехнадзор', 
    'Росреестр', 
    'Росфинмониторинг', 
    'Ростуризм', 
    'ФСО России', 
    'Минздрав России']}

df_cross = pd.read_excel('Тест_4_cross2.xlsx')
df_unload = pd.read_excel('Тест_4_unload2.xlsx')

sum_unload = df_unload.groupby('Организация')['Количество'].sum()
for short_name, full_name in entit.items():
    if full_name in sum_unload.index:
        df_cross.loc[df_cross['Ответственная организация'] == short_name, 'Фактические данные'] = sum_unload[full_name]
    else:
        print(f"Warning: Full name '{full_name}' not found in unload2.xlsx")
df_cross['Общее количество заявлений о предоставлении услуги'] = df_cross['Общее количество заявлений о предоставлении услуги'].astype('int')
df_cross['Фактические данные'] = df_cross['Фактические данные'].astype('int')
df_cross['да/нет'] = np.where(df_cross['Общее количество заявлений о предоставлении услуги'] == df_cross['Фактические данные'], 'да','нет')
new_data = {
    'Ответственная организация' : 'Министерство энергетики Российской Федерации',
    'Общее количество заявлений о предоставлении услуги' : 0,
    'Фактические данные' : sum_unload['Министерство энергетики Российской Федерации'],
    'да/нет' : 'нет'
}
df_cross = df_cross._append(new_data, ignore_index= True)


# df_cross.to_excel('cross2_complete.xlsx')





