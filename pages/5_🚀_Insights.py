import streamlit as st


st.set_page_config(
    page_title='Insights - Previsão de renda',
    page_icon='🚀',
    layout= 'wide')




st.header(' Insights análise Bivariada')


st.write('''

- Renda x sexo --> o sexo Masculino (M) tem uma media de renda acima do que o sexo Feminino (F).


- Renda x idade --> percebe-se uma renda menor em pessoas mais novas, entre 22 a 34 anos.


- Renda x educacao --> as pessoas com superior completo possuem uma renda maior que a maioria.


- Renda x posse_de_veiculo --> as pessoas que possuem veiculo possuem uma renda maior que as pessoas sem veiculos.


- Renda x tipo_renda --> as pessoas que são servidores publicos possuem renda maior que as outras variaveis.


- Renda x q_tempo_emprego --> pessoas com um tempo de emprego maior possuem uma renda mais alta.''')


st.write('---')

st.header(' Insights modelo de regressão') 

st.write('Com base no que foi deservolvido até o momento no curso Cientista de dados, pode-se observar:')

st.write('''

- As variáveis mais significativas com o menor pvalue segundo modelo Stepwise são:
         

['tempo_emprego', 
'sexo_M', 
'tipo_renda_Pensionista', 
'tipo_renda_Empresário', 
'posse_de_imovel', 
'tipo_renda_Servidor público']
         

- Realizando um melhor ajuste final no modelo, max_depth=5 e min_samples_leaf=13 chego ao resultado de r² = 29.37
''')





on = st.toggle('Show Code')

if on:

    st.code('''
            

import streamlit as st


st.set_page_config(
    page_title='Insights - Previsão de renda',
    page_icon='🚀',
    layout= 'wide')




st.header(' Insights análise Bivariada')


st.write('

- Renda x sexo --> o sexo Masculino (M) tem uma media de renda acima do que o sexo Feminino (F).


- Renda x idade --> percebe-se uma renda menor em pessoas mais novas, entre 22 a 34 anos.


- Renda x educacao --> as pessoas com superior completo possuem uma renda maior que a maioria.


- Renda x posse_de_veiculo --> as pessoas que possuem veiculo possuem uma renda maior que as pessoas sem veiculos.


- Renda x tipo_renda --> as pessoas que são servidores publicos possuem renda maior que as outras variaveis.


- Renda x q_tempo_emprego --> pessoas com um tempo de emprego maior possuem uma renda mais alta.')


st.write('---')

st.header(' Insights modelo de regressão') 

st.write('Com base no que foi deservolvido até o momento no curso Cientista de dados, pode-se observar:')

st.write('

- As variáveis mais significativas com o menor pvalue segundo modelo Stepwise são:
         

['tempo_emprego', 
'sexo_M', 
'tipo_renda_Pensionista', 
'tipo_renda_Empresário', 
'posse_de_imovel', 
'tipo_renda_Servidor público']
         

- Realizando um melhor ajuste final no modelo, max_depth=5 e min_samples_leaf=13 chego ao resultado de r² = 29.37')
''') 


