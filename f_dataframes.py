import pandas as pd

def compararPorFila(dfOri, dfMod):
    
    dfOriAux = dfOri.copy()
    dfModAux = dfMod.copy()
    
    dfOriAux['TABLA'] = 'ORI'
    dfModAux['TABLA'] = 'MOD'
    
    dfCompararPorFila = dfOriAux.compare(dfModAux, keep_shape=True, keep_equal=True)
    
    print('[ OK ] ComparadoPorFila')
    return dfCompararPorFila

def concatVertical(dfOri, dfMod):
    
    dfOriAux = dfOri.copy()
    dfModAux = dfMod.copy()
    
    dfOriAux['TABLA'] = 'ORI'
    dfModAux['TABLA'] = 'MOD'
    dfConcatVertical = pd.concat([dfOriAux,dfModAux], axis=0)#.drop_duplicates(keep=False)
    
    print('[ OK ] Concatenado')
    return dfConcatVertical

def duplicados(dfOri, dfMod):
    
    oKeys = dfOri.keys()

    dfConcatVertical = pd.concat([dfOri,dfMod], axis=0)
    
    df = dfConcatVertical[dfConcatVertical[oKeys].duplicated(keep='last')].drop_duplicates(keep='last')
    
    print('[ OK ] Duplicados')
    return df

def distintos(dfOri, dfMod):
    
    oKeys = dfOri.keys()

    dfConcatVertical = pd.concat([dfOri,dfMod], axis=0)
        
    df = dfConcatVertical.drop_duplicates(keep=False)
    
    print('[ OK ] No Duplicados')
    return df

