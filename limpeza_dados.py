import pandas as pd

df=pd.read_csv('C:/Users/leandro/Downloads/clientes.csv')

pd.set_option('display.width',None) #para nao ocultar nenhum caracter das linhas
print('sem mudança: \n',df.head())

#remover dados
df.drop('pais',axis=1,inplace=True) # coluna
df.drop(2,axis=0,inplace=True) # linha

#normalizar campos de texto
df['nome']= df['nome'].str.title()
df['endereco']= df['endereco'].str.lower()
df['estado']= df['estado'].str.strip().str.upper()
#print(df.head())

#converter tipos de dados
df['idade']= df['idade'].astype(int)
#print(df.head())

#tratar valores nulos(ausentes)
df_fillna= df.fillna(0) # substituir valores por 0
df_dropna= df.dropna() # remover registro com valores nulos
df_dropna4= df.dropna(thresh=4) # manter registros com o minimo 4 valores nao nulos
df=df.dropna(subset=['cpf']) # remover registro com cpf nulo
print(df.head())

print('valores nulos:\n',df.isnull().sum())
print('Quatidade de registro nulos com fillna:',df_fillna.isnull().sum().sum())
print('quantidade de registros nulos com dropna',df_dropna.isnull().sum().sum())
print('quantidade de registros nulos com dropna4:',df_dropna4.isnull().sum().sum())
print('quantidade de registros nulos do cpf:',df.isnull().sum().sum())


df.fillna({'estado': 'desconhecido'}, inplace=True)
df['endereco']= df['endereco'].fillna('Endereço nao informado')
df['idade_corrigida']= df['idade'].fillna(df['idade'].mean())

#tratar formato dos dados
df['data_corrigida']= pd.to_datetime(df['data'],format='%d/%m/%Y',errors='coerce')

#tratar dados duplicados
print('quantidade de registros atual',df.shape[0])
df.drop_duplicates()
df.drop_duplicates(subset='cpf',inplace=True)
print('quantidade de registros removendo os duplicados:',len(df))

print('dados limpos: \n',df)

#salvar dataframe
df['data']= df['data_corrigida']
df['idade']= df['idade_corrigida']

df_salvar=df[['nome','cpf','idade','data','endereco','estado']]
df_salvar.to_csv('clientes_limpeza.csv',index=False)

print('Novo dataframe: \n', pd.read_csv('clientes_limpeza.csv'))