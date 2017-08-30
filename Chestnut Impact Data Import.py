import openpyxl as xl
import numpy as np

# imports Diana's Simapro Impact Data
wb = xl.load_workbook(r'C:\Users\Ian\Dropbox\iSEE_Woody_Polyculture_Shared\life_cycle_assessment_spreadsheets\Chestnut LCA.xlsx')
sheet = wb.get_sheet_by_name('SimaPro CONT')

# creates library of Inventory Item Categories (as strings) and Impact Categories (as arrays) from B46 to N56 of Diana's data
impact = {}
for y in range(46, 57):
    name = sheet['B'+str(y)].value
    impacts = []
    for x in range (5, 15):
        value = sheet.cell(row = y, column= x).value
        impacts.append(value)
    fark = np.array(impacts)
    impact[name]= fark

# testing an array
derp=impact['Urea, as N {RER}| production | Alloc Def, U']*2

#printing the dictionary and the array test
print(impact)
print('derp=' + str(derp))