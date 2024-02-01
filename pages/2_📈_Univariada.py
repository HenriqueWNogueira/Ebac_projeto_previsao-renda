import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import seaborn as sns
import numpy as np

st.set_page_config(
    page_title='Univariada - Previsão de renda',
    page_icon='📈')


renda = pd.read_csv('./input/previsao_de_renda.csv')


st.markdown('''# Gráficos Univariada''')

opcao = st.selectbox('Escolha uma variável:',
                     ('Renda', 'Quantidade de pessoas na residência',
                      'Tempo de emprego', 'Idade',
                      'Tipo de residência', 'Estado civil',
                      'Educacão', 'Tipo de renda',
                      'Quantidade de filhos', 'Posse de imóvel',
                      'Posse de veiculo', 'Sexo'))


if opcao == 'Renda':
    plt.close('all')
    st.markdown('## Univariada renda')
    fig, axs = plt.subplots(3, figsize=[20,20])
    sns.boxplot(renda, y='renda', ax=axs[0])
    sns.histplot(renda, x='renda', bins=50, ax=axs[1])
    renda['renda'].plot()
    plt.ylim(0)
    plt.xlim(0)
    plt.ylabel('renda')
    with st.spinner('Aguarde...'):
        st.pyplot(fig)


elif opcao == 'Quantidade de pessoas na residência':
    plt.close('all')
    st.markdown('## Univariada qt_pessoas_residencia ')
    fig, axs = plt.subplots(2, figsize=[20,20])
    sns.boxplot(renda, y='qt_pessoas_residencia', ax=axs[0])
    renda['qt_pessoas_residencia'].value_counts().plot.bar()
    with st.spinner('Aguarde...'):
        st.pyplot(fig)

elif opcao == 'Tempo de emprego':
    plt.close('all')
    st.markdown(' ## Univariada tempo_emprego')
    fig, axs = plt.subplots(2, figsize=[20,20])
    sns.histplot(renda, x='tempo_emprego', bins=50, ax=axs[0])
    sns.boxplot(renda, y='tempo_emprego', ax=axs[1])
    with st.spinner('Aguarde...'):
        st.pyplot(fig)

elif opcao == 'Idade':
    plt.close('all')
    st.markdown('## Univariada idade')
    ticks = list(np.arange(0, 600, 50))
    fig, ax = plt.subplots(figsize=[20, 20])
    ax.yaxis.set_ticks(ticks)
    renda['idade'].value_counts().plot.bar()
    with st.spinner('Aguarde...'):
        st.pyplot(fig)

elif opcao == 'Tipo de residência':
    plt.close('all')
    st.markdown('## Univariada tipo_residencia')
    fig = plt.figure(figsize=[20,20])
    sns.histplot(renda, x='tipo_residencia')
    plt.xticks(rotation=60)
    with st.spinner('Aguarde...'):
        st.pyplot(fig)

elif opcao == 'Estado civil':
    plt.close('all')
    st.markdown('## Univariada estado_civil')
    fig = plt.figure(figsize=[20,20])
    sns.histplot(renda, x='estado_civil')
    with st.spinner('Aguarde...'):
        st.pyplot(fig)

elif opcao == 'Educacão':
    plt.close('all')
    st.markdown('## Univariada educacao')
    fig = plt.figure(figsize=[20,10])
    sns.histplot(renda, x='educacao')
    plt.xticks(rotation=90)
    with st.spinner('Aguarde...'):
        st.pyplot(fig)

elif opcao == 'Tipo de renda':
    plt.close('all')
    st.markdown('## Univariada tipo_renda')
    fig = plt.figure(figsize=[20,10])
    sns.histplot(renda, x='tipo_renda')
    plt.xticks(rotation=90)
    with st.spinner('Aguarde...'):
        st.pyplot(fig)

elif opcao == 'Quantidade de filhos':
    plt.close('all')
    st.markdown('## Univariada qtd_filhos')
    fig, axs = plt.subplots(2, figsize=[20,20])
    sns.histplot(renda, x='qtd_filhos', bins=40, ax=axs[0])
    sns.boxplot(renda, y='qtd_filhos', ax=axs[1])
    with st.spinner('Aguarde...'):
        st.pyplot(fig)

elif opcao == 'Posse de imóvel':
    plt.close('all')
    st.markdown('## Univariada posse_de_imovel')
    fig = plt.figure(figsize=[20,20])
    renda['posse_de_imovel'].value_counts().plot.bar()
    with st.spinner('Aguarde...'):
        st.pyplot(fig)

elif opcao == 'Posse de veiculo':
    plt.close('all')
    st.markdown('## Univariada posse_de_veiculo')
    fig = plt.figure(figsize=[20,20])
    renda['posse_de_veiculo'].value_counts().plot.bar()
    with st.spinner('Aguarde...'):
        st.pyplot(fig)

elif opcao == 'Sexo':
    plt.close('all')
    st.markdown('## Univariada sexo')
    fig = plt.figure(figsize=[20,20])
    renda['sexo'].value_counts().plot.bar()
    with st.spinner('Aguarde...'):
        st.pyplot(fig)





on = st.toggle('Show Code')

