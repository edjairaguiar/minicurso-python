# Importa as dependências.
import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler

# Importa a base de dados.
churn_data = pd.read_csv('data/churn_data.csv')
print(churn_data.sample(3))

# Remove colunas pouco relevantes para o modelo.
churn_data.drop(['phone_number', 'area_code', 'state'], inplace=True, axis=1)
print(churn_data.columns,"\n")

# Divide os dados entre treinamento e teste
# bem como, entre features e atributo alvo.
X_train, X_test, y_train, y_test = train_test_split(
        churn_data.iloc[:,:-1],
        churn_data.iloc[:,-1],
        test_size=0.3,
        random_state=42
    )

# Cria variáveis dummies, convertendo as variáveis
# categóricas em numéricas de valor binário.
X_train = pd.get_dummies(X_train, prefix_sep='_', drop_first=True)
X_test = pd.get_dummies(X_test, prefix_sep='_', drop_first=True)
print(X_train.sample(3),"\n")

# Converte variável alvo em numérica (valor binário).
y_train = y_train.astype(int)
y_test = y_test.astype(int)
print(y_train.sample(3),"\n")


# Normaliza variáveis numéricas para valores entre 0 e 1.
scaler = MinMaxScaler()
X_train_norm = scaler.fit_transform(X_train)
X_test_norm = scaler.fit_transform(X_test)
X_train = pd.DataFrame(dict(zip(X_train.columns.values, X_train_norm.T)))
X_test = pd.DataFrame(dict(zip(X_test.columns.values, X_test_norm.T)))
print(X_test.sample(3),"\n")


# Cria diretório para arquivos pré-processados caso não existam.
path = 'data/preprocessed'
if not os.path.exists(path):
    os.mkdir(path)

# Salva a base de dados pré-processada e separada entre
# treinamento e teste, bem como features e variável alvo.
X_train.to_csv(f'{path}/churn_data_X_train.csv', index=False)
X_test.to_csv(f'{path}/churn_data_X_test.csv', index=False)
y_train.to_csv(f'{path}/churn_data_y_train.csv', index=False)
y_test.to_csv(f'{path}/churn_data_y_test.csv', index=False)
