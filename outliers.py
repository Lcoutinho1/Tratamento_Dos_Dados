import pandas as pd
from scipy import stats

pd.set_option('display.width',None)

df=pd.read_csv('clientes_limpeza.csv')

df_filtro_basico= df[df['idade']>100]

print('Filtro basico \n',df_filtro_basico[['nome','idade']])

#indentificar outliers com Z-score
z_scores= stats.zscore(df['idade'].dropna())
outliers_z= df[z_scores >=3]
print('outliers pelo zscore: \n', outliers_z)

#filtrar outliers com zscore
df_zscore= df[(stats.zscore(df['idade'])<3)]
#print('df_zscore \n',df_zscore)
#identificar outliers com IQR
Q1= df['idade'].quantile(0.25)
Q3= df['idade'].quantile(0.75)
IQR= Q3 - Q1

limite_baixo=Q1  -1.5*IQR
limite_alto= Q3 + 1.5*IQR

print('limites IQR: ',limite_baixo,limite_alto)

outliers_iqr= df[(df['idade']< limite_baixo)  | (df['idade']> limite_alto)]
print('outliers pelo IQR:\n', outliers_iqr)

#filtar outliers com IQR
df_iqr= df[(df['idade']>= limite_baixo) & (df['idade'] <= limite_alto)]

limite_baixo=1
limite_alto=100
df= df[(df['idade']>= limite_baixo) & (df['idade'] <= limite_alto)]
#filtar endereço invalido
df['endereco']= df['endereco'].apply(lambda x: 'endereço invalido' if len(x.split('\n'))<3 else x)

# tratar campos de texto
df['nome']= df['nome'].apply(lambda x: 'nome invalido' if isinstance(x,str) and len(x) >50 else x)
print('qquantidades de registros com nomes grande: ',(df['nome'] == 'nome invalido').sum())

print('dados com outliers tratados:\n ',df)


#salvar dataframe
df.to_csv('clientes_remove_outliers',index=False)