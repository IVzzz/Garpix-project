# Garpix-project

Входные данные:
{
   "version": 2,
   "put_cargos": [],
   "cargo_space": {
       "id": "1111",
       "mass": 20,
       "size": {
           "width": 800,
           "height": 2300,
           "length": 1200
       },
       "params": {
           "protrusion": {
               "width": 0,
               "length": 0
           },
           "indentation": {
               "width": 0,
               "length": 0
           }
       },
       "carrying_capacity": 800000
   },
   "cargo_groups": [
       {
           "mass": 6357,
           "size": {
               "width": 190,
               "height": 237,
               "length": 260
           },
           "sort": 1,
           "count": 1,
           "group_id": "11111",
           "stacking": true,
           "turnover": true,
           "overhang_angle": 50,
           "stacking_limit": 0,
           "stacking_is_limited": false
       }
   ],
   "calculation_params": {
       "packing_side": 0,
       "calculation_id": "11111",
       "accounting_center_of_mass": false
   }
}
Где:
cargo space - параметры грузового пространства
mass - собственный вес ГП (в кг)
size - размер ГП (в мм)
carrying_capacity - грузоподъемность
cargo_groups - список групп одинаковых грузов
mass - вес груза (в гр)
size - размер груза (в мм)
sort - порядковый номер группы на конвейере
count - количество одинаковых грузов
group_id - идентификатор группы
stacking - штабелирование
turnover - кантование
серым отмечены доп поля, не влияющие на решение задачи и ее оценку
 
Выходные данные:
{
   "cargoSpace": {
       "loading_size": {
           "height": 2.2,
           "length": 1.2,
           "width": 0.8
       },
       "position": [
           0.6,
           1.1,
           0.4
       ],
       "type": "pallet"
   },
   "cargos": [
       {
           "calculated_size": {
               "height": 0.4,
               "length": 0.15,
               "width": 0.4
           },
           "cargo_id": "22222",
           "id": 0,
           "mass": 1.0,
           "position": {
               "x": 0.2015,
               "y": 0.2015,
               "z": 0.0765
           },
           "size": {
               "height": 0.4,
               "length": 0.4,
               "width": 0.15
           },
           "sort": 1,
           "stacking": true,
           "turnover": true,
           "type": "box"
       }
   ],
   "unpacked": [
       {
           "group_id": "22222",
           "id": 20,
           "mass": 1.0,
           "position": {
               "x": -4.0,
               "y": 0.5,
               "z": -2.0
           },
           "size": {
               "height": 1.4,
               "length": 1.5,
               "width": 1.4
           },
           "sort": 1,
           "stacking": true,
           "turnover": true
       }
   ]
}
Где:
cargoSpace - параметры грузового пространства
loading_size - размер ГП (в м)
carrying_capacity - грузоподъемность
cargos - список упакованных грузов
mass - вес груза (в кг)
size - размер груза (в м)
calculated_size - расчитанный размер груза с учетом поворота (в м)
sort - порядковый номер группы на конвейере
count - количество одинаковых грузов
cargo_id - идентификатор группы
stacking - штабелирование
turnover - кантование
position - позиция груза (в м) (доп примечание ниже)
unpacked - список неупакованных грузов
поля соответствуют cargos
