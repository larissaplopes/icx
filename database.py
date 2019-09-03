#!/usr/bin/env python
# coding: utf-8

import csv
import os

def WriteFile(userName, animalName, iD, numberTouch, leftSide, rightSide, routinePeriod, date, start, finish, minutes):
    #          0         1          2      3          4         5           6             7    8        9       10
    """
        Recebe as variáveis coletadas durante a execução de um experimento na caixa comportamental, 
        gera um novo arquivo de relatório, caso o mesmo não exista, e salva em um arquivo no formato CSV
        :param userName: nome do usuario
        :param animalName: nome do animal
        :param iD: identificador do animal
        :param numberTouch: número de vezes que o animal tocou a bara para receber recompensa
        :param leftSide: flag indicativa que barra do lado esquerdo está ativa
        :param rightSide: flag indicativa que barra do lado direito está ativa
        :param routinePeriod: duração da rotina
        :param date: data
        :param start: momento de início do experimento
        :param finish: momento de final do experimento
        :param minutes: duração em minutos
        
    """
    
    if not "Relatorio.csv" in os.listdir():
        with open("Relatorio.csv", "w") as f:
            pass

#                    0            1            2               3                  4                  5              
    columnsName = ["User_Name", "Animal_Name", "Animal_ID", "Number_Touch", "Left_Side_Lever", "Right_Side_Lever", 
                   "Routine_Period", "Date", "Start", "Finish", "Elapsed_Time_Minutes"]
#                    6                 7       8         9       10

    if os.stat("Relatorio.csv").st_size == 0:
        with open("Relatorio.csv", "w") as f:

            writer = csv.DictWriter(f, fieldnames = columnsName)
            writer.writeheader()
            writer.writerow({columnsName[0]: userName, columnsName[1]: animalName, 
                             columnsName[2]: iD, columnsName[3]: numberTouch, 
                             columnsName[4]: leftSide, columnsName[5]: rightSide, 
                             columnsName[6]: routinePeriod, columnsName[7]: date, 
                             columnsName[8]: start, columnsName[9]: finish, 
                             columnsName[10]: minutes})
    else:
        with open("Relatorio.csv", "a") as f:
            writer = csv.DictWriter(f, fieldnames = columnsName)
            writer.writerow({columnsName[0]: userName, columnsName[1]: animalName, 
                             columnsName[2]: iD, columnsName[3]: numberTouch, 
                             columnsName[4]: leftSide, columnsName[5]: rightSide, 
                             columnsName[6]: routinePeriod, columnsName[7]: date, 
                             columnsName[8]: start, columnsName[9]: finish, 
                             columnsName[10]: minutes})


"""
  Exemplo de execução do método
"""

WriteFile("Larissa", "Rato1", 1, 5, 4, 3, 30,"2018-05-12",  2, 50, 30)
WriteFile("Larissa", "Rato2", 1, 5, 4, 3, 30,"2018-05-12",  2, 50, 30)

