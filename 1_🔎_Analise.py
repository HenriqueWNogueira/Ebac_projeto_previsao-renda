import streamlit as st
import pandas as pd 


st.set_page_config(
    page_title='Análise - Previsão de renda',
    page_icon= '🔎',
    layout= 'wide')



df = pd.read_csv('./input/previsao_de_renda.csv')
df  = df.drop(['Unnamed: 0'], axis=1) 


st.image('https://raw.githubusercontent.com/rhatiro/Credit-score/main/ebac-course-utils/media/logo/newebac_logo_black_half.png')
st.write('---')


st.write('### Profissão: Cientista de Dados')
st.write('Projeto: **Previsão de renda**') 
st.write('Por: Henrique W. Nogueira') 
st.write('---')

st.write('# Análise exploratória ')
st.write('')


st.write('### -- Entendimento do negócio:')
st.write('''Uma instituição financeira quer conhecer melhor o perfil de renda de seus novos clientes para diversos fins, por exemplo, melhor dimensionar o limite de cartões de crédito dos novos clientes, sem necessariamente solicitar olerites ou documentações que impactem na experiência do seu cliente.
Para isto, conduziu um estudo com alguns clientes, comprovando suas rendas através de olerites e outros documentos, e pretende construir um modelo preditivo para esta renda com base em algumas variáveis que já possui em seu banco de dados.''')



st.write('### -- Dicionário de dados:')
dados = pd.DataFrame({'Variável': df.columns,
            'Descrição': ['Data de referência de coleta das variáveis',
                            'Código de identificação do cliente',
                            'Sexo do cliente',
                            'Indica se o cliente possui veículo',
                            'Indica se o cliente possui imóvel',
                            'Quantidade de filhos do cliente',
                            'Tipo de renda do cliente',
                            'Grau de instrução do cliente',
                            'Estado civil do cliente',
                            'Tipo de residência do cliente (própria, alugada etc)',
                            'Idade do cliente',
                            'Tempo no emprego atual',
                'Quantidade de pessoas que moram na residência',
                'Renda em reais'],
                'Tipo': df.dtypes}).reset_index(drop= True)

dados 



st.write('### -- Dados utilizados:')
df 





on = st.toggle('Show Code')

if on:

    st.code('''
    
        
    import streamlit as st
    import pandas as pd 
            

    st.set_page_config(
        page_title='Previsão de renda',
        page_icon= ':bar_chart:',
        layout= 'wide')


    df = pd.read_csv('./input/previsao_de_renda.csv')
    df  = df.drop(['Unnamed: 0'], axis=1) 




    st.write('### Profissão: Cientista de Dados')
    st.write('Projeto: **Previsão de renda**') 
    st.write('Por: Henrique W. Nogueira') 
    st.write('---')

    st.write('# Análise exploratória ')
    st.write('')


    st.write('### -- Entendimento do negócio:')
    st.markdown('Uma instituição financeira quer conhecer melhor o perfil de renda de seus novos clientes para diversos fins, por exemplo, melhor dimensionar o limite de cartões de crédito dos novos clientes, sem necessariamente solicitar olerites ou documentações que impactem na experiência do seu cliente.
    Para isto, conduziu um estudo com alguns clientes, comprovando suas rendas através de olerites e outros documentos, e pretende construir um modelo preditivo para esta renda com base em algumas variáveis que já possui em seu banco de dados.')



    
    dados = pd.DataFrame({'Variável': df.columns,
                'Descrição': ['Data de referência de coleta das variáveis',
                                'Código de identificação do cliente',
                                'Sexo do cliente',
                                'Indica se o cliente possui veículo',
                                'Indica se o cliente possui imóvel',
                                'Quantidade de filhos do cliente',
                                'Tipo de renda do cliente',
                                'Grau de instrução do cliente',
                                'Estado civil do cliente',
                                'Tipo de residência do cliente (própria, alugada etc)',
                                'Idade do cliente',
                                'Tempo no emprego atual',
                                'Quantidade de pessoas que moram na residência',
                                'Renda em reais'],
                                'Tipo': df.dtypes}).reset_index(drop= True) 

    dados
                    
                    
    st.write('### -- Dados utilizados:')
    df''')

      



        
        


            