if on:

    st.code('''

    import matplotlib.pyplot as plt
    import streamlit as st
    import pandas as pd
    import seaborn as sns
    import numpy as np

    st.set_page_config(
        page_title='Univariada - Previsão de renda',
        page_icon='📈')


    renda = pd.read_csv('./input/previsao_de_renda.csv')


    st.markdown('# Gráficos Univariada')

    opcao = st.selectbox('Escolha uma variável:',
                        ('Renda', 'Quantidade de pessoas na residência',
                        'Tempo de emprego', 'Idade',
                        'Tipo de residência', 'Estado civil',
                        'Educacão', 'Tipo de renda',
                        'Quantidade de filhos', 'Posse de imóvel',
                        'Posse de veiculo', 'Sexo'))


    if opcao == 'Renda':
        plt.close('all')
        st.markdown('## Univariada renda')
        fig, axs = plt.subplots(3, figsize=[20,20])
        sns.boxplot(renda, y='renda', ax=axs[0])
        sns.histplot(renda, x='renda', bins=50, ax=axs[1])
        renda['renda'].plot()
        plt.ylim(0)
        plt.xlim(0)
        plt.ylabel('renda')
        with st.spinner('Aguarde...'):
            st.pyplot(fig)


    elif opcao == 'Quantidade de pessoas na residência':
        plt.close('all')
        st.markdown('## Univariada qt_pessoas_residencia ')
        fig, axs = plt.subplots(2, figsize=[20,20])
        sns.boxplot(renda, y='qt_pessoas_residencia', ax=axs[0])
        renda['qt_pessoas_residencia'].value_counts().plot.bar()
        with st.spinner('Aguarde...'):
            st.pyplot(fig)

    elif opcao == 'Tempo de emprego':
        plt.close('all')
        st.markdown(' ## Univariada tempo_emprego')
        fig, axs = plt.subplots(2, figsize=[20,20])
        sns.histplot(renda, x='tempo_emprego', bins=50, ax=axs[0])
        sns.boxplot(renda, y='tempo_emprego', ax=axs[1])
        with st.spinner('Aguarde...'):
            st.pyplot(fig)

    elif opcao == 'Idade':
        plt.close('all')
        st.markdown('## Univariada idade')
        ticks = list(np.arange(0, 600, 50))
        fig, ax = plt.subplots(figsize=[20, 20])
        ax.yaxis.set_ticks(ticks)
        renda['idade'].value_counts().plot.bar()
        with st.spinner('Aguarde...'):
            st.pyplot(fig)

    elif opcao == 'Tipo de residência':
        plt.close('all')
        st.markdown('## Univariada tipo_residencia')
        fig = plt.figure(figsize=[20,20])
        sns.histplot(renda, x='tipo_residencia')
        plt.xticks(rotation=60)
        with st.spinner('Aguarde...'):
            st.pyplot(fig)

    elif opcao == 'Estado civil':
        plt.close('all')
        st.markdown('## Univariada estado_civil')
        fig = plt.figure(figsize=[20,20])
        sns.histplot(renda, x='estado_civil')
        with st.spinner('Aguarde...'):
            st.pyplot(fig)

    elif opcao == 'Educacão':
        plt.close('all')
        st.markdown('## Univariada educacao')
        fig = plt.figure(figsize=[20,20])
        sns.histplot(renda, x='educacao')
        plt.xticks(rotation=90)
        with st.spinner('Aguarde...'):
            st.pyplot(fig)

    elif opcao == 'Tipo de renda':
        plt.close('all')
        st.markdown('## Univariada tipo_renda')
        fig = plt.figure(figsize=[20,20])
        sns.histplot(renda, x='tipo_renda')
        plt.xticks(rotation=90)
        with st.spinner('Aguarde...'):
            st.pyplot(fig)

    elif opcao == 'Quantidade de filhos':
        plt.close('all')
        st.markdown('## Univariada qtd_filhos')
        fig, axs = plt.subplots(2, figsize=[20,20])
        sns.histplot(renda, x='qtd_filhos', bins=40, ax=axs[0])
        sns.boxplot(renda, y='qtd_filhos', ax=axs[1])
        with st.spinner('Aguarde...'):
            st.pyplot(fig)

    elif opcao == 'Posse de imóvel':
        plt.close('all')
        st.markdown('## Univariada posse_de_imovel')
        fig = plt.figure(figsize=[20,20])
        renda['posse_de_imovel'].value_counts().plot.bar()
        with st.spinner('Aguarde...'):
            st.pyplot(fig)

    elif opcao == 'Posse de veiculo':
        plt.close('all')
        st.markdown('## Univariada posse_de_veiculo')
        fig = plt.figure(figsize=[20,20])
        renda['posse_de_veiculo'].value_counts().plot.bar()
        with st.spinner('Aguarde...'):
            st.pyplot(fig)

    elif opcao == 'Sexo':
        plt.close('all')
        st.markdown('## Univariada sexo')
        fig = plt.figure(figsize=[20,20])
        renda['sexo'].value_counts().plot.bar()
        with st.spinner('Aguarde...'):
            st.pyplot(fig)''')




