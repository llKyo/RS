import pandas as pd
from datetime   import datetime
from pathlib    import Path
# Imports Internos
from f_dataframes import *

if __name__ == '__main__':
    
    now   = datetime.now().strftime("%Y%m%d_%H%M%S")
    # tabla = input('\nNombre de Tabla: ')
    tabla = 'TEST'
    
    df1 = pd.read_excel(  'original.xlsx'  )
    df2 = pd.read_excel( 'modificado.xlsx' )
    
    print('\n[INFO] Procesando...\n')
    dfConcatVertical    = concatVertical ( df1, df2 )
    dfCompararPorFila   = compararPorFila( df1, df2 )
    dfDuplicado         = duplicados     ( df1, df2 )
    dfDistintos         = distintos   ( df1, df2 )
    
    nombreExcel = now + ' - ' + tabla
    path        = './documents/'
    Path(path).mkdir(parents=True, exist_ok=True)
    
    with pd.ExcelWriter(path + nombreExcel + '.xlsx') as writer:
        df1.to_excel(writer, sheet_name='Original')
        df2.to_excel(writer, sheet_name='Modificada')
        dfConcatVertical.to_excel( writer, sheet_name='Concatenado')
        dfCompararPorFila.to_excel( writer, sheet_name = 'ComparadoPorFila' )
        dfDuplicado.to_excel(writer, sheet_name='Duplicados')
        dfDistintos.to_excel(writer, sheet_name='Distintos')

print('\nDone! 🐤\n')