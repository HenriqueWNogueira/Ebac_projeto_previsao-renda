import streamlit as st 
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import statsmodels.api as sm
import statsmodels.formula.api as smf

from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split


st.set_page_config(
    page_title='Modelo de regressão - Previsão de renda',
    page_icon='⚙')


renda = pd.read_csv('./input/previsao_de_renda.csv')

renda.drop(columns= ['Unnamed: 0', 'id_cliente', 'data_ref', 'idade'], inplace= True)
renda['tempo_emprego'].fillna(0, inplace=True) 
renda = renda[renda['renda'] < 20000]  
renda = renda[renda['qtd_filhos'] < 14] 

df = renda.copy(deep=True)



df_dummies = pd.get_dummies(data= df.dropna(), drop_first= True).astype(int)

X = df_dummies.drop(columns='renda')
y = df_dummies['renda']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)




def stepwise_selection(X, y, 
                       initial_list=[], 
                       threshold_in=0.05, 
                       threshold_out = 0.05, 
                       verbose=True):
  
    included = list(initial_list)
    while True:
        changed=False
        
        # forward step
        excluded = list(set(X.columns)-set(included))
        new_pval = pd.Series(index=excluded, dtype=np.dtype('float64'))
        for new_column in excluded:
            model = sm.OLS(y, sm.add_constant(pd.DataFrame(X[included+[new_column]]))).fit()
            new_pval[new_column] = model.pvalues[new_column]
        best_pval = new_pval.min()
        if best_pval < threshold_in:
            best_feature = new_pval.index[new_pval.argmin()]
            included.append(best_feature)
            changed=True
            if verbose:
                 print('Add  {:30} with p-value {:.6}'.format(best_feature, best_pval))

        # backward step
        print("#############")
        print(included)
        model = sm.OLS(y, sm.add_constant(pd.DataFrame(X[included]))).fit()
        # use all coefs except intercept
        pvalues = model.pvalues.iloc[1:]
        worst_pval = pvalues.max() # null if pvalues is empty
        if worst_pval > threshold_out:
            changed=True
            worst_feature = pvalues.argmax()
            included.remove(worst_feature)
            if verbose:
                print('Drop {:30} with p-value {:.6}'.format(worst_feature, worst_pval))
        if not changed:
            break
    return included


variaveis = stepwise_selection(X_test, y_test)





st.write('## Melhores variáveis - Modelo Stepwise:')
variaveis


X = df_dummies[variaveis]
y = df_dummies['renda']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

y_pred = sm.OLS(y_train, X_train).fit().predict(X_test)

st.write(f'-->> R² com o Modelo Stepwise: {r2_score(y_test, y_pred)*100:2f}')


st.write('---')


st.write('## Melhor ajuste na árvore de regressão')

X = df_dummies[variaveis]
y = df_dummies['renda']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

reg_tree = DecisionTreeRegressor(random_state=42, max_depth=5, min_samples_leaf=13)
reg_tree.fit(X_train, y_train)

st.write('Realizando um melhor ajuste final no modelo, max_depth=5 e min_samples_leaf=13 ')
st.write(f'-->> Coeficiente de determinação R² na base de testes: {reg_tree.score(X=X_test, y=y_test)*100:2f}')

st.write('---')






on = st.toggle('Show Code')

if on:

    st.code('''
import streamlit as st 
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

import statsmodels.api as sm
import statsmodels.formula.api as smf

from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import r2_score
from sklearn.model_selection import train_test_split


st.set_page_config(
    page_title='Modelo de regressão - Previsão de renda',
    page_icon='⚙')


renda = pd.read_csv('./input/previsao_de_renda.csv')

renda.drop(columns= ['Unnamed: 0', 'id_cliente', 'data_ref', 'idade'], inplace= True)
renda['tempo_emprego'].fillna(0, inplace=True) 
renda = renda[renda['renda'] < 20000]  
renda = renda[renda['qtd_filhos'] < 14] 

df = renda.copy(deep=True)



df_dummies = pd.get_dummies(data= df.dropna(), drop_first= True).astype(int)

X = df_dummies.drop(columns='renda')
y = df_dummies['renda']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)




def stepwise_selection(X, y, 
                       initial_list=[], 
                       threshold_in=0.05, 
                       threshold_out = 0.05, 
                       verbose=True):
  
    included = list(initial_list)
    while True:
        changed=False
        
        # forward step
        excluded = list(set(X.columns)-set(included))
        new_pval = pd.Series(index=excluded, dtype=np.dtype('float64'))
        for new_column in excluded:
            model = sm.OLS(y, sm.add_constant(pd.DataFrame(X[included+[new_column]]))).fit()
            new_pval[new_column] = model.pvalues[new_column]
        best_pval = new_pval.min()
        if best_pval < threshold_in:
            best_feature = new_pval.index[new_pval.argmin()]
            included.append(best_feature)
            changed=True
            if verbose:
                 print('Add  {:30} with p-value {:.6}'.format(best_feature, best_pval))

        # backward step
        print("#############")
        print(included)
        model = sm.OLS(y, sm.add_constant(pd.DataFrame(X[included]))).fit()
        # use all coefs except intercept
        pvalues = model.pvalues.iloc[1:]
        worst_pval = pvalues.max() # null if pvalues is empty
        if worst_pval > threshold_out:
            changed=True
            worst_feature = pvalues.argmax()
            included.remove(worst_feature)
            if verbose:
                print('Drop {:30} with p-value {:.6}'.format(worst_feature, worst_pval))
        if not changed:
            break
    return included


variaveis = stepwise_selection(X_test, y_test)





st.write('## Melhores variáveis - Modelo Stepwise:')
variaveis


X = df_dummies[variaveis]
y = df_dummies['renda']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

y_pred = sm.OLS(y_train, X_train).fit().predict(X_test)

st.write(f'-->> R² com o Modelo Stepwise: {r2_score(y_test, y_pred)*100:2f}')


st.write('---')


st.write('## Melhor ajuste na árvore de regressão')

X = df_dummies[variaveis]
y = df_dummies['renda']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)

reg_tree = DecisionTreeRegressor(random_state=42, max_depth=5, min_samples_leaf=13)
reg_tree.fit(X_train, y_train)

st.write('Realizando um melhor ajuste final no modelo, max_depth=5 e min_samples_leaf=13 ')
st.write(f'-->> Coeficiente de determinação R² na base de testes: {reg_tree.score(X=X_test, y=y_test)*100:2f}')

st.write('---')''')